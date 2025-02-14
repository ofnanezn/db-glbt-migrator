from pydantic import BaseModel
from typing import List

class Job(BaseModel):
    id: int
    job: str

class Jobs(BaseModel):
    rows: List[Job]