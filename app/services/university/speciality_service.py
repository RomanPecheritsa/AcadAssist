from app.models.university import Speciality
from app.repositories.university_repository import SpecialityRepository, UniversityRepository


class SpecialityService:
    def __init__(self, repository: SpecialityRepository, university_repository: UniversityRepository):
        self.repository = repository
        self.university_repository = university_repository

    async def _validate_university_exists(self, university_id: int):
        university = await self.university_repository.get_by_id(university_id)
        if not university:
            raise ValueError(f"University with id={university_id} does not exist.")

    async def create_speciality(self, data: dict) -> Speciality:
        await self._validate_university_exists(data["university_id"])
        return await self.repository.create(data)

    async def update_speciality(self, speciality: Speciality, data: dict) -> Speciality:
        university_id = data.get("university_id", speciality.university_id)
        await self._validate_university_exists(university_id)
        return await self.repository.update(speciality, data)

    async def get_all_specialties(self):
        return await self.repository.get_all()

    async def get_speciality_by_id(self, speciality_id: int):
        return await self.repository.get_by_id(speciality_id)

    async def delete_speciality(self, speciality: Speciality):
        await self.repository.delete(speciality)
