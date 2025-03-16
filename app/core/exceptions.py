from fastapi import HTTPException, status

class BaseAPIException(HTTPException):
    """Base API exception"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)

class AIProviderError(BaseAPIException):
    """AI provider specific errors"""
    pass

class ValidationError(BaseAPIException):
    """Data validation errors"""
    pass
