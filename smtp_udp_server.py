import socket

# Server configuration
HOST = "127.0.0.1"
PORT = 2525

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"SMTP UDP Server running on {HOST}:{PORT}")

message_storage = ""
in_data_mode = False

while True:
    data, addr = server_socket.recvfrom(1024)
    command = data.decode().strip()
    print(f"[Client -> Server]: {command}")

    response = ""

    if in_data_mode:
        if command == ".":
            in_data_mode = False
            response = "250 Message accepted for delivery"
            print(f"[Server Log] Stored message:\n{message_storage}\n")
            message_storage = ""
        else:
            message_storage += command + "\n"
    else:
        if command.startswith("HELO"):
            response = "250 Hello, pleased to meet you"
        elif command.startswith("MAIL FROM"):
            response = "250 Sender OK"
        elif command.startswith("RCPT TO"):
            response = "250 Recipient OK"
        elif command == "DATA":
            response = "354 Start mail input; end with <CRLF>.<CRLF>"
            in_data_mode = True
        elif command == "QUIT":
            response = "221 Closing connection"
        else:
            response = "500 Command unrecognized"

    # Send response
    server_socket.sendto(response.encode(), addr)
    print(f"[Server -> Client]: {response}")
