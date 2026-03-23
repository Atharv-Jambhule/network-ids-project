from scapy.all import wrpcap

PCAP_FILE = "captured_packets.pcap"

def log_packet(packet):
    wrpcap(PCAP_FILE, packet, append=True)