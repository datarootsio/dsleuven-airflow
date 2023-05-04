from airflow.decorators import dag, task
from pendulum import datetime


@dag(schedule=None, start_date=datetime(2023, 5, 2), catchup=False, tags=["taskflow"])
def simple_taskflow_with_args():
    @task
    def hello():
        print("Hello, DS Leuven!")
        return 2

    @task
    def how_are_you(random_number: int):
        print("How are you, DS Leuven? The random number was " + str(random_number))

    @task
    def goodbye():
        print("Goodbye, DS Leuven!")

    how_are_you(hello()) >> goodbye()


simple_taskflow_with_args()
