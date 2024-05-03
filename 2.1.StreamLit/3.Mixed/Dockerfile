FROM python:3.10-slim

EXPOSE 8501

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U pip
RUN pip install -r requirements.txt

# Run
ENTRYPOINT ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]