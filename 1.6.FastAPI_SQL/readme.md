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
git clone https://github.com/masoud-n91/Python-For-Development.git
```

- Navigate to the project directory:
```
cd .\Python-For-Development\1.6.FastAPI_SQL\
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

- Pull PostgreSQL Docker image:
```
docker pull postgres
```

- Run PostgreSQL Docker container:
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=<password> -e POSTGRES_USER=<username> -e POSTGRES_DB=<database_name> -d postgres
```

- Run the code by starting uvicorn:
```
uvicorn sql_app.main:app
``` 

- Note: for now, the default username, password, and database_name is Masoud, Which_password, and UniversityStudents. If you want to use the default settings, just use the following line to run the container:

```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=Which_password -e POSTGRES_USER=Masoud -e POSTGRES_DB=UniversityStudents -d postgres
```

If you want to change the default setting, you have to update the database.py script, accordingly.


## Contribution
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.