import socket, json
from Podatak import Electricity
import time

# lista u koju smestamo podatke tipa Podatak koje salje Writer komponenta
buffer = list(range(10))
buffer.clear()
# parametri za slanje podataka
HOST = 'localhost'
PORT2 = 50056
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST, PORT2))


# fja za slanje podataka na Worker
def sendtoWorker():
    try:
        data_string2 = json.dumps(buffer)
        s2.send(data_string2.encode(encoding="utf-8"))
        time.sleep(1)
        print('Data Sent to Server')
    except:
        print("Error LoadBalancer")


# parametri za prijem podataka
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('LoadBalancer server started:')
print('Waiting for connection...')
conn, addr = s.accept()

print('Connected by', addr)
while True:
    if len(buffer) == 10:
        buffer.clear()
    try:
        data_encoded = conn.recv(4096)
        data_string = data_encoded.decode(encoding="utf-8")
        data_variable = json.loads(data_string)
        # Primljene podatke smestamo u buffer
        buffer.append(data_variable)
        print('Data received from client')
        print(len(buffer))
        # Uslov poziva fje za slanje na Worker
        if len(buffer) == 10:
            sendtoWorker()


    except:
        break

# za manuelni upis podatak
s2.close()
conn.close()
