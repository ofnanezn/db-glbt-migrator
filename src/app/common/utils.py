from google.cloud import bigquery
from datetime import datetime
import pandas as pd
import os

# Config per tables
tables = {
    "departments": {
        "table_name": "dm_departments", 
    },
    "jobs": {
        "table_name": "dm_jobs", 
    },
    "hired_employees": {
        "table_name": "ft_hired_employees", 
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
        print(query)
        job = client.query(query=query)
        return job.result()
    except Exception as e:
        raise Exception(f"Error while merging data into target table. {e}")