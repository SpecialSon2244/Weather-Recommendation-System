# Flask API for Predictions
"""
Flask API for Weather-Based Recommendation System
Author: Abhiram Ramakrishnan
"""

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("weather_model.pkl")

# Load the scaler
scaler = joblib.load("scaler.pkl")

# Load label encoders
label_encoders = joblib.load("label_encoders.pkl")

# Define feature names (must match training features)
FEATURES = [
    "MEAN ANNUAL AIR TEMP",
    "MEAN MONTHLY MAX TEMP",
    "MEAN MONTHLY MIN TEMP",
    "MEAN ANNUAL WIND SPEED",
    "MEAN CLOUD COVER",
    "MEAN ANNUAL SUNSHINE",
    "MEAN ANNUAL RAINFALL",
    "MAX MONTHLY WIND SPEED",
    "MAX AIR TEMP",
    "MAX WIND SPEED",
    "MAX RAINFALL",
    "MIN AIR TEMP",
    "EXTRA_FEATURE_1",
    "EXTRA_FEATURE_2",
    "EXTRA_FEATURE_3",
]


@app.route("/")
def home():
    return jsonify({"message": "Weather-Based Recommendation API is running!"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.json
        print("Received Data:", data)

        # Ensure input has all required features
        if not all(key in data for key in FEATURES):
            return jsonify({"error": "Missing required weather features"}), 400

        # Convert input data into numpy array
        input_data = np.array([[data[feature] for feature in FEATURES]])

        # Scale the input using the trained scaler
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)[0]

        # Decode predictions into human-readable recommendations
        decoded_predictions = {
            label: label_encoders[label].inverse_transform([pred])[0]
            for label, pred in zip(label_encoders.keys(), prediction)
        }

        return jsonify({"recommendations": decoded_predictions})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)


# Add your API script here

python api.py