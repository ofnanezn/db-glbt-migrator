from app.common.utils import df_to_bq, merge_staging_into_target, backup_into_gcs


class Service():
    def insert_rows(data):
        try:
            df, table_name_stg = df_to_bq(data, "hired_employees")
            merge_staging_into_target("hired_employees", table_name_stg)
            return {
                "message": "Rows inserted successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
        
    def backup():
        try:
            backup_into_gcs("hired_employees")
            return {
                "message": "Table hired_employees backup created successfully.",
            }
        except Exception as e:
            raise Exception(str(e))