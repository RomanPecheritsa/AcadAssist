from fastapi import FastAPI

from app.core.config import get_settings
from app.middleware import log_requests_middleware
from app.routes.university.specialty_routes import router as specialty_router
from app.routes.university.university_routes import router as university_router

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)
app.middleware("http")(log_requests_middleware)
app.include_router(university_router)
app.include_router(specialty_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to AcadAssist API"}
