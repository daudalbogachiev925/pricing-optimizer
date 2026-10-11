from app.core.gabor_granger import compute_gg

class O:
    def __init__(self, p, i, t):
        self.price = p; self.interested = i; self.total_asked = t

def test_gg_optimum():
    obs = [O(50, 100, 200), O(80, 70, 200), O(120, 40, 200)]
    r = compute_gg(obs)
    assert r["optimal_price"] in (50, 80, 120)
    assert r["revenue"] > 0

def test_gg_empty():
    assert compute_gg([]) is None
