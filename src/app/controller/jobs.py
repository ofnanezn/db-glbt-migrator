from app.service.jobs import Service

from fastapi import HTTPException, Request
from abc import ABC
import json

class Controller(ABC):
    def insert_rows(self, body):
        body = json.loads(body.json())
        
        if not len(body["rows"]):
            raise HTTPException(status_code=400, detail="Rows should not be empty.")
            
        try:
            return Service.insert_rows(body["rows"])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inserting rows: {e}")
