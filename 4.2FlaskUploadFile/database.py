from sqlmodel import Field, SQLModel, create_engine, Session, select

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str
    username: str
    password: str

DATABASE_URL = 'sqlite:///./database.db'
# DATABASE_URL = 'postgresql://root:n1pWuZc7GruapxRavKzYp2Lu@chatbotdb:5432/postgres'
engine = create_engine(DATABASE_URL, echo=True)

# Create the database tables
SQLModel.metadata.create_all(engine)

def get_user_by_username(username: str):
    with Session(engine) as db_session:
        statement = select(User).where(User.username == username)
        return db_session.exec(statement).first()

def create_user(db_session, name, surname, email, username, password):
    user = User(name=name, surname=surname, email=email, username=username, password=password)
    with Session(engine) as db_session:
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
    return user
