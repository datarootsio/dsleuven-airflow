from airflow.decorators import dag, task
from pendulum import datetime
import os


@dag(schedule=None, catchup=False, start_date=datetime(2023, 5, 2), tags=["dynamic"])
def process_file(file_name: str | None = None):
    @task
    def process_file_task(file_name: str | None = None):
        assert file_name is not None

        source_file_full_path = os.path.join("/sample_data", file_name)

        with open(source_file_full_path, "r") as f:
            print("The content of the file is:")
            print(f.read())

    process_file_task(file_name)


process_file()
