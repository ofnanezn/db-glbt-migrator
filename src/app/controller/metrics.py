from app.service.metrics import Service

from fastapi import HTTPException, Request
from abc import ABC
import json

class Controller(ABC):
    def report(report_number):            
        try:
            return Service.report(report_number)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating {report_number}: {e}")