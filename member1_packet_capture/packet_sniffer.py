from scapy.all import sniff
from pcap_logger import log_packet

def process_packet(packet):
    print("Packet captured")
    log_packet(packet)

def start_sniffing():
    print("Starting packet capture...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()