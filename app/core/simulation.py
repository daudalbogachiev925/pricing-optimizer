def simulate_revenue(segments, prices, elasticity=1.5):
    total = 0.0
    details = []
    for s in segments:
        price = prices.get(s["segment"], s.get("price", 0))
        base_price = s.get("price", price)
        if base_price <= 0:
            continue
        delta = (price - base_price) / base_price
        conv = max(0.0, s["conversion"] * (1 - delta * elasticity))
        customers = s["market_size"] * conv
        mrr = customers * price
        total += mrr
        details.append({"segment": s["segment"], "price": price,
                        "conversion": round(conv, 4),
                        "customers": int(customers),
                        "mrr": round(mrr, 2)})
    return {"total_mrr": round(total, 2), "details": details}
