import socket, json
import time
from Podatak import Option



HOST = 'localhost'
PORT = 50011
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
buffer = list()
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
            time.sleep(1)
            data_encoded = s.recv(4096)
            data_string = data_encoded.decode(encoding="utf-8")
            bufferdba = json.loads(data_string)
            print("Prosecna potrosnja za grad %s po mesecima:"%(city))
            print("(Ukoliko grad ne postoji bice ispisani gradovi koji postoje)")
            for i in bufferdba:
                print(i)
        except:
            break
        #prijem

    elif int(option) == 2 :
        brojilo = input("Unesite id brojila: ")
        try:
            #slanje
            variable = Option(option, brojilo)
            data_as_dict = vars(variable)
            data_string = json.dumps(data_as_dict)
            s.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')
            #prijem
            time.sleep(1)
            data_encoded = s.recv(4096)
            data_string = data_encoded.decode(encoding="utf-8")
            bufferdba = json.loads(data_string)
            print("Prosecna potrosnja za brojilo %d po mesecima:"%(brojilo))
            print("(Ukoliko id brojila ne postoji bice ispisan id brojila koja postoje)")
            for i in bufferdba:
                print(i)
        except:
            break
    else:
        print("Uneta opcija ne postoji!!!")

s.close()


