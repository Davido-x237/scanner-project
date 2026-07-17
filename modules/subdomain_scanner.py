import socket
import os
from datetime import datetime
from time import time

# ============================================
# CYBER RECON TOOLKIT - SUBDOMAIN SCANNER
# ============================================

print("\n" + "=" * 60)
print("        CYBER RECON TOOLKIT - SUBDOMAIN SCANNER")
print("=" * 60)

# Get domain name
domain = input("Enter domain (example: google.com): ").strip().lower()

if not domain:
    print("\n[-] Domain cannot be empty.")
    exit()

# Common subdomains
subdomains = [
    "www",
    "mail",
    "ftp",
    "test",
    "dev",
    "api",
    "blog",
    "shop",
    "admin",
    "portal",
    "vpn",
    "smtp",
    "ns1",
    "ns2",
    "cpanel",
    "webmail",
    "support",
    "docs",
    "download",
    "m"
]

# Create reports folder
os.makedirs("reports", exist_ok=True)

# Report filename
report_file = "reports/subdomain_report.txt"
print("\nScanning...\n")

start_time = time()

found = []

for sub in subdomains:

    subdomain = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(subdomain)

        print(f"[FOUND] {subdomain:<30} --> {ip}")

        found.append((subdomain, ip))

    except socket.gaierror:
        continue

end_time = time()
elapsed = round(end_time - start_time, 2)

print("\n" + "=" * 60)
print("SCAN SUMMARY")
print("=" * 60)

if found:

    print(f"Subdomains Found : {len(found)}\n")

    for subdomain, ip in found:
        print(f"{subdomain:<30} --> {ip}")

else:

    print("No common subdomains found.")

print(f"\nTime Taken : {elapsed} seconds")

# Save Report
with open(report_file, "a") as report:

    report.write("=" * 60 + "\n")
    report.write("CYBER RECON TOOLKIT - SUBDOMAIN SCAN REPORT\n")
    report.write("=" * 60 + "\n\n")
    report.write("\n")
    report.write("=" * 60 + "\n")
    report.write(f"Scan Date : {datetime.now()}\n")
    report.write("=" * 60 + "\n")

    report.write(f"Target Domain : {domain}\n")
    report.write(f"Date          : {datetime.now()}\n")
    report.write(f"Time Taken    : {elapsed} seconds\n\n")

    if found:

        report.write("DISCOVERED SUBDOMAINS\n")
        report.write("-" * 60 + "\n")

        for subdomain, ip in found:
            report.write(f"{subdomain:<30} {ip}\n")

    else:

        report.write("No common subdomains found.\n")

print(f"\n[+] Report saved to: {report_file}")
print("=" * 60)