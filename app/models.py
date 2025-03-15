from pydantic import BaseModel

class AiderCommand(BaseModel):
    command: str
    params: str
