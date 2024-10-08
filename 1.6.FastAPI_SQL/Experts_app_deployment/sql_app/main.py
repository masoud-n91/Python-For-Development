from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Student management": "You are going to to shocked by the power of our API :)"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, firstname=user.firstname, lastname=user.lastname)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/courses/", response_model=schemas.Course)
def create_course_for_user(
    user_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)
):
    return crud.create_user_course(db=db, course=course, user_id=user_id)


@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    response = crud.remove_user_id(id=user_id, db=db)
    return response


@app.put("/users/{user_id}")
def update_user(user_id: int, firstname: str = None, lastname: str = None, average: float = None, graduated: bool = None, db: Session = Depends(get_db)):
    if not firstname and not lastname and not average and not graduated:
        raise HTTPException(status_code=400, detail="No information is provided to update")
    response = crud.edit_user_id(id=user_id, db=db, firstname=firstname, lastname=lastname, average=average, graduated=graduated)
    return response