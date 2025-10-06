import socket

def file_client():
    host = "127.0.0.1"   # server IP (localhost)
    port = 8000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to the server.")

    file_name = input("Enter the filename you want to download: ")
    client_socket.send(file_name.encode())

    file_data = client_socket.recv(4096)

    if b"File not found" not in file_data:
        with open("Downloaded_" + file_name, "wb") as f:
            f.write(file_data)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(file_data.decode())

    client_socket.close()

if __name__ == "__main__":
    file_client()
