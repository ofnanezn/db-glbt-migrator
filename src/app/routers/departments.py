from fastapi import APIRouter, Request

router = APIRouter(
    prefix="/departments",
    tags=["migrator"],
    responses={
        404: {"description": "Not found"}
    }
)

@router.post("/insert")
def insert_rows(request: Request):
    return "Inserting departments table..."