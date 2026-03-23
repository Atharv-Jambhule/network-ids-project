from scapy.all import rdpcap, IP
import pandas as pd

PCAP_FILE = "captured_packets.pcap"

packets = rdpcap(PCAP_FILE)

data = []

for pkt in packets:
    if IP in pkt:
        data.append({
            "src_ip": pkt[IP].src,
            "dst_ip": pkt[IP].dst,
            "packet_length": len(pkt)
        })

df = pd.DataFrame(data)

df.to_csv("traffic_dataset.csv", index=False)

print("Dataset created: traffic_dataset.csv")