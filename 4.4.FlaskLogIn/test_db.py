import psycopg2

# Database connection parameters
AUTH_HOST = '49.13.94.198'
AUTH_USER = 'Masoud'
AUTH_PASSWORD = 'Mikhandi91!'
AUTH_DATABASE = 'auth'
POSTGRES_PORT = 5432

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=AUTH_HOST,
        user=AUTH_USER,
        password=AUTH_PASSWORD,
        database=AUTH_DATABASE,
        port=POSTGRES_PORT
    )

    cursor = connection.cursor()
    
    # Query to select all records from the admins table
    cursor.execute("SELECT * FROM admins;")
    
    # Fetch all records
    records = cursor.fetchall()

    print("Records from admins table:")
    for record in records:
        print(record)

except psycopg2.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
