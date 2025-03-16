from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)  # active, inactive, busy
    capabilities = Column(JSON)  # available tools and prompts
    last_seen = Column(DateTime, default=datetime.utcnow)
    is_authorized = Column(Boolean, default=False)
    api_key = Column(String, unique=True)
