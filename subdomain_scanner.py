import socket

print("=== SUBDOMAIN SCANNER ===\n")

domain = input("Enter domain (e.g. example.com): ")

subdomains = [
    "www", "mail", "ftp", "test", "dev", "api",
    "blog", "shop", "admin", "portal"
]

print("\nScanning...\n")

for sub in subdomains:
    subdomain = f"{sub}.{domain}"
    
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[FOUND] {subdomain} --> {ip}")
    except:
        pass

print("\nScan complete.")
