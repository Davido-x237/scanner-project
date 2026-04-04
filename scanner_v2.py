import socket

print("=== SIMPLE PORT SCANNER v2 ===")

target = input("Enter IP or domain: ")

print(f"\nScanning target: {target}\n")

for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    s.close()

print("\nScan complete.")
