# 
FROM python:3.9.7-slim-buster

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY ./todo.db /code/todo.db

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]