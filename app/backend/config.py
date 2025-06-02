from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEVELOPMENT = "dev"
    TESTING = "test"
    PRODUCTION = "prod"


class Settings(BaseSettings):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT

    APP_HOST: str
    APP_PORT: int
    DEBUG: bool

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file_encoding = "utf-8"

    @classmethod
    def load_config(cls, environment: Environment = Environment.DEVELOPMENT):
        return cls(_env_file=f".env.{environment.value}")


@lru_cache
def get_settings() -> Settings:
    from os import getenv

    env = getenv("ENVIRONMENT", "dev")
    return Settings.load_config(Environment(env))
