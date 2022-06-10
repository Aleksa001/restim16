import json
import random
import socket
import threading
import time

HOST = 'localhost'
PORT2 = 50009
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST, PORT2))


def ClientThread(bufferworker):
    data_string2 = json.dumps(bufferworker)
    s2.send(data_string2.encode(encoding="utf-8"))
    time.sleep(1)
    print('Data Sent to Server')


bufferworker = list()
countofinstance = random.randint(2, 3)
threads = []
for i in range(countofinstance):
    thread = threading.Thread()
    threads.append(thread)

counter = 0

HOST = "localhost"
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
s.listen(1)
conn, addr = s.accept()
while True:
    data_encoded = conn.recv(4096)
    data_string = data_encoded.decode(encoding="utf-8")
    bufferworker = json.loads(data_string)
    threads[counter] = threading.Thread(target=ClientThread(bufferworker))
    counter = counter + 1
    if counter > len(threads) - 1:
        counter = 0
    threads[counter].start()
    print(threading.current_thread().name)
    print(threading.active_count())
s2.close()
