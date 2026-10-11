import random
from app.database import SessionLocal
from app.models import VWSurvey, GGObservation

def seed(n=200):
    db = SessionLocal()
    try:
        for i in range(n):
            seg = random.choice(["consumer", "smb", "enterprise"])
            scale = {"consumer": 1.0, "smb": 1.8, "enterprise": 3.5}[seg]
            tc = random.randint(5, 20) * scale
            b = random.randint(20, 40) * scale
            e = random.randint(50, 80) * scale
            te = random.randint(90, 150) * scale
            db.add(VWSurvey(respondent_id=f"r{i}", segment=seg,
                             too_cheap=tc, bargain=b,
                             expensive=e, too_expensive=te))

        for p in [30, 50, 80, 120, 180, 250]:
            db.add(GGObservation(price=p, interested=int(200 - p * 0.5),
                                  total_asked=200))

        db.commit()
        print(f"Seeded {n} VW surveys + {6} GG observations")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
