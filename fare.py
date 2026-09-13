BASE_FARE = 50
PER_KM = 12
PER_MIN = 2
MINIMUM_FARE = 80


def calculate_fare(distance_km, duration_min, surge):
    """Returns (total, breakdown). Rounds once, at the end."""
    base = BASE_FARE
    distance_cost = PER_KM * distance_km
    duration_cost = PER_MIN * duration_min
    subtotal = base + distance_cost + duration_cost
    surged = subtotal * surge
    minimum_adjustment = max(MINIMUM_FARE - surged, 0)
    total = surged + minimum_adjustment

    breakdown = {
        "base": base,
        "distance_cost": distance_cost,
        "duration_cost": duration_cost,
        "subtotal": subtotal,
        "surge_multiplier": surge,
        "after_surge": surged,
        "minimum_fare_adjustment": minimum_adjustment,
        "total": round(total, 2),
    }
    return round(total, 2), breakdown


if __name__ == "__main__":
    total, breakdown = calculate_fare(distance_km=5, duration_min=10, surge=1.0)
    assert total == 130.0, total
    assert breakdown["after_surge"] + breakdown["minimum_fare_adjustment"] == total

    total, breakdown = calculate_fare(distance_km=0, duration_min=0, surge=1.0)
    assert total == MINIMUM_FARE, total

    total, breakdown = calculate_fare(distance_km=1, duration_min=1, surge=2.5)
    assert total == round((50 + 12 + 2) * 2.5, 2), total

    print("ok")
