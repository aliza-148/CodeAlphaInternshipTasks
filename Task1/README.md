# CodeAlpha - Basic Network Sniffer 🛜

## What does this project do? 

Whenever we use the internet (YouTube, WhatsApp, or any website), our laptop
sends and receives small pieces of data called **packets**.

This program **captures** those packets as they pass through the computer and
displays the following information on the screen:

* 📤 **Source IP** — where the packet came from (website/server)
* 📥 **Destination IP** — where the packet is going (your computer)
* 🔌 **Protocol** — the type of packet (TCP, UDP, or ICMP)
* 📦 **Packet Size** — the size of the packet (in bytes)
* 👀 **Payload Preview** — a small preview of the packet's data (if it can be read)

> **Note:** Most websites (Google, YouTube, etc.) send their data in encrypted
> form (HTTPS), so the payload usually appears as random characters. This is
> completely normal and indicates that the connection is secure.

---

## What happens in the file? (Code walkthrough)

File name: `network_sniffer.py`

1. **Library import:** The project uses the `scapy` library to capture and
   analyze network packets.

2. **`sniff()` function:** This function puts the computer's network interface
   into listening mode so it can monitor all incoming and outgoing packets.

3. **`process_packet()` function:** Whenever a packet is captured, this function
   automatically runs and extracts its details (IP, protocol, size, and payload)
   before displaying them on the screen.

4. **Loop:** The program continues capturing packets until you stop it by
   pressing `Ctrl + C`. At the end, it also displays the total number of packets
   that were captured.

---

## How to run the project?

### Requirements

```bash
pip install scapy
```

Windows users: Install [Npcap](https://npcap.com/#download) first and enable the
**"WinPcap API-compatible Mode"** option during installation.

### Run the program (Administrator/sudo privileges are required)

```bash
# Windows (Open VS Code as Administrator)
python network_sniffer.py

# Linux/Mac
sudo python3 network_sniffer.py
```

To stop the program, press: `Ctrl + C`

---


## Tools Used
- Python
- Scapy (packet capturing library)

## Task
CodeAlpha Cyber Security Internship — Task 1: Basic Network Sniffer
