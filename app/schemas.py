from typing import Optional, List, Dict
from pydantic import BaseModel, Field

class VWCreate(BaseModel):
    respondent_id: str
    segment: Optional[str] = None
    too_cheap: float = Field(gt=0)
    bargain: float = Field(gt=0)
    expensive: float = Field(gt=0)
    too_expensive: float = Field(gt=0)

class VWRead(VWCreate):
    id: int
    class Config:
        from_attributes = True

class GGCreate(BaseModel):
    price: float = Field(gt=0)
    interested: int = Field(ge=0)
    total_asked: int = Field(gt=0)
    segment: str = "all"

class VWResult(BaseModel):
    pmc: Optional[float]
    idp: Optional[float]
    opp: Optional[float]
    optimal_range: List[float]
    n_respondents: int

class GGPoint(BaseModel):
    price: float
    buyers: int
    revenue: float

class GGOptimum(BaseModel):
    optimal_price: float
    revenue: float
    buyers: int
    curve: List[GGPoint]

class SegmentSim(BaseModel):
    segment: str
    price: float
    conversion: float
    market_size: int

class SimulationResult(BaseModel):
    total_mrr: float
    details: List[Dict]
