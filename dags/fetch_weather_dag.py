from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount


with DAG(
    dag_id="fetch_weather_dag",
    schedule_interval="@hourly",
    start_date=days_ago(1),
    catchup=False,
    tags=["weather-analysis"],
) as dag:

    analyze_weather = DockerOperator(
        task_id="fetch_weather",
        image="weather-analysis:latest",
        api_version="auto",
        auto_remove=True,
        command="python /app/app/run_fetch.py",
        mounts=[
            Mount(source="data", target="/app/data", type="volume")
        ],
        mount_tmp_dir=False,
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={"DATA_DIR": "/app/data"}
    )
