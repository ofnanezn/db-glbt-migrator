from app.controller.departments import Controller
from app.models.departments import Departments

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/departments",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(data: Departments, request: Request):
    return Controller(request).insert_rows(data)