from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from app.core.config import settings

api_key_header = APIKeyHeader(name="X-API-Key")
agent_key_header = APIKeyHeader(name="X-Agent-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

async def verify_agent_key(api_key: str = Security(agent_key_header)):
    """Verify agent API key"""
    # Add agent key validation logic
    if not is_valid_agent_key(api_key):
        raise HTTPException(status_code=403, detail="Invalid agent key")
    return api_key
