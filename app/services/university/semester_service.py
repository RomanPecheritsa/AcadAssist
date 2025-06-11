from app.models.university import Semester, Speciality
from app.repositories.university_repository import SemesterRepository, SpecialityRepository


class SemesterService:
    def __init__(self, repository: SemesterRepository, speciality_repository: SpecialityRepository):
        self.repository = repository
        self.speciality_repository = speciality_repository

    async def _validate_semester_number(self, speciality_id: int, number: int):
        speciality: Speciality | None = await self.speciality_repository.get_by_id(speciality_id)
        if not speciality:
            raise ValueError("Speciality not found")
        if number > speciality.semesters_count:
            raise ValueError(f"Semester number {number} exceeds max allowed: {speciality.semesters_count}")

    async def create_semester(self, data: dict) -> Semester:
        speciality_id = data["speciality_id"]
        semester_number = data["number"]

        await self._validate_semester_number(speciality_id, semester_number)

        return await self.repository.create(data)

    async def update_semester(self, semester: Semester, data: dict) -> Semester:
        new_number = data.get("number", semester.number)
        new_speciality_id = data.get("speciality_id", semester.speciality_id)

        await self._validate_semester_number(new_speciality_id, new_number)

        return await self.repository.update(semester, data)

    async def get_all_semesters(self):
        return await self.repository.get_all()

    async def get_semester_by_id(self, semester_id: int):
        return await self.repository.get_by_id(semester_id)

    async def delete_semester(self, semester: Semester):
        await self.repository.delete(semester)
