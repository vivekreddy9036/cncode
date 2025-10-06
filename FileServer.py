import socket
import os

def file_server():
    host = "127.0.0.1"   # localhost
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is waiting for a client to connect...")

    conn, addr = server_socket.accept()
    print(f"Client connected: {addr}")

    file_name = conn.recv(1024).decode()
    print(f"Client requested file: {file_name}")

    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            file_data = f.read()
            conn.sendall(file_data)
        print(f"File '{file_name}' sent to client.")
    else:
        error_message = "File not found!"
        conn.send(error_message.encode())
        print(f"File not found: {file_name}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    file_server()
