import json
import os

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

model = joblib.load(os.path.join(BASE, "model.joblib"))
with open(os.path.join(BASE, "metadata.json")) as f:
    meta = json.load(f)


@app.route("/")
def home():
    return render_template("index.html", meta=meta)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    try:
        company = data["company"]
        name = data["name"]
        year = int(data["year"])
        kms = int(data["kms_driven"])
        fuel = data["fuel_type"]
    except (KeyError, TypeError, ValueError):
        return jsonify(error="Fill in every field with valid values."), 400

    if name not in meta["companies"].get(company, []):
        return jsonify(error="Choose a company and a model from the lists."), 400
    if not meta["year_min"] <= year <= meta["year_max"]:
        return jsonify(error=f"Year must be between {meta['year_min']} and {meta['year_max']}."), 400
    if not 0 <= kms <= 1_000_000:
        return jsonify(error="Kilometres driven must be between 0 and 1,000,000."), 400
    if fuel not in meta["fuel_types"]:
        return jsonify(error="Choose a fuel type from the list."), 400

    row = pd.DataFrame([{"name": name, "company": company, "year": year,
                         "kms_driven": kms, "fuel_type": fuel}])
    price = max(float(model.predict(row)[0]), 10000)
    return jsonify(price=int(round(price, -3)), mae=meta["mae"])


if __name__ == "__main__":
    app.run(debug=True)
