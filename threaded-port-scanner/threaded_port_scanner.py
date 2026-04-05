import socket
import threading

print("=== THREADED PORT SCANNER ===\n")

target = input("Enter target IP or domain: ")

# Resolve domain to IP
try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target")
    exit()

print(f"\nScanning target: {target_ip}\n")

# Function to scan a port
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((target_ip, port))
        print(f"[OPEN] Port {port}")
    except:
        pass
    finally:
        s.close()

# Create threads
threads = []

for port in range(1, 1025):  # scanning first 1024 ports
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("\nScan complete.")
