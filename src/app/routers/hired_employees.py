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
    return Controller.insert_rows(data)

@router.post("/backup")
def backup():
    return Controller.backup()

@router.post("/restore")
def restore():
    return Controller.restore()