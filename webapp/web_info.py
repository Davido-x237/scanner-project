import socket
import requests

print("=== WEBSITE INFO TOOL ===\n")

target = input("Enter website (e.g. google.com): ")

# Get IP
try:
    ip = socket.gethostbyname(target)
    print(f"\n[+] IP Address: {ip}")
except:
    print("Could not resolve IP")

# Get headers
try:
    response = requests.get("http://" + target)
    print("\n[+] HTTP Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
except:
    print("Could not fetch headers")
