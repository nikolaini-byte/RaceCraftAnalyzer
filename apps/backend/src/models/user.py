from sqlalchemy import Column, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime
from passlib.context import CryptContext
from ..core.config import settings
from .base import BaseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    # sessions = relationship("Session", back_populates="user")
    
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
    
    def set_password(self, password: str) -> None:
        self.hashed_password = pwd_context.hash(password)
        
    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return pwd_context.hash(password)
