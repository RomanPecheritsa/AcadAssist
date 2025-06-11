from app.models.university import Semester, Specialty, University
from app.repositories.university_repository import SpecialtyRepository, UniversityRepository


class UniversityService:
    def __init__(self, repository: UniversityRepository):
        self.repository = repository

    async def get_all_universities(self) -> list[University]:
        return await self.repository.get_all()

    async def get_university_by_id(self, university_id: int) -> University | None:
        return await self.repository.get_by_id(university_id)

    async def create_university(self, name: str) -> University:
        return await self.repository.create({"name": name})

    async def update_university(self, university: University, name: str) -> University:
        return await self.repository.update(university, {"name": name})

    async def delete_university(self, university: University) -> None:
        await self.repository.delete(university)


class SpecialtyService:
    def __init__(self, repository: SpecialtyRepository):
        self.repository = repository

    async def get_all_specialties(self) -> list[Specialty]:
        return await self.repository.get_all()

    async def get_specialty_by_id(self, specialty_id: int) -> Specialty | None:
        return await self.repository.get_by_id(specialty_id)

    async def create_specialty(self, data: dict) -> Specialty:
        return await self.repository.create(data)

    async def update_specialty(self, specialty: Specialty, data: dict) -> Specialty:
        return await self.repository.update(specialty, data)

    async def delete_specialty(self, specialty: Specialty) -> None:
        await self.repository.delete(specialty)


class SemesterService:
    def __init__(self, repository, specialty_repository: SpecialtyRepository):
        self.repository = repository
        self.specialty_repository = specialty_repository

    async def _validate_semester_number(self, specialty_id: int, number: int):
        specialty: Specialty | None = await self.specialty_repository.get_by_id(specialty_id)
        if not specialty:
            raise ValueError("Specialty not found")
        if number > specialty.semesters_count:
            raise ValueError(f"Semester number {number} exceeds max allowed: {specialty.semesters_count}")

    async def create_semester(self, data: dict) -> Semester:
        specialty_id = data["specialty_id"]
        semester_number = data["number"]

        await self._validate_semester_number(specialty_id, semester_number)

        return await self.repository.create(data)

    async def update_semester(self, semester: Semester, data: dict) -> Semester:
        new_number = data.get("number", semester.number)
        new_specialty_id = data.get("specialty_id", semester.specialty_id)

        await self._validate_semester_number(new_specialty_id, new_number)

        return await self.repository.update(semester, data)

    async def get_all_semesters(self):
        return await self.repository.get_all()

    async def get_semester_by_id(self, semester_id: int):
        return await self.repository.get_by_id(semester_id)

    async def delete_semester(self, semester: Semester):
        await self.repository.delete(semester)
