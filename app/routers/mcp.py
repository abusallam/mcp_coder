from fastapi import APIRouter, Depends, HTTPException
from app.core.security import verify_api_key
from app.schemas.mcp import MCPServerCreate, MCPServerResponse
from typing import List

router = APIRouter()

@router.get("/servers", response_model=List[MCPServerResponse])
async def get_servers(api_key: str = Depends(verify_api_key)):
    """Get all MCP servers"""
    pass

@router.post("/servers", response_model=MCPServerResponse)
async def create_server(server: MCPServerCreate, api_key: str = Depends(verify_api_key)):
    """Create a new MCP server"""
    pass
