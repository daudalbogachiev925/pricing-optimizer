def compute_gg(observations):
    points = []
    for o in observations:
        if o.total_asked <= 0:
            continue
        points.append({"price": o.price, "buyers": o.interested,
                        "revenue": o.price * o.interested})
    if not points:
        return None
    best = max(points, key=lambda x: x["revenue"])
    return {"optimal_price": best["price"], "revenue": best["revenue"],
            "buyers": best["buyers"],
            "curve": sorted(points, key=lambda x: x["price"])}
