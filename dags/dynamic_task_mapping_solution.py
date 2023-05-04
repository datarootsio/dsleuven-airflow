from airflow.decorators import dag, task
from pendulum import datetime
import os


@dag(schedule=None, catchup=False, start_date=datetime(2023, 5, 2), tags=["dynamic"])
def dynamic_task_mapping_solution():
    @task(multiple_outputs=False)
    def read_from_file() -> list[str]:
        content = os.listdir("/sample_data")
        return content

    @task
    def process_file(file_name: str):
        source_file_full_path = os.path.join("/sample_data", file_name)

        with open(source_file_full_path, "r") as f:
            print("The content of the file is:")
            print(f.read())

    process_file.expand(file_name=read_from_file())


dynamic_task_mapping_solution()
