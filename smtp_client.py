import socket

def smtp_client():
    host = "127.0.0.1"
    port = 1025
    buffer_size = 1024

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_command(command):
        client_socket.sendto(command.encode(), (host, port))
        response, _ = client_socket.recvfrom(buffer_size)
        print("Server:", response.decode())

    # SMTP sequence
    send_command("HELO client.example.com")
    send_command("MAIL FROM:<alice@example.com>")
    send_command("RCPT TO:<bob@example.com>")
    send_command("DATA")

    print("Enter your email content. End with a single '.' on a line:")
    while True:
        line = input()
        client_socket.sendto(line.encode(), (host, port))
        if line == ".":
            break

    response, _ = client_socket.recvfrom(buffer_size)
    print("Server:", response.decode())

    send_command("QUIT")

    client_socket.close()

if __name__ == "__main__":
    smtp_client()
