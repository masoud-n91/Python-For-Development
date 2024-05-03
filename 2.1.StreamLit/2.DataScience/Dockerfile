FROM python:3.10-slim

EXPOSE 8501

COPY . /app
WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

# Run
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]