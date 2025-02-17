from app.controller.metrics import Controller

from fastapi import APIRouter

router = APIRouter(
    prefix="/metrics",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/report1")
def report1():
    return Controller.report("report1")

@router.post("/report2")
def report2():
    return Controller.report("report2")