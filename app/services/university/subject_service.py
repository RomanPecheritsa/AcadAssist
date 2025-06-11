from app.models.university import Subject
from app.repositories.university_repository import SemesterRepository, SubjectRepository


class SubjectService:
    def __init__(self, repository: SubjectRepository, semester_repository: SemesterRepository):
        self.repository = repository
        self.semester_repository = semester_repository

    async def _validate_semester_exists(self, semester_id: int):
        semester = await self.semester_repository.get_by_id(semester_id)
        if not semester:
            raise ValueError(f"Semester with id={semester_id} does not exist.")

    async def create_subject(self, data: dict) -> Subject:
        await self._validate_semester_exists(data["semester_id"])
        return await self.repository.create(data)

    async def update_subject(self, subject: Subject, data: dict) -> Subject:
        semester_id = data.get("semester_id", subject.semester_id)
        await self._validate_semester_exists(semester_id)
        return await self.repository.update(subject, data)

    async def get_all_subjects(self) -> list[Subject]:
        return await self.repository.get_all()

    async def get_subject_by_id(self, subject_id: int) -> Subject | None:
        return await self.repository.get_by_id(subject_id)

    async def delete_subject(self, subject: Subject) -> None:
        await self.repository.delete(subject)
