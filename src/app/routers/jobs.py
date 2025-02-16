from app.controller.jobs import Controller
from app.models.jobs import Jobs

from fastapi import APIRouter

router = APIRouter(
    prefix="/jobs",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(data: Jobs):
    return Controller.insert_rows(data)

@router.post("/backup")
def backup():
    return Controller.backup()