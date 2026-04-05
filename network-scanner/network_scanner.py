import socket
import subprocess
import platform

print("=== NETWORK SCANNER (UPGRADED) ===\n")

# Auto-detect local network base
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"[+] Your IP: {local_ip}")

# Extract network base (simple method)
parts = local_ip.split(".")
network_base = f"{parts[0]}.{parts[1]}.{parts[2]}"

print(f"[+] Scanning network: {network_base}.0/24\n")

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-W", "1", ip]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

active_hosts = []

for i in range(1, 255):
    ip = f"{network_base}.{i}"

    if ping(ip):
        print(f"[ACTIVE] {ip}")
        active_hosts.append(ip)

print("\n=== SCAN COMPLETE ===")
print(f"Total active devices found: {len(active_hosts)}")
