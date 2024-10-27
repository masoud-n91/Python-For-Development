from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.ext.declarative import declared_attr
from dotenv import load_dotenv
from datetime import datetime
import os
import pytz

# Load environment variables
load_dotenv()

paris_tz = pytz.timezone("Europe/Paris")

# SQLAlchemy base
Base = declarative_base()

# SQLAlchemy Models
class Admins(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    family_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    join_time = Column(DateTime, default=lambda: datetime.now(tz=paris_tz))

class Guests(Base):
    __tablename__ = 'guests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    family_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    join_time = Column(DateTime, default=lambda: datetime.now(tz=paris_tz))
    comments = relationship("Comments", back_populates="guest")

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    family_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    sutdent_number = Column(String, unique=True)
    is_active = Column(Boolean, default=False)
    join_time = Column(DateTime, default=lambda: datetime.now(tz=paris_tz))

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("guests.id"))
    comment = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(tz=paris_tz))
    guest = relationship("Guests", back_populates="comments")

# Database connection configuration
def get_engine(auth=True):
    if auth:
        host = os.getenv('AUTH_HOST')
        username = os.getenv('AUTH_USER')
        password = os.getenv('AUTH_PASSWORD')
        database = os.getenv('AUTH_DATABASE')
    else:
        host = os.getenv('DATA_HOST')
        username = os.getenv('DATA_USER')
        password = os.getenv('DATA_PASSWORD')
        database = os.getenv('DATA_DATABASE')
    
    port = os.getenv('POSTGRES_PORT', 5432)  # Default port for PostgreSQL
    return create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Create a session
engine = get_engine(auth=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=get_engine())

# CRUD operations
def get_admin_by_email(email):
    session = Session()
    admin = session.query(Admins).filter_by(email=email).first()
    session.close()
    return admin

def get_admin_by_id(admin_id):
    session = Session()
    admin = session.query(Admins).get(admin_id)
    session.close()
    return admin

def get_guest_by_email(email):
    session = Session()
    guest = session.query(Guests).filter_by(email=email).first()
    session.close()
    return guest

def get_guest_by_id(guest_id):
    session = Session()
    guest = session.query(Guests).get(guest_id)
    session.close()
    return guest

def activate_guest(email):
    session = Session()
    guest = session.query(Guests).filter_by(email=email).first()
    if guest:
        guest.is_active = True
        session.commit()
    session.close()

def delete_user(database, email):
    session = Session()
    if database == 'guests':
        session.query(Guests).filter_by(email=email).delete()
    elif database == 'admins':
        session.query(Admins).filter_by(email=email).delete()
    session.commit()
    session.close()

def update_password(table, email, password):
    session = Session()
    if table == 'guests':
        guest = session.query(Guests).filter_by(email=email).first()
        if guest:
            guest.password = password
    elif table == 'admins':
        admin = session.query(Admins).filter_by(email=email).first()
        if admin:
            admin.password = password
    session.commit()
    session.close()

def read_admins():
    session = Session()
    admins = session.query(Admins).all()
    session.close()
    return admins

def create_user(database, first_name, family_name, email, password, join_time, student_number=None):
    session = Session()
    if database == "students":
        new_user = Students(first_name=first_name, family_name=family_name, sutdent_number=str(student_number),
                            email=email, password=password, is_active=False, join_time=join_time)
    elif database == "admins":
        new_user = Admins(first_name=first_name, family_name=family_name,
                          email=email, password=password, is_active=False, join_time=join_time)
    else:
        new_user = Guests(first_name=first_name, family_name=family_name,
                          email=email, password=password, is_active=False, join_time=join_time)
    
    session.add(new_user)
    session.commit()
    session.close()

def fetch_table_data(table_name):
    session = Session()
    data = session.execute(f"SELECT * FROM {table_name}").fetchall()
    column_names = data[0].keys() if data else []
    rows = [dict(row) for row in data]
    session.close()
    return {'columns': column_names, 'rows': rows}

def fetch_table_auth(table_name):
    return fetch_table_data(table_name)

def submit_comment(user_id, comment):
    session = Session()
    new_comment = Comments(user_id=user_id, comment=comment)
    session.add(new_comment)
    session.commit()
    session.close()


def get_comments():
    session = Session()
    comments = session.query(Comments).all()

    # Convert the comments to a list of dictionaries for easier reading
    comments_list = [
        {
            "id": comment.id,
            "user_id": comment.user_id,
            "comment": comment.comment,
            "created_at": comment.created_at
        }
        for comment in comments
    ]

    session.close()
    return comments_list
