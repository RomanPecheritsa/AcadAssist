from app.models.universitie import University
from app.repositories.university_repository import UniversityRepository


class UniversityService:
    def __init__(self, repository: UniversityRepository):
        self.repository = repository

    async def get_all_universities(self) -> list[University]:
        return await self.repository.get_all_universities()
