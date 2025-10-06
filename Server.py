import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[+] Socket successfully created")
except socket.error as err:
    print("[-] Socket creation failed with error:", err)
    sys.exit()

port = 80
hostname = 'www.google.com'

try:
    ip = socket.gethostbyname(hostname)
    print(f"[+] The IP address of {hostname} is {ip}")
except socket.gaierror:
    print("[-] Error resolving hostname.")
    sys.exit()

try:
    s.connect((ip, port))
    print(f"[+] Successfully connected to {hostname} on port {port}")
    s.close()
except socket.error as err:
    print(f"[-] Connection failed: {err}")
