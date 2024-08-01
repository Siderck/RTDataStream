from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

TAGS = ['PythonDataFlow']
DAG_ID = "MI_PRIMER_DAG"
DAG_DESCRIPTION =  """MI PRIMER DAG PARA EL CURSO DE AIRFLOW"""
DAG_SCHEDULE = "0 9 * * *"

default_args = {
    "start_date": datetime(2024, 4, 24)
}

retries = 4
retry_delay = timedelta(minutes=5)

def execute_tasks ():
    print("Hola Mundo")

dag = DAG(
    dag_id=DAG_ID,
    description=DAG_DESCRIPTION,
    catchup=False,
    schedule_interval=DAG_SCHEDULE,
    max_active_runs=1,
    dagrun_timeout=200000,
    default_args=default_args,
    tags=TAGS
)

with dag as dag:
    start_task = EmptyOperator(
        task_id="inicia_proceso"
    )

    end_task = EmptyOperator(
        task_id="finaliza_proceso"
    )

    first_task = PythonOperator(
        task_id="first_task",
        python_callable=execute_tasks,
        retries=retries,
        retry_delay=retry_delay
    )