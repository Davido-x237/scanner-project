# 📡 Network Scanner

A Python-based local network reconnaissance tool that detects active devices in your LAN.

---

## 🚀 Features

- Automatically detects your local network range
- Scans all IPs in /24 subnet
- Identifies active devices using ICMP ping
- Displays total number of live hosts

---

## ⚙️ How It Works

The tool:
1. Detects your local IP address
2. Extracts network base (e.g. 192.168.1)
3. Pings all IPs from .1 to .254
4. Reports active devices

---

## ▶️ Usage

```bash
python3 network_scanner.py
