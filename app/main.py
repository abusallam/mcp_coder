from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from fastapi.middleware.cors import CORSMiddleware
from app.helpers import execute_aider_command
import os
import logging
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Custom exception classes
class CommandExecutionError(Exception):
    pass

class InvalidCommandError(CommandExecutionError):
    pass

class InvalidParamsError(CommandExecutionError):
    pass

# Configure CORS for domain access
# Externalize CORS origins to environment variables
origins: List[str] = os.getenv("CORS_ORIGINS", "https://mcp-coder.consulting.sa,http://localhost:3000,http://localhost:8000").split(",")

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

    @validator("command")
    def validate_command(cls, command):
        allowed_commands = ["/run", "/add", "/read", "/fix", "/improve", "/explain", "/generate", "/test", "/clean", "/document"]
        if command not in allowed_commands:
            raise ValueError(f"Command '{command}' is not allowed.")
        return command

    @validator("params")
    def validate_params(cls, params, values):
        command = values.get("command")
        # Add command-specific parameter validation here
        if command == "aider" and not isinstance(params, str):
            raise ValueError("Params must be a string for aider command.")
        return params

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
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except CommandExecutionError as e:
        logger.error(f"Execution error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint for deployment monitoring
@app.get("/health/")
def health_check():
    """
    Health check endpoint for deployment monitoring.

    Returns:
        dict: A dictionary containing the status.
    """
    return {"status": "ok"}
