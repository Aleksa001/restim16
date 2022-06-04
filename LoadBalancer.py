
import socket, json

# lista u koju smestamo podatke tipa Podatak koje salje Writer komponenta
buffer = list(range(10))

HOST = 'localhost'
PORT = 50007
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
        # data_variable is a dict representing your sent object
        #print(data_variable)

        #Primljene podatke smestamo u buffer
        buffer.append(data_variable)
    except:
        #print(ConnectionAbortedError)
        break
    print('Data received from client')
conn.close()

