from app.routers import departments, jobs, hired_employees

from fastapi import FastAPI

app = FastAPI()
app.include_router(departments.router)
app.include_router(jobs.router)
app.include_router(hired_employees.router)

@app.get("/ping")
def ping():
    return "pong"