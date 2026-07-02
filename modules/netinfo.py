import os

print("=== NETWORK INFORMATION TOOL ===\n")

print("Your IP Address:")
os.system("hostname -I")

print("\nDetailed Network Info:")
os.system("ip a")

print("\nRouting Table:")
os.system("ip route")
