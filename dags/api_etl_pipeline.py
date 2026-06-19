from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define where your project files live on the Windows mount
PROJECT_DIR = "/mnt/c/Users/user/Desktop/Data Engineering Projects/Project 5/Warehouse"
# Point to the python executable inside your sandbox environment
PYTHON_ENV = "/home/sharugesh/airflow_project/sandbox/bin/python"

default_args = {
    'owner': 'sharugesh',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'warehouse_etl_pipeline',
    default_args=default_args,
    description='Orchestrates the Extract, Transform, and Load scripts for the Warehouse project',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id='extract_data',
        bash_command=f'cd "{PROJECT_DIR}" && {PYTHON_ENV} src/extract.py',
    )

    transform_task = BashOperator(
        task_id='transform_data',
        bash_command=f'cd "{PROJECT_DIR}" && {PYTHON_ENV} src/transform.py',
    )

    load_task = BashOperator(
        task_id='load_data',
        bash_command=f'cd "{PROJECT_DIR}" && {PYTHON_ENV} src/load.py',
    )

    # Set the sequence: Extract -> Transform -> Load
    extract_task >> transform_task >> load_task