from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import VWSurvey, GGObservation
from app.schemas import VWCreate, VWRead, GGCreate

router = APIRouter()

@router.post("/vw", response_model=VWRead, status_code=201)
def create_vw(payload: VWCreate, db: Session = Depends(get_db)):
    s = VWSurvey(**payload.model_dump())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

@router.post("/vw/batch", status_code=201)
def batch_vw(payloads: List[VWCreate], db: Session = Depends(get_db)):
    for p in payloads:
        db.add(VWSurvey(**p.model_dump()))
    db.commit()
    return {"inserted": len(payloads)}

@router.get("/vw", response_model=List[VWRead])
def list_vw(db: Session = Depends(get_db)):
    return db.query(VWSurvey).all()

@router.post("/gg", status_code=201)
def create_gg(payload: GGCreate, db: Session = Depends(get_db)):
    o = GGObservation(**payload.model_dump())
    db.add(o)
    db.commit()
    return {"id": o.id}

@router.get("/gg")
def list_gg(db: Session = Depends(get_db)):
    return db.query(GGObservation).all()

@router.delete("/vw", status_code=204)
def delete_vw(db: Session = Depends(get_db)):
    db.query(VWSurvey).delete()
    db.commit()
