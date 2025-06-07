from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db import get_db
from app.repositories.university_repository import UniversityRepository
from app.services.university_service import UniversityService


# ==== University Dependencies ====
def get_university_repository(session: AsyncSession = Depends(get_db)) -> UniversityRepository:
    return UniversityRepository(session)


def get_university_service(repo: UniversityRepository = Depends(get_university_repository)) -> UniversityService:
    return UniversityService(repo)
