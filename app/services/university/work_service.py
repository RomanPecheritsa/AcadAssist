from app.models.university import Work
from app.repositories.university_repository import SubjectRepository, WorkRepository


class WorkService:
    def __init__(self, repository: WorkRepository, subject_repository: SubjectRepository):
        self.repository = repository
        self.subject_repository = subject_repository

    async def _validate_subject_exists(self, subject_id: int):
        subject = await self.subject_repository.get_by_id(subject_id)
        if not subject:
            raise ValueError(f"Subject with id={subject_id} does not exist.")

    async def create_work(self, data: dict) -> Work:
        await self._validate_subject_exists(data["subject_id"])
        return await self.repository.create(data)

    async def update_work(self, work: Work, data: dict) -> Work:
        subject_id = data.get("subject_id", work.subject_id)
        await self._validate_subject_exists(subject_id)
        return await self.repository.update(work, data)

    async def get_all_works(self) -> list[Work]:
        return await self.repository.get_all()

    async def get_work_by_id(self, work_id: int) -> Work | None:
        return await self.repository.get_by_id(work_id)

    async def delete_work(self, work: Work) -> None:
        await self.repository.delete(work)
