from app.models.university import University
from app.repositories.university_repository import UniversityRepository


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
