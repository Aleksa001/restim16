import json
import random
import socket
import threading
import time

HOST = 'localhost'
PORT2 = 50009
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def ClientThread(bufferworker):
            s2.connect((HOST, PORT2))
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
while True:
    s.listen(1)
    conn, addr = s.accept()
    data_encoded = conn.recv(4096)
    data_string = data_encoded.decode(encoding="utf-8")
    bufferworker = json.loads(data_string)
    threads[counter] = threading.Thread(target=ClientThread(bufferworker))
    print(threads[counter].native_id)
    counter = counter + 1
    if counter > len(threads) - 1:
        counter = 0
    threads[counter].start()

s2.close()
