from abc import ABC, abstractmethod
from typing import Dict, Any
import aiohttp
import os

class AIProvider(ABC):
    @abstractmethod
    async def execute_command(self, command: str, params: str) -> Dict[str, Any]:
        pass

class AiderProvider(AIProvider):
    def __init__(self, aider_path: str):
        self.aider_path = aider_path

    async def execute_command(self, command: str, params: str) -> Dict[str, Any]:
        try:
            from app.helpers import execute_aider_command
            result = await execute_aider_command(command, params)
            return {"success": True, "data": result}
        except Exception as e:
            return {"success": False, "error": str(e)}

class AIService:
    def __init__(self):
        self.providers = {
            "aider": AiderProvider(os.getenv("AIDER_PATH", "/usr/local/bin/aider")),
        }

    async def execute(self, provider: str, command: str, params: str) -> Dict[str, Any]:
        if provider not in self.providers:
            raise ValueError(f"Unknown AI provider: {provider}")
        return await self.providers[provider].execute_command(command, params)
