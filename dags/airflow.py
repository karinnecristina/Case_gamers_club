import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from pipeline import Pipeline


pipeline = Pipeline(["tb_players","tb_players_medalha","tb_lobby_stats_player"])

DEFAULT_ARGS = {
    'owner': 'Airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0)
}

dag = DAG('etl', 
          default_args=DEFAULT_ARGS,
           schedule_interval="@daily"
        )

buckets_task = PythonOperator(
    task_id="criar_buckets",
    python_callable=pipeline.create_buckets,
    do_xcom_push=False,
    dag=dag,
)

extract_task = PythonOperator(
    task_id="extrair_dados_e_salvar_dados",
    python_callable=pipeline.extract_data,
    do_xcom_push=False,
    dag=dag,
)

load_task = PythonOperator(
    task_id="transformar_e_carregar_dados",
    email_on_failure=True,
    python_callable=pipeline.transform_data,
    do_xcom_push=False,
    dag=dag,
)

buckets_task >> extract_task >> load_task