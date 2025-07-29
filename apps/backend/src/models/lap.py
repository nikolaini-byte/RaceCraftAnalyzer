from datetime import timedelta
from sqlalchemy import Column, Integer, Float, ForeignKey, JSON, Interval
from sqlalchemy.orm import relationship
from .base import BaseModel

class Lap(BaseModel):
    """Represents a single lap within a racing session"""
    __tablename__ = "laps"
    
    # Lap identification
    lap_number = Column(Integer, nullable=False)
    is_valid = Column(Integer, default=1)  # 1 for valid, 0 for invalid
    
    # Timing
    lap_time = Column(Interval, nullable=True)  # Stored as PostgreSQL interval
    sector_times = Column(JSON, nullable=True)  # List of sector times in seconds
    
    # Performance metrics
    top_speed = Column(Float, nullable=True)  # km/h or mph
    avg_speed = Column(Float, nullable=True)
    fuel_used = Column(Float, nullable=True)  # Liters or gallons
    
    # Track position
    start_position = Column(JSON, nullable=True)  # {x, y, z} coordinates
    end_position = Column(JSON, nullable=True)    # {x, y, z} coordinates
    
    # Relationships
    session_id = Column(String(36), ForeignKey('sessions.id'), nullable=False)
    session = relationship("Session", back_populates="laps")
    telemetry = relationship("TelemetryData", back_populates="lap", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Lap(id={self.id}, number={self.lap_number}, time={self.formatted_lap_time})>"
    
    @property
    def formatted_lap_time(self):
        if not self.lap_time:
            return "No time"
        # Convert to mm:ss.fff format
        total_seconds = self.lap_time.total_seconds()
        minutes = int(total_seconds // 60)
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:06.3f}"
    
    @property
    def sector_count(self):
        return len(self.sector_times) if self.sector_times else 0
