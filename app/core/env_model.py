from pydantic import BaseModel, Field, validator
from typing import List
import os

class EnvironmentModel(BaseModel):
    # Server Configuration
    UVICORN_HOST: str = Field("0.0.0.0", description="Uvicorn host address")
    UVICORN_PORT: int = Field(8000, description="Uvicorn port number")
    DEBUG: bool = Field(False, description="Debug mode flag")
    PROJECT_NAME: str = Field("MCP Server", description="Project name")
    
    # Database Configuration
    SQLITE_DB_PATH: str = Field("/app/data/database.db", description="SQLite database path")
    DATABASE_URL: str = Field("sqlite:///data/database.db", description="Database URL")
    
    # API Configuration
    API_V1_STR: str = Field("/api/v1", description="API version 1 prefix")
    API_KEY: str = Field(..., description="API key for authentication")
    
    # AI Configuration
    AIDER_PATH: str = Field("/usr/local/bin/aider", description="Path to Aider executable")
    AI_PROVIDERS: List[str] = Field(["aider"], description="Enabled AI providers")
    
    # Security Configuration
    CORS_ORIGINS: List[str] = Field(
        default_factory=lambda: ["https://mcp-coder.consulting.sa", 
                               "http://localhost:3000", 
                               "http://localhost:8000"]
    )
    
    @validator("DATABASE_URL", pre=True)
    def validate_database_url(cls, v, values):
        if not v:
            db_path = values.get("SQLITE_DB_PATH", "/app/data/database.db")
            return f"sqlite:///{db_path}"
        return v

    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global instance
env = EnvironmentModel()
