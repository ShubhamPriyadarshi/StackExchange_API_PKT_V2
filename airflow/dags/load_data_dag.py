from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import subprocess

def run_dbt_command(folder, model_tag):
    command = f"dbt run --models tag:{model_tag}"
    dbt_path = f"../{folder}/"
    subprocess.check_call(command, shell=True, cwd=dbt_path)

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 2),
    'email': ['your-email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stackexchange_elt',
    default_args=default_args,
    description='An ELT pipeline full ingest pipeline from stackexchange api to Snowflake',
    schedule_interval=timedelta(days=1),
)

start_operator = EmptyOperator(task_id='Begin_execution',  dag=dag)

extract_load_task = BashOperator(
    task_id='api_extract_load',
    bash_command="curl http://localhost:8000/api/v1/load-data",
    dag=dag,
)


dbt_curation_task = PythonOperator(
    task_id='dbt_curation',
    python_callable=run_dbt_command,
    op_args=["dbt_se", "curation"],
    dag=dag,
)

dbt_calculation_task = PythonOperator(
    task_id='dbt_calculation',
    python_callable=run_dbt_command,
    op_args=["dbt_se", "calculation"],
    dag=dag,
)

dbt_consumption_task = PythonOperator(
    task_id='dbt_consumption',
    python_callable=run_dbt_command,
    op_args=["dbt_se", "consumption"],
    dag=dag,
)


end_operator = EmptyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> extract_load_task >> dbt_curation_task >> dbt_calculation_task >> dbt_consumption_task >> end_operator

