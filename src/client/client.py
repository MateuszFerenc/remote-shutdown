import socket

host = "localhost"
port = 21037

if __name__ == "__main__": 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sfd:
        sfd.connect((host, port))
        sfd.sendall(b"author")
        data = sfd.recv(64)

    print(f"Received {data!r}")
