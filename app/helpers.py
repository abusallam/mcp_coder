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

import shlex

def execute_aider_command(command, params):
    """
    Executes an Aider command with the given parameters.

    Args:
        command (str): The Aider command to execute.
        params (str): The parameters to pass to the Aider command.

    Returns:
        str: The output of the Aider command.

    Raises:
        ValueError: If the command is unsupported or if the Aider execution fails.
    """
    if command not in AIDER_COMMANDS:
        raise ValueError(f"Unsupported command: {command}")

    try:
        # Use shlex.split to properly quote arguments, preventing issues with spaces or special characters
        command_list = [AIDER_PATH, command] + shlex.split(params)
        result = subprocess.run(
            command_list,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Aider execution failed: {e.stderr}")
        raise ValueError(f"Error executing command: {e.stderr}")
