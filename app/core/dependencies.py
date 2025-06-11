from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.repositories.university_repository import SpecialtyRepository, UniversityRepository
from app.services.university_service import SpecialtyService, UniversityService


# ==== University Dependencies ====
def get_university_repository(session: AsyncSession = Depends(get_db)) -> UniversityRepository:
    return UniversityRepository(session)


def get_university_service(repo: UniversityRepository = Depends(get_university_repository)) -> UniversityService:
    return UniversityService(repo)


# ==== Specialty Dependencies ====
def get_specialty_repository(session: AsyncSession = Depends(get_db)) -> SpecialtyRepository:
    return SpecialtyRepository(session)


def get_specialty_service(repo: SpecialtyRepository = Depends(get_specialty_repository)) -> SpecialtyService:
    return SpecialtyService(repo)
