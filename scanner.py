import socket

target = input("Enter target IP: ")

print(f"\nScanning {target}...\n")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8000: "HTTP (Custom)"
}

for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        service = common_ports[port]
        print(f"[+] Port {port} OPEN → {service}")

    s.close()
