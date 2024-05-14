FROM python:3.10.11-slim-buster

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

CMD ["streamlit", "run", "--server.port=8000", "--server.address=0.0.0.0", "app.py"]
