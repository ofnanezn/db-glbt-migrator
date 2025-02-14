from pydantic import BaseModel
from typing import List

class HiredEmployee(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

class HiredEmployees(BaseModel):
    rows: List[HiredEmployee]