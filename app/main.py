from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.helpers import execute_aider_command
import os
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure CORS for domain access
origins = [
    "https://mcp-coder.consulting.sa",
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Define request model for Aider commands
class AiderCommand(BaseModel):
    command: str
    params: str

@app.post("/execute/")
async def execute_command(command_request: AiderCommand):
    """
    Executes an Aider command with parameters.

    Args:
        command_request (AiderCommand): The Aider command and parameters to execute.

    Returns:
        dict: A dictionary containing the executed command and the result.

    Raises:
        HTTPException: If the command execution fails.
    """
    try:
        logger.info(f"Executing command: {command_request.command} with params: {command_request.params}")
        result = execute_aider_command(command_request.command, command_request.params)
        return {"command": command_request.command, "result": result}
    except ValueError as e:
        logger.error(f"Execution error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

# Health check endpoint for deployment monitoring
@app.get("/health/")
def health_check():
    """
    Health check endpoint for deployment monitoring.

    Returns:
        dict: A dictionary containing the status.
    """
    return {"status": "ok"}
