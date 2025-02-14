from datetime import datetime
import os

# Config per tables
tables = {
    "departments": {
        "table_name": "dm_departments", 
    },
    "jobs": {
        "table_name": "dm_jobs", 
    },
    "departments": {
        "table_name": "ft_hired_employees", 
    },
}

def df_to_bq(rows, table):
    now = datetime.now()
    table_name = f"{tables[table]['table_name']}_{int(now.timestamp())}"

    table_id = f"{os.getenv('DATASET_ID')}_stg.{table_name}"

    df = pd.DataFrame(data)
    df.to_gbq(table_id, project_id=os.getenv("PROJECT_ID"), if_exists="replace")

    return df