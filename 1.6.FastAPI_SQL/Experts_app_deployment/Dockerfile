FROM python:3.9

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=qdi3HbMlExVTYrTUz3UTe4ZH
ENV POSTGRES_DB=postgres
ENV DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@university-students:5432/${POSTGRES_DB}

WORKDIR /app

COPY . /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "sql_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
