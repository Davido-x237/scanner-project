import requests
import socket

print("=== IP GEOLOCATION TRACKER ===\n")

target = input("Enter IP or domain: ")

# Convert domain to IP if needed
try:
    ip = socket.gethostbyname(target)
except:
    print("Invalid domain/IP")
    exit()

print(f"\n[+] Resolved IP: {ip}")

# API request
url = f"http://ip-api.com/json/{ip}"

try:
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print("\n🌍 Location Information:")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
    else:
        print("Could not retrieve data.")

except:
    print("Error connecting to API.")
