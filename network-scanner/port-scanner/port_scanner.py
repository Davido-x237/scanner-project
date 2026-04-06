import socket
import threading
from datetime import datetime

target = input("Enter target IP or domain: ")

print(f"\n[+] Scanning target: {target}\n")

open_ports = []
lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            with lock:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

        sock.close()

    except:
        pass

threads = []

start_time = datetime.now()

for port in range(1, 1001):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = datetime.now()

# Save results
filename = "scan_results.txt"

with open(filename, "w") as f:
    f.write(f"PORT SCAN REPORT\n")
    f.write(f"Target: {target}\n")
    f.write(f"Scan time: {start_time} - {end_time}\n\n")

    if open_ports:
        f.write("OPEN PORTS:\n")
        for port in open_ports:
            f.write(f"- {port}\n")
    else:
        f.write("No open ports found.\n")

print(f"\n[+] Scan complete. Results saved to {filename}")
