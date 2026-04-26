import joblib
import pandas as pd
import time
import requests
from collections import defaultdict
from scapy.all import sniff, IP, TCP, UDP, wrpcap

# Load trained model
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "anomaly_model.pkl")

model = joblib.load(MODEL_PATH)
print("🚀 Real-time IDS started...")

# Alert control
last_alert_time = defaultdict(float)
ALERT_INTERVAL = 5  # seconds

# File to store suspicious packets
SUSPICIOUS_FILE = "suspicious_packets.pcap"

def process_packet(pkt):
    if IP in pkt:

        # Ignore local traffic (optional)
        if pkt[IP].src.startswith("192.168"):
            return

        length = len(pkt)

        src_port = 0
        dst_port = 0

        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport

        # Feature creation
        features = pd.DataFrame(
            [[length, src_port, dst_port]],
            columns=["packet_length", "src_port", "dst_port"]
        )

        prediction = model.predict(features)

        # If anomaly detected
        if prediction[0] == -1:
            ip = pkt[IP].src
            current_time = time.time()

            if current_time - last_alert_time[ip] > ALERT_INTERVAL:

                # Protocol detection
                proto = "OTHER"
                if TCP in pkt:
                    proto = "TCP"
                elif UDP in pkt:
                    proto = "UDP"

                attack = "Anomaly"

                print(f"🚨 ALERT: {ip} | Protocol: {proto} | Size: {length}")

                last_alert_time[ip] = current_time

                # ✅ SEND TO FLASK (IMPORTANT)
                try:
                    requests.post("http://127.0.0.1:5000/add_alert", json={
                        "ip": ip,
                        "protocol": proto,
                        "length": length,
                        "attack": attack
                    })
                except:
                    print("⚠️ Flask server not running")

                # Save suspicious packet
                wrpcap(SUSPICIOUS_FILE, pkt, append=True)

# Start sniffing
sniff(prn=process_packet, store=False)