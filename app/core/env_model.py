from pydantic import BaseModel, Field, validator
from typing import List
import os

class EnvironmentModel(BaseModel):
    # Server Configuration
    UVICORN_HOST: str = Field("0.0.0.0", description="Uvicorn host address")
    UVICORN_PORT: int = Field(8000, description="Uvicorn port number")
    DEBUG: bool = Field(False, description="Debug mode flag")
    PROJECT_NAME: str = Field("MCP Server", description="Project name")
    MAX_WORKERS: int = Field(4, description="Maximum number of workers")
    
    # Database Configuration
    SQLITE_DB_PATH: str = Field("/app/data/database.db", description="SQLite database path")
    DATABASE_URL: str = Field("sqlite:///data/database.db", description="Database URL")
    
    # API Configuration
    API_V1_STR: str = Field("/api/v1", description="API version 1 prefix")
    API_KEY: str = Field(..., description="API key for authentication")
    RATE_LIMIT: int = Field(100, description="API rate limit per minute")
    
    # AI Configuration
    AIDER_PATH: str = Field("/usr/local/bin/aider", description="Path to Aider executable")
    AIDER_MODEL: str = Field("gpt-4", description="AI model to use")
    AIDER_TEMPERATURE: float = Field(0.7, description="Model temperature")
    AIDER_MAX_TOKENS: int = Field(2000, description="Maximum tokens per response")
    AIDER_API_KEY: str = Field(..., description="OpenAI API key")
    AIDER_COMMIT_MESSAGE: str = Field("AI-assisted code changes", description="Git commit message")
    
    # Aider User Configuration
    AIDER_USER: str = Field(..., description="Aider user account")
    AIDER_PASSWORD: str = Field(..., description="Aider user password")
    AIDER_PERMISSIONS: List[str] = Field(
        default_factory=lambda: ["read", "write", "execute"],
        description="Aider permissions"
    )
    
    # Security Configuration
    CORS_ORIGINS: List[str] = Field(
        default_factory=lambda: ["https://mcp-coder.consulting.sa", 
                               "http://localhost:3000", 
                               "http://localhost:8000"]
    )
    
    # Monitoring Configuration
    LOG_LEVEL: str = Field("INFO", description="Logging level")
    ENABLE_METRICS: bool = Field(True, description="Enable Prometheus metrics")
    
    # Deployment Configuration
    DEPLOY_TOKEN: str = Field(None, description="Deployment token")
    
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
