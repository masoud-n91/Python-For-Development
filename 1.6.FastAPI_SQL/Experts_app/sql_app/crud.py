from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, firstname: str, lastname: str):
    return db.query(models.User).filter(models.User.firstname == firstname, models.User.lastname == lastname).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(firstname=user.firstname, lastname=user.lastname, average=user.average, graduated=user.graduated)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def create_user_course(db: Session, course: schemas.CourseCreate, user_id: int):
    db_course = models.Course(name=course.name, unit=course.unit, owner_id=user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course