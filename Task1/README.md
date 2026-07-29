# CodeAlpha - Basic Network Sniffer 🛜

## Ye project kya karta hai? (Simple explanation)

Jab bhi hum internet use karte hain (YouTube, WhatsApp, koi bhi website), hamara
laptop chhoti chhoti "chitthiyan" bhejta aur receive karta hai. Inhe **packets**
kehte hain.

Ye program un packets ko **pakadta (capture)** hai jab wo hamare laptop se guzarte
hain, aur screen pe dikhata hai:

- 📤 **Source IP** — packet kahan se aaya (kis website/server se)
- 📥 **Destination IP** — packet kahan jaa raha hai (hamare laptop pe)
- 🔌 **Protocol** — kis tarah ka packet hai (TCP, UDP, ya ICMP)
- 📦 **Packet Size** — packet ka size (bytes mein)
- 👀 **Payload Preview** — packet ke andar ka thoda sa data (agar padha ja sake)

> **Note:** Zyada tar websites (Google, YouTube, etc.) apna data encrypt karke
> bhejti hain (HTTPS), isliye payload zyada tar random letters jaisa dikhta hai —
> ye normal hai, iska matlab security theek kaam kar rahi hai.

---

## File mein kya ho raha hai? (Code walkthrough)

Faayl ka naam: `network_sniffer.py`

1. **Library import:** `scapy` naam ki library use hoti hai jo network packets
   capture karne mein madad karti hai.

2. **`sniff()` function:** Ye function laptop ke network card ko "sunne" (listen)
   ke mode mein daal deta hai — jaise koi guard darwaze pe khada ho kar har
   chitthi check kar raha ho.

3. **`process_packet()` function:** Jab bhi koi packet pakda jata hai, ye function
   automatically chal jata hai aur us packet ki details (IP, protocol, size,
   payload) nikal kar screen pe print kar deta hai.

4. **Loop:** Ye process tab tak chalta rehta hai jab tak hum `Ctrl + C` dabakar
   ise rok nahi dete. Aakhir mein total kitne packets capture hue, wo bhi
   dikhata hai.

---

## Kaise run karein?

### Requirements
```bash
pip install scapy
```
Windows users: pehle [Npcap](https://npcap.com/#download) install karna zaroori
hai ("WinPcap API-compatible Mode" checkbox check karke).

### Run karna (Admin/sudo zaroori hai)
```bash
# Windows (VS Code ko Administrator mode mein khol kar)
python network_sniffer.py

# Linux/Mac
sudo python3 network_sniffer.py
```

Rokne ke liye: `Ctrl + C`

---

## Tools Used
- Python
- Scapy (packet capturing library)

## Task
CodeAlpha Cyber Security Internship — Task 1: Basic Network Sniffer
