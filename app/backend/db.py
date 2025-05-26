from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.backend.config import settings

engine = create_async_engine(settings.db.async_dsn)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
