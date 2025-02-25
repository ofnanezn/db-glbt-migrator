from app.common.utils import (
    df_to_bq, 
    merge_staging_into_target, 
    backup_into_gcs, 
    restore_from_gcs
)


class Service():
    def insert_rows(data):
        try:
            df, table_name_stg = df_to_bq(data, "departments")
            merge_staging_into_target("departments", table_name_stg)
            return {
                "message": "Rows inserted/updated successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
    
    def backup():
        try:
            backup_into_gcs("departments")
            return {
                "message": "Table departments backup created successfully.",
            }
        except Exception as e:
            raise Exception(str(e))

    def restore():
        try:
            restore_from_gcs("departments")
            return {
                "message": "Table departments restored successfully.",
            }
        except Exception as e:
            raise Exception(str(e))