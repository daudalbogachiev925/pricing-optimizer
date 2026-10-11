from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import VWSurvey, GGObservation
from app.schemas import (VWResult, GGOptimum, GGPoint,
                         SegmentSim, SimulationResult)
from app.core.van_westendorp import compute_vw
from app.core.gabor_granger import compute_gg
from app.core.simulation import simulate_revenue
from app.config import settings

router = APIRouter()

@router.get("/vw", response_model=VWResult)
def vw(segment: str = None, db: Session = Depends(get_db)):
    q = db.query(VWSurvey)
    if segment:
        q = q.filter(VWSurvey.segment == segment)
    return compute_vw(q.all(), price_max=settings.VW_PRICE_MAX)

@router.get("/gg", response_model=GGOptimum)
def gg(db: Session = Depends(get_db)):
    result = compute_gg(db.query(GGObservation).all())
    if result is None:
        return GGOptimum(optimal_price=0, revenue=0, buyers=0, curve=[])
    return GGOptimum(
        optimal_price=result["optimal_price"],
        revenue=result["revenue"], buyers=result["buyers"],
        curve=[GGPoint(**p) for p in result["curve"]])

@router.post("/simulate", response_model=SimulationResult)
def simulate(segments: List[SegmentSim], prices: dict):
    seg_dicts = [s.model_dump() for s in segments]
    return simulate_revenue(seg_dicts, prices,
                             elasticity=settings.ELASTICITY)
