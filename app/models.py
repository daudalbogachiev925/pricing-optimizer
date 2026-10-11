from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class VWSurvey(Base):
    __tablename__ = "vw_surveys"
    id = Column(Integer, primary_key=True)
    respondent_id = Column(String, index=True)
    segment = Column(String, index=True)
    too_cheap = Column(Float, nullable=False)
    bargain = Column(Float, nullable=False)
    expensive = Column(Float, nullable=False)
    too_expensive = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

class GGObservation(Base):
    __tablename__ = "gg_observations"
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False, index=True)
    interested = Column(Integer, default=0)
    total_asked = Column(Integer, default=0)
    segment = Column(String, default="all")
    created_at = Column(DateTime, server_default=func.now())
