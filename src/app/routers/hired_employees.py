from app.controller.hired_employees import Controller
from app.models.hired_employees import HiredEmployees

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/hired_employees",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(data: HiredEmployees, request: Request):
    return Controller(request).insert_rows(data)