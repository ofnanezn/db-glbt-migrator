from app.controller.departments import Controller
from app.models.departments import Departments

from fastapi import APIRouter

router = APIRouter(
    prefix="/departments",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(data: Departments):
    return Controller.insert_rows(data)

@router.post("/backup")
def backup():
    return Controller.backup()

@router.post("/restore")
def restore():
    return Controller.restore()