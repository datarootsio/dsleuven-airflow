from airflow.decorators import dag, task
from pendulum import datetime
import os
from airflow.api.client.local_client import Client
import time


@dag(schedule=None, catchup=False, start_date=datetime(2023, 5, 2), tags=["dynamic"])
def dynamic_task_mapping_problem():
    @task(multiple_outputs=False)
    def read_from_file() -> list[str]:
        content = os.listdir("/sample_data")
        return content

    @task
    def process_files(file_list: list[str]):
        airflow_client = Client(None)
        for file_name in file_list:
            airflow_client.trigger_dag(
                dag_id="process_file",
                replace_microseconds=False,
                conf={
                    "file_name": file_name,
                },
            )
            time.sleep(5)

    process_files(read_from_file())


dynamic_task_mapping_problem()
