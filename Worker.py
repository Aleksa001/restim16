import json
import random
import socket
import threading
import time

HOST = 'localhost'
PORT2 = 50009


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", addr)
        while True:
            data_encoded = conn.recv(4096)
            data_string = data_encoded.decode(encoding="utf-8")
            bufferworker = json.loads(data_string)

            s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s2.connect((HOST, PORT2))
            data_string2 = json.dumps(bufferworker)
            s2.send(data_string2.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')

            s2.close()


bufferworker = list()
countofinstance = random.randint(2, 6)

HOST = "localhost"
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    s.listen(1)
    conn, addr = s.accept()
    newthread = ClientThread(addr, conn)
    newthread.start()
