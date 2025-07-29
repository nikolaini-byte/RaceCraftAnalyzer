from sqlalchemy import Column, Float, ForeignKey, Integer, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel

class TelemetryData(BaseModel):
    """Stores high-frequency telemetry data for a lap"""
    __tablename__ = "telemetry_data"
    
    # Reference
    lap_id = Column(String(36), ForeignKey('laps.id'), nullable=False)
    lap = relationship("Lap", back_populates="telemetry")
    
    # Time series data (stored as JSON arrays, all synchronized by index)
    timestamps = Column(JSON, nullable=False)  # Relative timestamps in seconds
    
    # Position and motion
    positions = Column(JSON, nullable=True)    # List of [x,y,z] coordinates
    speeds = Column(JSON, nullable=True)      # Speed values (km/h or mph)
    
    # Driver inputs
    throttle = Column(JSON, nullable=True)     # 0.0 to 1.0
    brake = Column(JSON, nullable=True)        # 0.0 to 1.0
    steering = Column(JSON, nullable=True)     # -1.0 to 1.0
    
    # Vehicle data
    rpm = Column(JSON, nullable=True)          # Engine RPM
    gear = Column(JSON, nullable=True)         # Current gear
    drs = Column(JSON, nullable=True)          # DRS status (0 or 1)
    
    # Performance metrics
    g_force_lat = Column(JSON, nullable=True)  # Lateral G-force
    g_force_long = Column(JSON, nullable=True) # Longitudinal G-force
    
    # Derived metrics (can be calculated on the fly or stored)
    distance = Column(JSON, nullable=True)     # Distance along track
    
    def __repr__(self):
        return f"<TelemetryData(id={self.id}, lap_id={self.lap_id}, points={len(self.timestamps) if self.timestamps else 0})>"
    
    @property
    def data_points_count(self):
        """Return the number of data points in this telemetry set"""
        return len(self.timestamps) if self.timestamps else 0
