from pendulum import datetime
from airflow.decorators import dag, task
from airflow.datasets import Dataset

produced_dataset = Dataset("s3://dataset-bucket/example.csv")


@dag(
    schedule="*/3 * * * *",
    start_date=datetime(2023, 5, 2),
    catchup=False,
    tags=["datasets"],
)
def dataset_sender():
    @task(outlets=[produced_dataset])
    def i_produce_a_dataset():
        print("dataset produced")

    i_produce_a_dataset()


dataset_sender()
