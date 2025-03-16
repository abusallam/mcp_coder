from typing import List
from app.core.env_model import env

class Settings:
    API_V1_STR: str = env.API_V1_STR
    PROJECT_NAME: str = env.PROJECT_NAME
    CORS_ORIGINS: List[str] = env.CORS_ORIGINS
    DATABASE_URL: str = env.DATABASE_URL
    API_KEY: str = env.API_KEY
    DEBUG: bool = env.DEBUG

settings = Settings()
