import socket, json
import time
from Podatak import Option



HOST = 'localhost'
#prijem podataka
PORT2 = 50012
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s2.bind((HOST, PORT2))
print("Server started")
print("Waiting for client request..")
s2.listen(1)
conn, addr = s2.accept()
#slanje
PORT = 50011
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
buffer=list()
while True:
    print("Izaberite izvestaj:")
    print("1.Potrosnja po mesecima za odredjeni grad")
    print("2.Potrosnja po mesecima za konkretno brojilo")
    option=input("Unesite opciju 1 ili 2: ")
    if int(option) == 1 :
        city = input("Unesite ime grada: ")
        try:
            variable = Option(option,city)
            data_as_dict = vars(variable)
            data_string = json.dumps(data_as_dict)
            s.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')
            #ovde prima podatke
            data_encoded = conn.recv(4096)
            data_string = data_encoded.decode(encoding="utf-8")
            bufferdba = json.loads(data_string)
            for i in bufferdba:
                print(i)
        except:
            break
        #prijem

    elif int(option) == 2 :
        brojilo = input("Unesite id brojila: ")
        try:
            variable = Option(option, brojilo)
            data_as_dict = vars(variable)
            data_string = json.dumps(data_as_dict)
            s.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')
            data_encoded = conn.recv(4096)
            data_string = data_encoded.decode(encoding="utf-8")
            bufferdba = json.loads(data_string)
            for i in bufferdba:
                print(i)
        except:
            break
    else:
        print("Uneta opcija ne postoji!!!")

s.close()


