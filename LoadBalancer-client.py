# LoadBalancer-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    s.connect((HOST, 65432))
    s.sendall(data)
    data = s.recv(1024)

print(f"Received {data!r}")