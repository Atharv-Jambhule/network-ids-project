from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/alerts")
def alerts():
    # Placeholder data - replace with actual alert data
    alert_data = [
        {"attack": "DDoS", "ip": "192.168.1.100", "protocol": "TCP", "lat": 20.123, "lon": 78.456, "country": "India"},
        {"attack": "Port Scan", "ip": "192.168.1.101", "protocol": "UDP", "lat": 30.123, "lon": 80.456, "country": "India"}
    ]
    return jsonify(alert_data)

@app.route("/stats")
def stats():
    # Placeholder data - replace with actual statistics
    stats_data = {
        "total_alerts": 150,
        "ddos_attacks": 50,
        "port_scans": 30,
        "malware": 20,
        "other": 50
    }
    return jsonify(stats_data)
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

    