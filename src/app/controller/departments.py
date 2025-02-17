from app.service.departments import Service

from fastapi import HTTPException
from abc import ABC
import json

class Controller(ABC):
    def insert_rows(body):
        body = json.loads(body.json())
        
        if not len(body["rows"]):
            raise HTTPException(status_code=400, detail="Rows should not be empty.")
            
        try:
            return Service.insert_rows(body["rows"])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inserting rows: {e}")

    def backup():            
        try:
            return Service.backup()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in backup process: {e}")

    def restore():            
        try:
            return Service.restore()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in restore process: {e}")
