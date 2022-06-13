import random
import socket
import threading
import time

countOfInstance = random.randint(9, 10)
threads = []
condition = threading.Condition
HOST = "localhost"
PORT = 50008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
s.listen(1)
conn, addr = s.accept()
print("Connected by", addr)


def Worker():
    PORT2 = 50008
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect((HOST, PORT2))

    while True:
        try:
            for name in names.keys():
                if name == threading.current_thread().name:
                    condition.wait(1000)

            data_encoded = conn.recv(4096)
            s2.sendall(data_encoded)
            print('Data Sent to Server by', threading.current_thread().name)

        except:
            break

    conn.close()


def ThreadFactory():
    counter = 0
    while counter < len(threads):
        threads[counter].start()
        counter = counter + 1


names = dict()


def StopThreads():
    number = 0
    while True:
        answer = input('Would you like to stop any threads? (y/n)').lower()
        if answer == 'y':
            chosenThread = input('Choose what thread to stop')
            names[chosenThread] = number
            number = number + 1
        else:
            break


print("List of WORKERS you can choose from")
for i in range(countOfInstance):
    thread = threading.Thread(target=Worker)
    threads.append(thread)
    print(threads[i].name)
StopThreads()
ThreadFactory()
time.sleep(1)
for j in range(len(threads)):
    print(threads[j].name, threads[j].is_alive())





