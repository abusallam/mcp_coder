from app.core.env_model import env
from app.core.exceptions import AIProviderError
from typing import Dict, Any
import asyncio

class AiderService:
    """Aider-based MCP service for code operations"""
    
    def __init__(self):
        self.config = {
            "path": env.AIDER_PATH,
            "model": env.AIDER_MODEL,
            "temperature": env.AIDER_TEMPERATURE,
            "max_tokens": env.AIDER_MAX_TOKENS,
            "api_key": env.AIDER_API_KEY,
            "user": env.AIDER_USER,
            "password": env.AIDER_PASSWORD,
            "permissions": env.AIDER_PERMISSIONS
        }
        self._authenticate()

    def _authenticate(self):
        """Authenticate Aider user"""
        cmd = [
            self.config["path"],
            "--auth",
            "--user", self.config["user"],
            "--password", self.config["password"]
        ]
        # Authentication logic here

    async def execute(self, command: str, params: str) -> Dict[str, Any]:
        """Execute Aider command"""
        cmd = [
            self.config["path"],
            "--model", self.config["model"],
            "--temperature", str(self.config["temperature"]),
            command,
            params
        ]
        
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                raise AIProviderError(f"Aider command failed: {stderr.decode()}")
                
            return {
                "success": True,
                "data": stdout.decode(),
                "command": command
            }
        except Exception as e:
            raise AIProviderError(f"Aider execution failed: {str(e)}")
