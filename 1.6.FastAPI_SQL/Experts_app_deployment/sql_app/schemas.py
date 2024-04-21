from pydantic import BaseModel


class CourseBase(BaseModel):
    unit: int
    name: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    firstname: str
    lastname: str
    average: float
    graduated: bool


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    courses: list[Course] = []

    class Config:
        orm_mode = True