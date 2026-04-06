# 🔌 Port Scanner v2

A multi-threaded Python port scanner that detects open ports and exports results to a file.

---

## 🚀 Features

- Multi-threaded scanning (faster execution)
- Scans ports 1–1000
- Detects open TCP ports
- Saves results to `scan_results.txt`

---

## ⚙️ How It Works

1. User enters a target IP or domain
2. Program scans ports concurrently using threads
3. Open ports are collected
4. Results are saved to a report file

---

## ▶️ Usage

```bash
python3 port_scanner.py
