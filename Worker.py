import random
import socket, json, time, _thread
import  DataBaseCRUD
from Podatak import Electricity
bufferworker=list()
countofinstance=random.randint(2,6)

HOST="localhost"
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
        bufferworker = json.loads(data_string)
        for i in bufferworker:
            print(getattr(i))
    except:
        break

conn.close()
