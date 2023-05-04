from airflow import DAG
from pendulum import datetime
from airflow.operators.python import PythonOperator

with DAG(
    "simple_old_style_python",
    description="Example of a simple DAG following the Airflow 1 style",
    schedule=None,
    start_date=datetime(2023, 5, 2),
    catchup=False,
    tags=["taskflow"],
) as dag:

    def hello_func():
        print("Hello, DS Leuven!")

    def how_are_you_func():
        print("How are you, DS Leuven?")

    def goodbye_func():
        print("Goodbye, DS Leuven!")

    hello = PythonOperator(task_id="hello", python_callable=hello_func)
    how_are_you = PythonOperator(
        task_id="how_are_you", python_callable=how_are_you_func
    )
    goodbye = PythonOperator(task_id="goodbye", python_callable=goodbye_func)

    hello >> how_are_you >> goodbye
