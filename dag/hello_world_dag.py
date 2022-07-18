from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello World...Ankush has written his first airflow DAG");


with DAG(dag_id="hello_world_dag",
         start_date=datetime(2022,7,17),
         schedule_interval="@hourly",
         catchup=True) as dag:
    task1 =PythonOperator(task_id="Hello_World",python_callable=helloWorld);

task1