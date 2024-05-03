FROM python:3.10-slim

EXPOSE 8501

RUN pip install -U pip
RUN pip install streamlit

COPY . /app
WORKDIR /app

# Run
ENTRYPOINT ["streamlit", "run", "counter.py", "--server.port=8501", "--server.address=0.0.0.0"]