import subprocess
import os
import logging

AIDER_PATH = os.getenv("AIDER_PATH", "/usr/local/bin/aider")

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AIDER_COMMANDS = [
    "/run", "/add", "/read", "/fix", "/improve", "/explain",
    "/generate", "/test", "/clean", "/document"
]

def execute_aider_command(command, params):
    if command not in AIDER_COMMANDS:
        raise ValueError(f"Unsupported command: {command}")

    try:
        result = subprocess.run(
            [AIDER_PATH, command, params],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Aider execution failed: {e.stderr}")
        raise ValueError(f"Error executing command: {e.stderr}")
