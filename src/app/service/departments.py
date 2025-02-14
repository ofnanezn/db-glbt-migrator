from app.common.utils import df_to_bq, merge_staging_into_target


class Service():
    def insert_rows(data):
        try:
            df, table_name_stg = df_to_bq(data, "departments")
            merge_staging_into_target("departments", table_name_stg)
            return {
                "message": "Rows inserted successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
        