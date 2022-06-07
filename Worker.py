import json
import random
import socket
import threading


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
            for i in bufferworker:
                print("from client", i["personal_id"], i["monthly_value"], i["month"])
        print("Client at ", addr, " disconnected...")


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
