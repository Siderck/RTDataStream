from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Siderck',
    'start_date': datetime(2024, 7, 31) 
}

#Get the data from API, formatting it to JSON and then gets the first index of results
def get_data():
    import requests
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]    
    return res

def format_data(res):
    data = {}
    data['first_name']


def stream_data():
    import json



with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data();
