from fastapi import FastAPI

from app.backend.config import get_settings
from app.middleware import log_requests_middleware

settings = get_settings()

app = FastAPI(debug=settings.DEBUG)
app.middleware("http")(log_requests_middleware)
