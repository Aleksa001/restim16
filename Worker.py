import socket, json
from Podatak import Electricity

HOST = 'localhost'
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:
    try:
        data_encoded = conn.recv(4096)
        data_string = data_encoded.decode(encoding="utf-8")
        data_variable = json.loads(data_string)
        print(data_variable)
    except:
        break

conn.close()