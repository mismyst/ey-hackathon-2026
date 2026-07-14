from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sheldra_env: str = "development"
    sheldra_cors_origins: str = "http://localhost:3000"
    redis_url: str = "redis://localhost:6379/0"
    kafka_broker_url: str = "localhost:29092"

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.sheldra_cors_origins.split(",")]


@lru_cache
def get_settings() -> Settings:
    return Settings()
