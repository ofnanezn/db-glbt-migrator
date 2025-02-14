from fastapi import HTTPException, Request
from abc import ABC
import json

class Controller(ABC):
    def __init__(self, request: Request):
        self.request = request

    def insert_rows(self, body):
        body = json.loads(body.json())
        
        if not len(body["rows"]):
            raise HTTPException(status_code=400, detail="Rows should not be empty.")
            
        try:
            return {
                "message": "Rows inserted successfully"
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error inserting rows: {e}")
