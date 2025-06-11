from app.models.university import Specialty, University
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
