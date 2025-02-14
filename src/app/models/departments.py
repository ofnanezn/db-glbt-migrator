from pydantic import BaseModel
from typing import List

class Department(BaseModel):
    id: int
    department: str

class Departments(BaseModel):
    rows: List[Department]