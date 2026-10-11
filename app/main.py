from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api import surveys, analysis

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pricing Optimizer", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(surveys.router, prefix="/api/surveys", tags=["surveys"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])

@app.get("/health")
def health():
    return {"status": "ok", "service": "pricing-optimizer"}
