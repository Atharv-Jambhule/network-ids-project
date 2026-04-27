import joblib
import pandas as pd
import time
import requests
import os
from collections import defaultdict
from scapy.all import sniff, IP, TCP, UDP, wrpcap

# 🔥 LOAD MODEL PATH CORRECTLY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "anomaly_model.pkl")

model = joblib.load(MODEL_PATH)

print("🚀 Real-time IDS started...")

# ALERT CONTROL
last_alert_time = defaultdict(float)
ALERT_INTERVAL = 5  # seconds

# FILE FOR WIRESHARK
SUSPICIOUS_FILE = "suspicious_packets.pcap"

def process_packet(pkt):
    if IP in pkt:

        # IGNORE LOCAL TRAFFIC
        if pkt[IP].src.startswith(("192.168", "10.")):
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

        # CREATE FEATURES
        features = pd.DataFrame(
            [[length, src_port, dst_port]],
            columns=["packet_length", "src_port", "dst_port"]
        )

        prediction = model.predict(features)

        # 🚨 IF ANOMALY
        if prediction[0] == -1:
            ip = pkt[IP].src
            current_time = time.time()

            if current_time - last_alert_time[ip] > ALERT_INTERVAL:

                proto = "OTHER"
                if TCP in pkt:
                    proto = "TCP"
                elif UDP in pkt:
                    proto = "UDP"

                attack = "Anomaly"

                print(f"🚨 ALERT: {ip} | Protocol: {proto} | Size: {length}")

                last_alert_time[ip] = current_time

                # 🔥 SEND TO DASHBOARD (API)
                try:
                    requests.post(
                        "http://127.0.0.1:5000/add_alert",
                        json={
                            "ip": ip,
                            "protocol": proto,
                            "length": length,
                            "attack": attack
                        },
                        timeout=2
                    )
                except:
                    print("⚠️ Flask server not running")

                # SAVE FOR WIRESHARK
                wrpcap(SUSPICIOUS_FILE, pkt, append=True)

# START SNIFFING
sniff(prn=process_packet, store=False)