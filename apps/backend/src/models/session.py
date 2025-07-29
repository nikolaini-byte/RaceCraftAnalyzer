from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class Session(BaseModel):
    """Represents a racing session with telemetry data"""
    __tablename__ = "sessions"
    
    # Basic session info
    name = Column(String(255), nullable=True)
    track_name = Column(String(255), nullable=True)
    vehicle = Column(String(100), nullable=True)
    
    # Timing
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    duration_seconds = Column(JSON, nullable=True)  # Store as {'minutes': x, 'seconds': y}
    
    # Session metadata
    session_type = Column(String(50), nullable=True)  # Practice, Qualifying, Race, etc.
    weather_conditions = Column(JSON, nullable=True)  # Store weather data as JSON
    
    # Relationships
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="sessions")
    laps = relationship("Lap", back_populates="session", cascade="all, delete-orphan")
    
    # Telemetry file info
    original_filename = Column(String(255), nullable=True)
    file_format = Column(String(10), nullable=True)  # CSV, JSON, etc.
    
    def __repr__(self):
        return f"<Session(id={self.id}, name='{self.name}', track='{self.track_name}')>"
    
    @property
    def lap_count(self):
        return len(self.laps) if self.laps else 0
    
    @property
    def best_lap(self):
        if not self.laps:
            return None
        return min((lap for lap in self.laps if lap.lap_time), 
                  key=lambda x: x.lap_time, 
                  default=None)
