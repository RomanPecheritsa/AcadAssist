from fastapi import FastAPI

from app.backend.config import get_settings

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)
