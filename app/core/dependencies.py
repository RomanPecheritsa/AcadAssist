from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.repositories.university_repository import (
    SemesterRepository,
    SpecialityRepository,
    SubjectRepository,
    UniversityRepository,
    WorkRepository,
)
from app.services.university import (
    SemesterService,
    SpecialityService,
    SubjectService,
    UniversityService,
    WorkService,
)


# ==== University Dependencies ====
def get_university_repository(session: AsyncSession = Depends(get_db)) -> UniversityRepository:
    return UniversityRepository(session)


def get_university_service(repo: UniversityRepository = Depends(get_university_repository)) -> UniversityService:
    return UniversityService(repo)


# ==== Speciality Dependencies ====
def get_speciality_repository(session: AsyncSession = Depends(get_db)) -> SpecialityRepository:
    return SpecialityRepository(session)


def get_speciality_service(
    repo: SpecialityRepository = Depends(get_speciality_repository),
    university_repo: UniversityRepository = Depends(get_university_repository),
) -> SpecialityService:
    return SpecialityService(repo, university_repo)


# ==== Semester Dependencies ====
def get_semester_repository(session: AsyncSession = Depends(get_db)) -> SemesterRepository:
    return SemesterRepository(session)


def get_semester_service(
    repo: SemesterRepository = Depends(get_semester_repository),
    speciality_repo: SpecialityRepository = Depends(get_speciality_repository),
) -> SemesterService:
    return SemesterService(repo, speciality_repo)


# ==== Subject Dependencies ====
def get_subject_repository(session: AsyncSession = Depends(get_db)) -> SubjectRepository:
    return SubjectRepository(session)


def get_subject_service(
    repo: SubjectRepository = Depends(get_subject_repository),
    semester_repo: SemesterRepository = Depends(get_semester_repository),
) -> SubjectService:
    return SubjectService(repo, semester_repo)


# ==== Work Dependencies ====
def get_work_repository(session: AsyncSession = Depends(get_db)) -> WorkRepository:
    return WorkRepository(session)


def get_work_service(
    repo: WorkRepository = Depends(get_work_repository),
    subject_repo: SubjectRepository = Depends(get_subject_repository),
) -> WorkService:
    return WorkService(repo, subject_repo)
