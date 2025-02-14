from app.models.jobs import Jobs

from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/jobs",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(data: Jobs, request: Request):
    return "Inserting jobs table..."