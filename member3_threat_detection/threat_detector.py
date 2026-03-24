import joblib
import pandas as pd
import time
from collections import defaultdict
from scapy.all import sniff, IP, TCP, UDP, wrpcap

# Load trained model
model = joblib.load("models/anomaly_model.pkl")

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

        # Smart alert control
        if prediction[0] == -1:
            ip = pkt[IP].src
            current_time = time.time()

            if current_time - last_alert_time[ip] > ALERT_INTERVAL:

                # Protocol detection (Wireshark-like)
                proto = "OTHER"
                if TCP in pkt:
                    proto = "TCP"
                elif UDP in pkt:
                    proto = "UDP"

                print(f"🚨 ALERT: {ip} | Protocol: {proto} | Size: {length}")

                last_alert_time[ip] = current_time

                # Save suspicious packet
                wrpcap(SUSPICIOUS_FILE, pkt, append=True)

# Start sniffing
sniff(prn=process_packet, store=False)