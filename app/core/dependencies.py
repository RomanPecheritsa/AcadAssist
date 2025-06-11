from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.repositories.university_repository import SemesterRepository, SpecialtyRepository, UniversityRepository
from app.services.university_service import SemesterService, SpecialtyService, UniversityService


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


# ==== Semester Dependencies ====
def get_semester_repository(session: AsyncSession = Depends(get_db)) -> SemesterRepository:
    return SemesterRepository(session)


def get_semester_service(
    repo: SemesterRepository = Depends(get_semester_repository),
    specialty_repo: SpecialtyRepository = Depends(get_specialty_repository),
) -> SemesterService:
    return SemesterService(repo, specialty_repo)
