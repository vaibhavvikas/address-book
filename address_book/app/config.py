from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLITE_DATABASE: str
    LOG_PATH: str

    class Config:
        env_file = "./.env"


settings = Settings()  # type: ignore
