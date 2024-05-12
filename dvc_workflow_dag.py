from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import data_processing

# Define the DAG
data_extraction_dag = DAG('data_extraction_dag', description='Automated Data Extraction and DVC Workflow',
                          schedule_interval='@daily',
                          start_date=datetime(2024, 9, 25), catchup=False)

# Define the PythonOperator task to run data processing
def run_data_processing_task():
    data_processing.main()

data_processing_task = PythonOperator(task_id='run_data_processing_task',
                                     python_callable=run_data_processing_task,
                                     dag=data_extraction_dag)
