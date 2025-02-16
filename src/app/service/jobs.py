from app.common.utils import df_to_bq, merge_staging_into_target, backup_into_gcs


class Service():
    def insert_rows(data):
        try:
            df, table_name_stg = df_to_bq(data, "jobs")
            merge_staging_into_target("jobs", table_name_stg)
            return {
                "message": "Rows inserted successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
        
    def backup():
        try:
            backup_into_gcs("jobs")
            return {
                "message": "Table jobs backup created successfully.",
            }
        except Exception as e:
            raise Exception(str(e))