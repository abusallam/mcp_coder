from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class MCPServer(Base):
    __tablename__ = "mcp_servers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)
    config = Column(String)
