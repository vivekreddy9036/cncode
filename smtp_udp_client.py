import socket
import time

# Client configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 2525

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_command(command):
    print(f"[Client -> Server]: {command}")
    client_socket.sendto(command.encode(), (SERVER_HOST, SERVER_PORT))
    response, _ = client_socket.recvfrom(1024)
    print(f"[Server -> Client]: {response.decode()}")
    time.sleep(0.5)

# SMTP command sequence
send_command("HELO client.example.com")
send_command("MAIL FROM:<alice@example.com>")
send_command("RCPT TO:<bob@example.com>")
send_command("DATA")
send_command("Subject: Test Mail")
send_command("Hello Bob,")
send_command("This is a test message over UDP SMTP.")
send_command(".")   # End of message
send_command("QUIT")
