from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago


with DAG(
    dag_id="fetch_weather_dag",
    schedule_interval="@hourly",
    start_date=days_ago(1),
    catchup=False,
    tags=["weather-analysis"],
) as dag:

    fetch_weather = DockerOperator(
        task_id="fetch_weather",
        image="weather-analysis:latest",
        api_version="auto",
        auto_remove=True,
        command="python /app/app/run_fetch.py",
        mount_tmp_dir=False,
        docker_url="unix://var/run/docker.sock",
        network_mode="etl_net",
    )

    get_anomalies = DockerOperator(
        task_id="get_anomalies",
        image="weather-analysis:latest",
        api_version="auto",
        auto_remove=True,
        command="python /app/app/run_anomalies_check.py",
        mount_tmp_dir=False,
        docker_url="unix://var/run/docker.sock",
        network_mode="etl_net",
    )

    fetch_weather >> get_anomalies
