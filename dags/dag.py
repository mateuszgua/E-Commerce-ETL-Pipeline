from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, World!")

def print_date():
    print("Current date is:", datetime.now().date())

with DAG('my_dag', start_date=datetime(2023, 5, 1), schedule_interval='@daily') as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "Executing Task 1"',
    )

    task2 = PythonOperator(
        task_id='task2',
        python_callable=hello_world,
    )

    task3 = PythonOperator(
        task_id='task3',
        python_callable=print_date,
    )

    task1 >> task2 >> task3
