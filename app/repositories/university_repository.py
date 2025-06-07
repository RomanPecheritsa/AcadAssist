from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.universitie import University


class UniversityRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_universities(self) -> list[University]:
        result = await self.session.execute(select(University))
        return result.scalars().all()
