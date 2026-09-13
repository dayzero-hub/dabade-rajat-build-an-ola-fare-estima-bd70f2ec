from flask import Flask, jsonify, request

from fare import calculate_fare

app = Flask(__name__)


def _require_number(data, field, minimum=None, maximum=None):
    if field not in data:
        return None, f"{field} is required"
    value = data[field]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None, f"{field} must be a number"
    if minimum is not None and value < minimum:
        return None, f"{field} must be at least {minimum}"
    if maximum is not None and value > maximum:
        return None, f"{field} must be at most {maximum}"
    return value, None


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/estimate")
def estimate():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error="request body must be a JSON object"), 400

    distance_km, error = _require_number(data, "distance_km", minimum=0)
    if error:
        return jsonify(error=error), 400

    duration_min, error = _require_number(data, "duration_min", minimum=0)
    if error:
        return jsonify(error=error), 400

    if "surge" in data:
        surge, error = _require_number(data, "surge", minimum=1.0, maximum=3.0)
        if error:
            return jsonify(error=error), 400
    else:
        surge = 1.0

    total, breakdown = calculate_fare(distance_km, duration_min, surge)
    return jsonify(total=total, breakdown=breakdown)


if __name__ == "__main__":
    app.run(debug=True)
