FROM python:3.9-slim
# Set working directory
WORKDIR /app
# Install system dependencies (for Aider)
RUN apt-get update &&     apt-get install -y --no-install-recommends     curl     git     && rm -rf /var/lib/apt/lists/*
# Install Aider
RUN curl -sSL https://github.com/aider-ai/aider/releases/download/v0.1.2/aider-linux-amd64 -o /usr/local/bin/aider &&     chmod +x /usr/local/bin/aider
# Install project dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code
COPY ./app /app
ENV PYTHONPATH=/app
# Expose FastAPI's port
EXPOSE 8000
# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
