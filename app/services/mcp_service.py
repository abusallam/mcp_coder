from typing import Dict, Any, List
from app.core.exceptions import MCPError
from app.models.agent import Agent
from app.services.ai_service import AiderService
from app.core.mcp import MCPCommand, MCPCapability
from app.services.mcp_engine import MCPEngine

class MCPService:
    """Core MCP Server service"""
    
    def __init__(self):
        self.aider = AiderService()
        self.engine = MCPEngine()
        self._load_capabilities()
        self._init_cache()

    async def _init_memory_cache(self):
        """Initialize in-memory cache for faster responses"""
        self.command_cache = {}
        self.result_cache = {}

    def _load_capabilities(self):
        """Load core MCP capabilities"""
        self.capabilities = {
            MCPCapability.CODE_ANALYSIS: [MCPCommand.ANALYZE],
            MCPCapability.CODE_IMPROVEMENT: [MCPCommand.IMPROVE],
            MCPCapability.CODE_GENERATION: [MCPCommand.GENERATE]
        }
        self._init_commands()

    def _init_commands(self):
        """Initialize core command handlers"""
        self.commands = {
            MCPCommand.ANALYZE: self._analyze_code,
            MCPCommand.IMPROVE: self._improve_code,
            MCPCommand.GENERATE: self._generate_code
        }

    async def _analyze_code(self, code: str) -> Dict[str, Any]:
        return await self.aider.execute("/analyze", code)

    async def _improve_code(self, code: str) -> Dict[str, Any]:
        return await self.aider.execute("/improve", code)

    async def _explain_code(self, code: str) -> Dict[str, Any]:
        return await self.aider.execute("/explain", code)

    async def _generate_code(self, prompt: str) -> Dict[str, Any]:
        return await self.aider.execute("/generate", prompt)

    async def process_request(self, agent_id: str, request: Dict[str, Any]) -> Dict[str, Any]:
        """Process request with caching and monitoring"""
        cache_key = self._generate_cache_key(agent_id, request)
        
        if cache_key in self.result_cache:
            return self.result_cache[cache_key]
            
        result = await self.engine.execute_command(
            request.get("command"),
            request.get("params", {})
        )
        self.result_cache[cache_key] = result
        return result
