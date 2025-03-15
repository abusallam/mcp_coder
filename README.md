# MCP Server - Aider-Powered Code Agent

This project provides an **MCP-based coding agent** that integrates with **Aider** for remote code editing and execution. The system supports all essential Aider commands like `/run`, `/add`, `/read`, and more via an API.

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
