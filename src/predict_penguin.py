import requests
import pickle
import pandas as pd
import json
import os

# Define file paths
model_path = "models/model.pkl"
label_encoder_path = "models/le.pkl"
scaler_path = "models/scaler.pkl"
json_output_path = "data/penguin_prediction.json"

# Check if model files exist
if not all(os.path.exists(f) for f in [model_path, label_encoder_path, scaler_path]):
    raise FileNotFoundError("🚨 Missing one or more model files (model.pkl, le.pkl, scaler.pkl).")

# Load trained model, label encoder, and scaler
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(label_encoder_path, "rb") as f:
    le = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

# Define API URL
api_url = "http://130.225.39.127:8000/new_penguin/"

try:
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)
    data = response.json()
    print("✅ Successfully fetched penguin data from API.")
except (requests.RequestException, ValueError) as e:
    print(f"⚠️ Error fetching data from API: {e}")
    # Use mock data for local testing
    data = {
        "datetime": "2025-03-21 12:00:00",
        "bill_length_mm": 45.3,
        "bill_depth_mm": 18.2,
        "flipper_length_mm": 195.0,
        "body_mass_g": 3800
    }
    print("🔄 Using mock penguin data.")

# Prepare input features
features = [[
    data["bill_length_mm"],
    data["bill_depth_mm"],
    data["flipper_length_mm"],
    data["body_mass_g"]
]]

# Apply scaling
features_scaled = scaler.transform(features)

# Make prediction
predicted_species = model.predict(features_scaled)[0]
species = le.inverse_transform([predicted_species])[0]

# Format prediction as JSON
penguin_prediction = {
    "datetime": data["datetime"],
    "bill_length_mm": data["bill_length_mm"],
    "bill_depth_mm": data["bill_depth_mm"],
    "flipper_length_mm": data["flipper_length_mm"],
    "body_mass_g": data["body_mass_g"],
    "predicted_species": species
}

# Save updated predictions to JSON  
with open(json_output_path, "w") as f:
    json.dump(penguin_prediction, f, indent=4)

print(f"✅ Prediction made and saved successfully: {penguin_prediction}")