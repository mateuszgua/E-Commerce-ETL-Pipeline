FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir apache-airflow

COPY . .

EXPOSE 8080

# ENV AIRFLOW_HOME=/app/airflow
ENV AIRFLOW_HOME=/airflow

CMD airflow db init && airflow webserver --port 8080
