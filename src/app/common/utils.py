from google.cloud import bigquery
from datetime import datetime
import pandas as pd
import os


# Config per tables
tables = {
    "departments": {
        "table_name": "dm_departments",
        "clusters": ["DEPARTMENT"], 
    },
    "jobs": {
        "table_name": "dm_jobs",
        "clusters": ["JOB"], 
    },
    "hired_employees": {
        "table_name": "ft_hired_employees",
        "clusters": ["NAME"],
        "partition": {
            "field": "DATETIME",
            "type": "DAY",
        } 
    },
}


def df_to_bq(rows, table):
    try:
        now = datetime.now()
        table_name = f"{tables[table]['table_name']}_{int(now.timestamp())}"

        table_id = f"{os.getenv('DATASET_ID')}_stg.{table_name}"

        df = pd.DataFrame(rows)
        df.to_gbq(table_id, project_id=os.getenv("PROJECT_ID"), if_exists="replace")

        return df, table_name
    except Exception as e:
        raise Exception(f"Error while pushing data into BigQuery staging. {e}")


def merge_staging_into_target(table_type, stg_table):
    try:
        client = bigquery.Client(project=os.getenv("PROJECT_ID"))

        with open(f"sql/{table_type}.sql", "r") as f:
            query = f.read()

        query = query.replace("<staging_table>", stg_table)
        job = client.query(query=query)
        return job.result()
    except Exception as e:
        raise Exception(f"Error while merging data into target table. {e}")


def backup_into_gcs(table_type):
    try:
        bucket_path = f"gs://{os.getenv('BUCKET_NAME')}/backup/{table_type}.avro"
        table_id = f"{os.getenv('DATASET_ID')}_tgt.{tables[table_type]['table_name']}"

        client = bigquery.Client(project=os.getenv("PROJECT_ID"))

        job_config = bigquery.ExtractJobConfig()
        job_config.destination_format = bigquery.job.DestinationFormat.AVRO
        job_config.compression = bigquery.job.Compression.SNAPPY

        extract_job = client.extract_table(
            table_id,
            bucket_path,
            location="us-central1",
            job_config=job_config,
        )   

        return extract_job.result()
    except Exception as e:
        raise Exception(f"Error while creating backup. {e}")


def restore_from_gcs(table_type):
    try:
        bucket_path = f"gs://{os.getenv('BUCKET_NAME')}/backup/{table_type}.avro"
        table_id = f"{os.getenv('DATASET_ID')}_tgt.{tables[table_type]['table_name']}"

        client = bigquery.Client(project=os.getenv("PROJECT_ID"))

        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.job.DestinationFormat.AVRO
        job_config.create_disposition = "CREATE_IF_NEEDED"
        job_config.clustering_fields = tables[table_type]["clusters"]

        import_job = client.load_table_from_uri(
            bucket_path,
            table_id,
            location="us-central1",
            job_config=job_config,
        )   

        return import_job.result()
    except Exception as e:
        raise Exception(f"Error while restoring table. {e}")