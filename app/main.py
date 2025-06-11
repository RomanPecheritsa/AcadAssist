from fastapi import FastAPI

from app.core.config import get_settings
from app.middleware import log_requests_middleware
from app.routers.university import semester_router, speciality_router, subject_router, university_router, work_router

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)
app.middleware("http")(log_requests_middleware)
app.include_router(university_router)
app.include_router(speciality_router)
app.include_router(semester_router)
app.include_router(subject_router)
app.include_router(work_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to AcadAssist API"}
