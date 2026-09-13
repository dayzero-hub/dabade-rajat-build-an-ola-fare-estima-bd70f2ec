from fare import calculate_fare


def test_normal_ride():
    total, breakdown = calculate_fare(distance_km=5, duration_min=10, surge=1.0)
    assert total == 130.0
    assert breakdown["minimum_fare_adjustment"] == 0.0


def test_ride_hits_minimum_floor():
    total, breakdown = calculate_fare(distance_km=0, duration_min=0, surge=1.0)
    assert total == 80.0
    assert breakdown["minimum_fare_adjustment"] > 0


def test_surge_at_lower_bound():
    total, _ = calculate_fare(distance_km=5, duration_min=10, surge=1.0)
    assert total == 130.0


def test_surge_at_upper_bound():
    total, _ = calculate_fare(distance_km=5, duration_min=10, surge=3.0)
    assert total == 390.0
