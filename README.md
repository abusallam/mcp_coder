# MCP Server (Model Control Present)

AI-powered code management server supporting multiple AI providers including Aider, Gemini, and Sonnet.

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure variables
3. Run with Docker:
```bash
docker-compose up -d
```

## Configuration

Configure AI providers in `.env`:
- Aider: OpenAI-based code assistance
- Gemini: Google's AI model
- Sonnet: Custom AI provider

## Deployment

### Prerequisites
- Python 3.9+
- Docker and Docker Compose
- Valid API keys for chosen AI providers

### Manual Deployment
```bash
# 1. Set up environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env
# Edit .env with your settings

# 3. Start the application
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Health Monitoring
- Health check endpoint: `/api/v1/health`
- Metrics: `/api/v1/metrics`
- Logs: Check Docker logs or application logs in `/var/log/mcp-server/`

## API Documentation
- OpenAPI docs: `/api/docs`
- ReDoc: `/api/redoc`

## Features

✅ Supports all **Aider commands** (`/run`, `/add`, `/read`, `/fix`, etc.)  
✅ **FastAPI-based** for high performance and async support  
✅ **Structured logging** for debugging and monitoring  
✅ **Production-ready** with **Docker Compose** deployment  
✅ **Coolify CI/CD Ready** with GitHub Actions  

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd mcp-server-updated
    ```

2. Set up environment variables:
    ```bash
    cp .env.example .env
    ```

3. Start the service with Docker Compose:
    ```bash
    docker-compose up --build
    ```

4. API is available at `http://localhost:8000`.

## API Endpoints

### `/execute/`

- **POST**: Executes an Aider command.
    - **Request Body**:
    ```json
    {
      "command": "/run",
      "params": "def foo(): return 42"
    }
    ```
    - **Response**:
    ```json
    {
      "command": "/run",
      "result": "Modified code output..."
    }
    ```

### `/health/`
- **GET**: Returns `{ "status": "ok" }` to verify deployment.

## Deployment with Coolify

1. Push the project to GitHub.  
2. Configure Coolify to deploy from your GitHub repository.  
3. Add `COOLIFY_API_KEY` as a GitHub secret for automatic deployment.  

## License

MIT
