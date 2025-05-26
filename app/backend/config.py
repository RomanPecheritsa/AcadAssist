from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    user: str
    password: str
    database: str
    host: str
    port: int

    @property
    def async_dsn(self) -> str:
        """Возвращает DSN для асинхронного подключения (asyncpg)"""
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class AppConfig:
    host: str
    port: int
    debug: bool


@dataclass
class Config:
    app: AppConfig
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        app=AppConfig(
            host=env.str("APP_HOST", "0.0.0.0"), port=env.int("APP_PORT", 8000), debug=env.bool("DEBUG", False)
        ),
        db=DatabaseConfig(
            user=env.str("POSTGRES_USER"),
            password=env.str("POSTGRES_PASSWORD"),
            database=env.str("POSTGRES_DB"),
            host=env.str("POSTGRES_HOST", "localhost"),
            port=env.int("POSTGRES_PORT", 5432),
        ),
    )


settings = load_config()
