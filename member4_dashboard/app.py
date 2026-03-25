from flask import Flask, jsonify, render_template, request
import time

app = Flask(__name__)

# GLOBAL ALERT STORAGE
alerts = []

@app.route("/")
def home():
    return render_template("dashboard.html")

# GET alerts (for dashboard)
@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

# POST alert (from IDS)
@app.route("/add_alert", methods=["POST"])
def receive_alert():
    data = request.json

    alert = {
        "ip": data["ip"],
        "protocol": data["protocol"],
        "length": data["length"],
        "attack": data["attack"],
        "time": time.strftime("%H:%M:%S"),
        "lat": 20 + (len(alerts) % 10),
        "lon": 78 + (len(alerts) % 10),
        "country": "India"
    }

    alerts.append(alert)

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)