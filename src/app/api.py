from app.routers import departments, jobs, hired_employees, metrics

from fastapi import FastAPI

app = FastAPI()
app.include_router(departments.router)
app.include_router(jobs.router)
app.include_router(hired_employees.router)
app.include_router(metrics.router)

@app.get("/ping")
def ping():
    return "pong"