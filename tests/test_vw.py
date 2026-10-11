from app.core.van_westendorp import compute_vw

class S:
    def __init__(self, tc, b, e, te):
        self.too_cheap = tc; self.bargain = b
        self.expensive = e; self.too_expensive = te

def test_vw_basic():
    surveys = [S(5, 20, 50, 80), S(10, 25, 60, 100),
               S(8, 22, 55, 90), S(6, 18, 45, 85)]
    r = compute_vw(surveys, price_max=120)
    assert r["pmc"] is not None
    assert len(r["optimal_range"]) == 2
    assert r["n_respondents"] == 4

def test_vw_empty():
    r = compute_vw([], price_max=120)
    assert r["pmc"] is None
    assert r["n_respondents"] == 0
