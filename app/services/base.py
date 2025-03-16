from abc import ABC, abstractmethod
from typing import Dict, Any, TypeVar, Generic

T = TypeVar('T')

class BaseService(ABC, Generic[T]):
    """Base service interface for all services"""
    
    @abstractmethod
    async def create(self, data: Dict[str, Any]) -> T:
        pass

    @abstractmethod
    async def get(self, id: int) -> T:
        pass

    @abstractmethod
    async def list(self) -> list[T]:
        pass

    @abstractmethod
    async def update(self, id: int, data: Dict[str, Any]) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass
