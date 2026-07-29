"""
CodeAlpha Cyber Security Internship - Task 1
Basic Network Sniffer

Captures live network packets and displays source/destination IPs,
protocol, ports, and a preview of the payload.

Requirements:
    pip install scapy

Windows: Install Npcap first -> https://npcap.com/#download
         (During install, check "Install Npcap in WinPcap API-compatible Mode")

Run (needs admin/root privileges):
    Windows (Run VS Code / terminal as Administrator):
        python network_sniffer.py
    Linux/Mac:
        sudo python3 network_sniffer.py
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# ------------------- CONFIG -------------------
INTERFACE = None          # None = auto-select default interface. Or set e.g. "Wi-Fi", "eth0"
PACKET_COUNT = 0          # 0 = capture indefinitely (stop with Ctrl+C)
FILTER = ""               # BPF filter, e.g. "tcp", "udp", "port 80". Empty = capture all
PAYLOAD_PREVIEW_LEN = 60  # how many bytes of payload to show
# ------------------------------------------------

packet_counter = 0


def get_protocol_name(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    else:
        return "OTHER"


def process_packet(packet):
    global packet_counter

    if not packet.haslayer(IP):
        return  # skip non-IP packets (ARP, etc.)

    packet_counter += 1
    ip_layer = packet[IP]
    proto = get_protocol_name(packet)
    timestamp = datetime.now().strftime("%H:%M:%S")

    src_ip = ip_layer.src
    dst_ip = ip_layer.dst

    src_port = dst_port = None
    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif packet.haslayer(UDP):
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    print("=" * 70)
    print(f"[#{packet_counter}] Time: {timestamp} | Protocol: {proto}")
    print(f"    Source IP      : {src_ip}" + (f":{src_port}" if src_port else ""))
    print(f"    Destination IP : {dst_ip}" + (f":{dst_port}" if dst_port else ""))
    print(f"    TTL            : {ip_layer.ttl}   | Packet Size: {len(packet)} bytes")

    if packet.haslayer(Raw):
        payload = packet[Raw].load
        try:
            decoded = payload[:PAYLOAD_PREVIEW_LEN].decode("utf-8", errors="replace")
        except Exception:
            decoded = str(payload[:PAYLOAD_PREVIEW_LEN])
        print(f"    Payload Preview: {decoded}")


def main():
    print("=" * 70)
    print(" Basic Network Sniffer - CodeAlpha Cyber Security Internship")
    print("=" * 70)
    print(f" Interface : {INTERFACE if INTERFACE else 'Default (auto)'}")
    print(f" Filter    : {FILTER if FILTER else 'None (all traffic)'}")
    print(" Press Ctrl+C to stop capturing.\n")

    try:
        sniff(
            iface=INTERFACE,
            filter=FILTER if FILTER else None,
            prn=process_packet,
            count=PACKET_COUNT,
            store=False,
        )
    except PermissionError:
        print("\n[!] Permission denied. Run this script as Administrator (Windows) or with sudo (Linux/Mac).")
    except KeyboardInterrupt:
        print(f"\n\n[+] Capture stopped. Total packets analyzed: {packet_counter}")


if __name__ == "__main__":
    main()