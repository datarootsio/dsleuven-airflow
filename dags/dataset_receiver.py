from pendulum import datetime
from airflow.decorators import dag, task
from airflow.datasets import Dataset

produced_dataset = Dataset("s3://dataset-bucket/example.csv")


@dag(
    schedule=[produced_dataset],
    start_date=datetime(2023, 5, 2),
    catchup=False,
    tags=["datasets"],
)
def dataset_receiver():
    @task
    def i_process_a_dataset():
        print("dataset processed")

    i_process_a_dataset()


dataset_receiver()
