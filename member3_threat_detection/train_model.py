import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load dataset
df = pd.read_csv("traffic_dataset.csv")

# Select features
X = df[["packet_length", "src_port", "dst_port"]]

# Train model
model = IsolationForest(contamination=0.05)
model.fit(X)

# Save model
joblib.dump(model, "models/anomaly_model.pkl")

print("✅ Model trained and saved")