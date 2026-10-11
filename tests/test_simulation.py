from app.core.simulation import simulate_revenue

def test_simulation():
    segments = [{"segment": "smb", "price": 49, "conversion": 0.06,
                 "market_size": 30000}]
    r = simulate_revenue(segments, {"smb": 49})
    assert r["total_mrr"] > 0

def test_price_increase_lowers_conversion():
    segments = [{"segment": "smb", "price": 49, "conversion": 0.06,
                 "market_size": 30000}]
    base = simulate_revenue(segments, {"smb": 49})
    higher = simulate_revenue(segments, {"smb": 79})
    assert higher["details"][0]["conversion"] < base["details"][0]["conversion"]
