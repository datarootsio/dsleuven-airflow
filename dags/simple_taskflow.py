from airflow.decorators import dag, task
from pendulum import datetime


@dag(
    schedule="*/3 * * * *",
    start_date=datetime(2023, 5, 2),
    catchup=False,
    tags=["taskflow"],
)
def simple_taskflow():
    @task
    def hello():
        print("Hello, DS Leuven!")

    @task
    def how_are_you():
        print("How are you, DS Leuven?")

    @task
    def goodbye():
        print("Goodbye, DS Leuven!")

    hello() >> how_are_you() >> goodbye()


simple_taskflow()
