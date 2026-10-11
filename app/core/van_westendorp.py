import numpy as np

def compute_vw(surveys, price_max=500):
    prices = np.arange(0, price_max, 1.0)
    if not surveys:
        return {"pmc": None, "idp": None, "opp": None,
                "optimal_range": [0, 0], "n_respondents": 0}

    def cum_below(col):
        return np.array([sum(getattr(s, col) >= p for s in surveys) / len(surveys)
                         for p in prices])

    def cum_above(col):
        return np.array([sum(getattr(s, col) <= p for s in surveys) / len(surveys)
                         for p in prices])

    too_cheap = cum_below("too_cheap")
    bargain = cum_below("bargain")
    expensive = cum_above("expensive")
    too_expensive = cum_above("too_expensive")

    def cross(a, b):
        for i in range(len(a) - 1):
            if (a[i] - b[i]) * (a[i + 1] - b[i + 1]) < 0:
                return float(prices[i])
        return None

    pmc = cross(bargain, expensive)
    idp = cross(too_cheap, expensive)
    opp = cross(too_cheap, too_expensive)

    optimal = [x for x in [pmc, opp] if x is not None]
    return {"pmc": pmc, "idp": idp, "opp": opp,
            "optimal_range": optimal if len(optimal) == 2 else [0, 0],
            "n_respondents": len(surveys)}
