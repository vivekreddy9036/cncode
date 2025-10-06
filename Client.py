import socket

def start_client():
    host = input("Enter server IP: ")
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f"[+] Connected to server at {host}:{port}")

    while True:
        data = s.recv(1824).decode()
        if not data:
            print("[-] Server disconnected.")
            break
        print(f"Server: {data}")

        msg = input("You: ")
        s.sendall(msg.encode())
        if msg.lower() in ["exit", "quit"]:
            break

    s.close()

if __name__ == "__main__":
    start_client()
