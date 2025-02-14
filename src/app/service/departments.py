from app.common.utils import df_to_bq

from datetime import datetime
import pandas as pd
import os


class Service():
    def insert_rows(data):
        try:
            df = df_to_bq(data, "departments")

            return {
                "message": "Rows inserted successfully.",
                "count": len(df),
            }
        except Exception as e:
            raise Exception(str(e))
        