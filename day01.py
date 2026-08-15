import socket
import requests

def osint_scan(domain):
    ip = socket.gethostbyname(domain)
    geo = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
    print("===== DAY 1 OSINT SCAN =====")
    print("Domain :", domain)
    print("IP     :", ip)
    print("Location:", geo.get("city"), geo.get("country"))

osint_scan("example.com")
