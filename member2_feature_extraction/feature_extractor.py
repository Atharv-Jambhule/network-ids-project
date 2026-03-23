from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd

packets = rdpcap("captured_packets.pcap")

data = []

for pkt in packets:
    if IP in pkt:

        src_port = 0
        dst_port = 0

        if TCP in pkt:
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif UDP in pkt:
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport

        data.append({
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "packet_length": len(pkt),
            "src_port": src_port,
            "dst_port": dst_port
        })

df = pd.DataFrame(data)
df.to_csv("traffic_dataset.csv", index=False)

print("✅ Updated dataset created")