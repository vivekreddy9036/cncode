import socket

def smtp_server():
    host = "127.0.0.1"
    port = 1025
    buffer_size = 1024

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"SMTP UDP Server listening on {host}:{port}...")

    message_store = {}

    while True:
        data, addr = server_socket.recvfrom(buffer_size)
        command = data.decode().strip()

        print(f"Received: {command} from {addr}")

        if command.startswith("HELO"):
            server_socket.sendto(b"250 Hello, pleased to meet you", addr)

        elif command.startswith("MAIL FROM"):
            message_store["from"] = command[10:]
            server_socket.sendto(b"250 OK - Sender accepted", addr)

        elif command.startswith("RCPT TO"):
            message_store["to"] = command[8:]
            server_socket.sendto(b"250 OK - Recipient accepted", addr)

        elif command.startswith("DATA"):
            server_socket.sendto(b"354 Start mail input; end with '.' on a line", addr)
            email_data = []
            while True:
                data, _ = server_socket.recvfrom(buffer_size)
                line = data.decode().strip()
                if line == ".":
                    break
                email_data.append(line)
            message_store["data"] = "\n".join(email_data)
            server_socket.sendto(b"250 OK - Message accepted for delivery", addr)

        elif command.startswith("QUIT"):
            server_socket.sendto(b"221 Bye", addr)
            print("Closing connection.")
            break

        else:
            server_socket.sendto(b"500 Command not recognized", addr)


if __name__ == "__main__":
    smtp_server()
