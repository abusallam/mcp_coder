import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    AIDER_PATH: str = "/usr/local/bin/aider"
    CORS_ORIGINS: List[str] = ["https://mcp-coder.consulting.sa", "http://localhost:3000", "http://localhost:8000"]
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
