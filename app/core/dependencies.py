from fastapi import Depends
from functools import lru_cache
from app.services.ai_service import AIService
from app.core.config import settings

@lru_cache()
def get_ai_service() -> AIService:
    return AIService()

@lru_cache()
def get_settings():
    return settings
