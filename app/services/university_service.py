from app.models.universitie import University
from app.repositories.university_repository import UniversityRepository


class UniversityService:
    def __init__(self, repository: UniversityRepository):
        self.repository = repository

    async def get_all_universities(self) -> list[University]:
        return await self.repository.get_all_universities()

    async def get_university_by_id(self, university_id) -> University | None:
        return await self.repository.get_university_by_id(university_id)

    async def create_university(self, name) -> University:
        return await self.repository.create_university(name)
