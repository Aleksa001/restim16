from Podatak import Electricity

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

#lista u koju smestamo podatke tipa Podatak koje salje Writer komponenta
buffer = list(range(10))



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(Electricity)
            print(data)
            if not data:
                break




