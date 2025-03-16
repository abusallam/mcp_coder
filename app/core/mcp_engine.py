from typing import Dict, Any, Optional
from app.core.exceptions import MCPError
import asyncio
import logging
import time

class MCPEngine:
    """Enhanced MCP command execution engine"""
    
    def __init__(self):
        self.logger = logging.getLogger("mcp_engine")
        self._setup_monitoring()
        
    async def execute_command(self, command: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute MCP command with validation and monitoring"""
        try:
            with self._track_performance():
                result = await self._run_with_timeout(command, params)
                self._log_execution(command, params, result)
                return result
        except Exception as e:
            self._log_error(command, params, str(e))
            raise MCPError(f"Command failed: {str(e)}")

    async def _run_command(self, command: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Run command with advanced resource management"""
        async with self._get_resource_lock():
            start_time = time.time()
            try:
                result = await self._execute(command, params)
                self._record_performance(command, time.time() - start_time)
                return result
            except Exception as e:
                self._handle_execution_error(e, command, params)
                raise

    async def _execute(self, command: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute with advanced error handling and monitoring"""
        if self._circuit_breaker.is_open:
            raise MCPError("Circuit breaker is open")
            
        try:
            with self._track_performance():
                result = await self._run_with_timeout(command, params)
                self._update_metrics(command, "success")
                return result
        except Exception as e:
            self._update_metrics(command, "failure")
            self._circuit_breaker.record_failure()
            raise
