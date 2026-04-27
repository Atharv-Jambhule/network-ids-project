from flask import Flask, jsonify, render_template, request
import time
import requests

app = Flask(__name__)

# GLOBAL ALERT STORAGE
alerts = []

# 🌍 GET REAL LOCATION
def get_location(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()
        return {
            "lat": res.get("lat", 0),
            "lon": res.get("lon", 0),
            "country": res.get("country", "Unknown")
        }
    except:
        return {
            "lat": 0,
            "lon": 0,
            "country": "Unknown"
        }

# HOME PAGE
@app.route("/")
def home():
    return render_template("dashboard.html")

# SEND ALERTS TO FRONTEND
@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

# RECEIVE ALERT FROM IDS
@app.route("/add_alert", methods=["POST"])
def receive_alert():
    data = request.json

    location = get_location(data["ip"])

    alert = {
        "ip": data["ip"],
        "protocol": data["protocol"],
        "length": data["length"],
        "attack": data["attack"],
        "time": time.strftime("%H:%M:%S"),
        "lat": location["lat"],
        "lon": location["lon"],
        "country": location["country"]
    }

    alerts.append(alert)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)