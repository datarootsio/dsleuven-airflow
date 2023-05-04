from airflow import DAG
from pendulum import datetime
from airflow.operators.bash import BashOperator

with DAG(
    "simple_old_style_bash",
    description="Example of a simple DAG following the Airflow 1 style",
    schedule="*/3 * * * *",
    start_date=datetime(2023, 5, 2),
    catchup=False,
    tags=["taskflow"],
) as dag:
    hello = BashOperator(task_id="hello", bash_command="echo 'Hello, DS Leuven!'")
    how_are_you = BashOperator(
        task_id="how_are_you", bash_command="echo 'How are you, DS Leuven?'"
    )
    goodbye = BashOperator(task_id="goodbye", bash_command="echo 'Goodbye, DS Leuven!'")

    hello >> how_are_you >> goodbye
