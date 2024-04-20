# FastAPI Project
## Description
This project is designed to demonstrate the implementation of a FastAPI application with two different modes: Beginner mode and Expert mode. The Beginner mode focuses on basic CRUD operations with a SQLite database, while the Expert mode extends functionality to utilize PostgreSQL database and implements more complex data structures.


## Prerequisites
Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- Docker (for Expert mode, PostgreSQL setup)
- Git (optional)


## Installation
- Clone this repository:
```
git clone <repository_url>
```

- Navigate to the project directory:
```
cd <project_directory>
```

- Install dependencies:
```
pip install -r requirements.txt
```

## Usage
### Beginner Mode
Use SQLAlchemy package to connect your SQLite database to your FastAPI project.
Create a User class with id, name, and email attributes.
Implement GET, POST, PUT, DELETE methods to manipulate data in the database.


### Expert Mode
Follow the FastAPI SQL Databases Tutorial to set up PostgreSQL database.
Create Student and Course classes with appropriate attributes.
Utilize PostgreSQL database instead of SQLite by configuring SQLAlchemy database URL.

- Pull PostgreSQL Docker image:
```
docker pull postgres
```

- Run PostgreSQL Docker container:
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=<password> -e POSTGRES_USER=<username> -e POSTGRES_DB=<database_name> -d postgres
```

- Change SQLAlchemy database URL in the project:
```
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/<database_name>"
```

Implement the required functionality for Student and Course classes.
Don't forget to update .gitignore, readme.md, and requirements.txt files accordingly.


## Contribution
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.