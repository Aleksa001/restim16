import socket, json
from Podatak import Electricity
import time

# lista u koju smestamo podatke tipa Podatak koje salje Writer komponenta
buffer = list(range(10))
buffer.clear()
#parametri za slanje podataka
HOST = 'localhost'
PORT2 = 50008
# Create a socket connection.
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST, PORT2))

#fja za slanje podataka na Worker
def sendtoWorker():
    for i in buffer:
        try:
            #ovde nekgde greska ne znam koja

            data_as_dict = vars(i)

            # Serialize your dict object
            data_string = json.dumps(data_as_dict)

            # Send this encoded object
            s2.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')
            counter = counter+1
        except:
            print("Neka greska")
            break


    s2.close()
    print("Zavrsio fju")





#parametri za prijem podataka

PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()


print('Connected by', addr)
while True:
    if len(buffer)== 10:
        buffer.clear()
    try:
        data_encoded = conn.recv(4096)
        data_string = data_encoded.decode(encoding="utf-8")

        data_variable = json.loads(data_string)
        # data_variable is a dict representing your sent object
        #print(data_variable)

        #Primljene podatke smestamo u buffer
        print(data_variable)
        buffer.append(data_variable)
        print('Data received from client')
        print(len(buffer))
        #Uslov poziva fje za slanje na Worker
        if len(buffer) == 10:
            sendtoWorker()


    except:
        #print(ConnectionAbortedError)
        break

conn.close()



