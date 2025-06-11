from typing import Any, Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import DeclarativeBase

from app.models.university import Semester, Speciality, Subject, University, Work

ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get_all(self) -> list[ModelType]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def get_by_id(self, id: int) -> ModelType | None:
        result = await self.session.execute(select(self.model).where(self.model.id == id))
        return result.scalar_one_or_none()

    async def create(self, obj_in: dict[str, Any]) -> ModelType:
        db_obj = self.model(**obj_in)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def update(self, db_obj: ModelType, obj_in: dict[str, Any]) -> ModelType:
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, db_obj: ModelType) -> None:
        await self.session.delete(db_obj)
        await self.session.commit()


class UniversityRepository(BaseRepository[University]):
    def __init__(self, session: AsyncSession):
        super().__init__(University, session)


class SpecialityRepository(BaseRepository[Speciality]):
    def __init__(self, session: AsyncSession):
        super().__init__(Speciality, session)


class SemesterRepository(BaseRepository[Semester]):
    def __init__(self, session: AsyncSession):
        super().__init__(Semester, session)


class SubjectRepository(BaseRepository[Subject]):
    def __init__(self, session: AsyncSession):
        super().__init__(Subject, session)


class WorkRepository(BaseRepository[Work]):
    def __init__(self, session: AsyncSession):
        super().__init__(Work, session)
