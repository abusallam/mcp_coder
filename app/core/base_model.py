from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any

class BaseResponseModel(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    timestamp: datetime = datetime.utcnow()
