from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_API_ID: str
    TELEGRAM_API_HASH: str

    class Config:
        env_file = ".env"

settings = Settings()