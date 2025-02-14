from app.common.utils import df_to_bq


class Service():
    def insert_rows(data):
        try:
            df, table_name = df_to_bq(data, "jobs")
            merge_staging_into_target("jobs", table_name_stg)
            return {
                "message": "Rows inserted successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
        