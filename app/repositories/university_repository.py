from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.universitie import University


class UniversityRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_universities(self) -> list[University]:
        result = await self.session.execute(select(University))
        return result.scalars().all()

    async def get_university_by_id(self, university_id: int) -> University | None:
        result = await self.session.execute(select(University).where(University.id == university_id))
        return result.scalar_one_or_none()

    async def create_university(self, name: str) -> University:
        university = University(name=name)
        self.session.add(university)
        await self.session.commit()
        await self.session.refresh(university)
        return university
