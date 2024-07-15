import psycopg2
from dotenv import load_dotenv
import os
from pydantic import BaseModel


class User(BaseModel):
    id: int
    first_name: str
    family_name: str
    email: str
    password: str
    is_active: bool

load_dotenv()


auth_host = os.getenv('AUTH_HOST')
auth_username = os.getenv('AUTH_USER')
auth_password = os.getenv('AUTH_PASSWORD')
auth_database = os.getenv('AUTH_DATABASE')

data_host = os.getenv('DATA_HOST')
data_username = os.getenv('DATA_USER')
data_password = os.getenv('DATA_PASSWORD')
data_database = os.getenv('DATA_DATABASE')

port = int(os.getenv('POSTGRES_PORT'))

def auth_connection():

    # try:
    
    connection = psycopg2.connect(
        database=auth_database,
        user=auth_username,
        password=auth_password,
        host=auth_host,
        port=port,
    )
    print("Connection to PostgreSQL DB successful")
        
    connection.autocommit = True
    cursor = connection.cursor()
    return connection, cursor

    # except Exception as e:
    #     print(f"The error '{e}' occurred")

    # return None, None    


def data_connection():
    
    # try:
    connection = psycopg2.connect(
        database=data_database,
        user=data_username,
        password=data_password,
        host=data_host,
        port=port,
    )
    print("Connection to PostgreSQL DB successful")
        
    connection.autocommit = True
    cursor = connection.cursor()
    return connection, cursor

    # except Exception as e:
    #     print(f"The error '{e}' occurred")

    # return None, None    


def get_column_names(cursor, database, table_name):
    cursor.execute(f"""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = '{table_name}'
    ORDER BY ORDINAL_POSITION
    """)
    columns_info = cursor.fetchall()

    print("columns_info: ", columns_info)

    return [column[0] for column in columns_info]


def get_admin_by_email(email):
    connection, cursor = auth_connection()
    table = "admins"
    query = f"SELECT * FROM {table} WHERE email = '{email}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        column_names = get_column_names(cursor, auth_database, table)
        admin = User(**dict(zip(column_names, user)))
        cursor.close()
        connection.close()
        return admin

    return None


def get_admin_by_id(id):
    connection, cursor = auth_connection()
    table = "admins"
    query = f"SELECT * FROM {table} WHERE id = '{id}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        column_names = get_column_names(cursor, auth_database, table)
        admin = User(**dict(zip(column_names, user)))
        cursor.close()
        connection.close()
        return admin

    return None


def get_guest_by_email(email):
    connection, cursor = auth_connection()
    table = "guests"
    query = f"SELECT * FROM {table} WHERE email = '{email}'"
    cursor.execute(query)
    user = cursor.fetchone()
    print("Guest by email: ", user)

    if user:
        print("auth_database: ", auth_database, "table: ", table)
        column_names = get_column_names(cursor, auth_database, table)
        print("User: ", user)
        print("column_names: ", column_names)
        guest = User(**dict(zip(column_names, user)))
        print("Guest by email: ", guest)
        cursor.close()
        connection.close()
        return guest
    
    return None


def get_guest_by_id(id):
    connection, cursor = auth_connection()
    table = "guests"
    query = f"SELECT * FROM {table} WHERE id = '{id}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        column_names = get_column_names(cursor, auth_database, table)
        guest = User(**dict(zip(column_names, user)))
        print("Guest by id: ", guest)
        cursor.close()
        connection.close()
        return guest

    return None


def activate_guest(email):
    print("is_active: ", email)
    connection, cursor = auth_connection()
    table = "guests"
    query = f"UPDATE {table} SET is_active = TRUE WHERE email = '{email}'"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def delete_user(database, email):
    connection, cursor = auth_connection()
    table = database
    query = f"DELETE FROM {table} WHERE email = '{email}'"
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def update_password(table, email, password):
    connection, cursor = auth_connection()
    print(f"table: {table}, email: {email}, password: {password}")
    query = f"UPDATE {table} SET password = %s WHERE email = %s"
    values = (password, email)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_student_by_email(email):
    connection, cursor = auth_connection()
    table = "students"
    query = f"SELECT * FROM {table} WHERE email = '{email}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        column_names = get_column_names(cursor, auth_database, table)
        student = User(**dict(zip(column_names, user)))
        cursor.close()
        connection.close()
        return student

    return None


def get_student_by_id(id):
    connection, cursor = auth_connection()
    table = "students"
    query = f"SELECT * FROM {table} WHERE id = '{id}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        column_names = get_column_names(cursor, auth_database, table)
        student = User(**dict(zip(column_names, user)))
        cursor.close()
        connection.close()
        return student

    return None


def create_user(database, first_name, family_name, email, password, student_number = None):
    connection, cursor = auth_connection()
    table = database
    
    if table == "students":
        query = f"INSERT INTO {table} (first_name, family_name, student_number, email, password, is_active) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, family_name, student_number, email, password, False)
    else:
        query = f"INSERT INTO {table} (first_name, family_name, email, password, is_active) VALUES (%s, %s, %s, %s, %s)"
        values = (first_name, family_name, email, password, False)
    
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


def get_tables():
    conn, cursor = data_connection()
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    cursor.close()
    conn.close()
    return tables


def fetch_table_data(table_name):
    conn, cursor = data_connection()
    cursor.execute(f"SELECT * FROM {table_name}")

    columns = cursor.column_names

    raw_rows = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    rows = translate_foriegn_keys(cursor, raw_rows, column_names)

    cursor.close()
    conn.close()

    modified_columns = tuple(column for column in columns if column != 'id')
    modified_rows = [tuple_[1:] for tuple_ in rows]

    return {'columns': modified_columns, 'rows': modified_rows}


def fetch_table_auth(table_name):
    conn, cursor = auth_connection()
    cursor.execute(f"SELECT * FROM {table_name}")

    columns = cursor.column_names

    raw_rows = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    rows = translate_foriegn_keys(cursor, raw_rows, column_names)

    cursor.close()
    conn.close()

    modified_columns = tuple(column for column in columns if column != 'id')
    modified_rows = [tuple_[1:] for tuple_ in rows]

    return {'columns': modified_columns, 'rows': modified_rows}


def translate_foriegn_keys(cursor, rows, columns):
    translator = {}
    for idx, column in enumerate(columns):
        temp = column.split("_")
        if (len(temp) >= 2 and temp[-1] == "id") or (temp[0] == "M1" or temp[0] == "M2"):
            f_table_name = temp[0].capitalize() + "s"
            if temp[0] == "M1" or temp[0] == "M2":
                f_table_name = "Years"
            translator[str(idx)] = {}
            query = f"SELECT id, full_name FROM {f_table_name}"
            cursor.execute(query)
            full_names = cursor.fetchall()
            for name in full_names:
                translator[str(idx)][name[0]] = name[1]

    list_rows = []
    for row in list(rows):
        row1 = list(row)
        for idx, value in enumerate(row1):
            if str(idx) in translator:
                if value in translator[str(idx)].keys():
                    row1[idx] = translator[str(idx)][value]
        list_rows.append(tuple(row1))

    return list_rows


def read_pending_activations(tables):

    conn, cursor = auth_connection()
    for table in tables:
        query = f"SELECT * FROM {table} WHERE is_active = 0"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            cursor.close()
            conn.close()
            return True

    cursor.close()
    conn.close()
    return False
