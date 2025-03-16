from fastapi import APIRouter, Depends, status, HTTPException
from app.services.ai_service import AIService
from app.core.exceptions import AIProviderError
from app.schemas.requests import CodeAnalysisRequest, CodeGenerationRequest
from app.schemas.responses import CodeAnalysisResponse, CodeGenerationResponse
from typing import Dict, Any, List
from app.core.base_model import BaseResponseModel
from app.services.mcp_service import MCPService
from app.core.security import verify_agent_key
from app.core.mcp import MCPCapability

router = APIRouter()

@router.post("/analyze", 
    response_model=BaseResponseModel,
    status_code=status.HTTP_200_OK,
    description="Analyze code using configured AI provider")
async def analyze_code(
    request: CodeAnalysisRequest,
    ai_service: AIService = Depends()
) -> BaseResponseModel:
    try:
        result = await ai_service.analyze(
            code=request.code,
            provider=request.provider
        )
        return BaseResponseModel(success=True, data=result)
    except AIProviderError as e:
        return BaseResponseModel(success=False, error=str(e))
    except Exception as e:
        raise AIProviderError(str(e))

@router.post("/generate", response_model=CodeGenerationResponse)
async def generate_code(prompt: str):
    """Generate code from prompt"""
    return await ai_service.generate(prompt)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/agent/register")
async def register_agent(
    agent_data: Dict[str, Any],
    mcp_service: MCPService = Depends()
) -> BaseResponseModel:
    """Register new agent with MCP server"""
    try:
        agent = await mcp_service.register_agent(agent_data)
        return BaseResponseModel(success=True, data=agent)
    except Exception as e:
        return BaseResponseModel(success=False, error=str(e))

@router.post("/process")
async def process_request(
    request: Dict[str, Any],
    agent_id: str,
    mcp_service: MCPService = Depends(),
    _: str = Depends(verify_agent_key)
) -> BaseResponseModel:
    """Process agent request"""
    # ...existing code...

@router.post("/code/analyze")
async def analyze_code(
    code: str,
    mcp_service: MCPService = Depends()
) -> BaseResponseModel:
    """Analyze code using Aider"""
    result = await mcp_service._analyze_code(code)
    return BaseResponseModel(success=True, data=result)

@router.post("/code/fix")
async def fix_code(
    code: str,
    mcp_service: MCPService = Depends()
) -> BaseResponseModel:
    """Fix code using Aider"""
    result = await mcp_service._fix_code(code)
    return BaseResponseModel(success=True, data=result)

@router.get("/capabilities")
async def get_capabilities(
    mcp_service: MCPService = Depends()
) -> BaseResponseModel:
    """Get MCP server capabilities"""
    return BaseResponseModel(
        success=True,
        data=mcp_service.capabilities
    )

@router.get("/capabilities/details")
async def get_capability_details(
    mcp_service: MCPService = Depends()
) -> BaseResponseModel:
    """Get detailed MCP server capabilities with examples"""
    return BaseResponseModel(
        success=True,
        data={
            "capabilities": mcp_service.capabilities,
            "examples": mcp_service.get_capability_examples(),
            "limits": mcp_service.get_capability_limits()
        }
    )

@router.post("/execute/{command}")
async def execute_command(
    command: str,
    params: Dict[str, Any],
    mcp_service: MCPService = Depends(),
    agent: Agent = Depends(get_authorized_agent)
) -> BaseResponseModel:
    try:
        result = await mcp_service.process_request(
            agent_id=agent.id,
            request={"command": command, "params": params}
        )
        return BaseResponseModel(success=True, data=result)
    except MCPError as e:
        return BaseResponseModel(success=False, error=str(e))

@router.post("/batch/execute")
async def execute_batch_commands(
    commands: List[Dict[str, Any]],
    mcp_service: MCPService = Depends(),
    agent: Agent = Depends(get_authorized_agent)
) -> BaseResponseModel:
    """Execute multiple MCP commands in batch with monitoring"""
    results = []
    failed = []
    
    for cmd in commands:
        try:
            result = await mcp_service.process_request(
                agent_id=agent.id,
                request=cmd
            )
            results.append(result)
        except Exception as e:
            failed.append({"command": cmd, "error": str(e)})
            
    return BaseResponseModel(
        success=len(failed) == 0,
        data={"results": results, "failed": failed}
    )
