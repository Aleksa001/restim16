import socket, json, time
from Podatak import Option

# Parametri
HOST = 'localhost'
PORT = 50023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
buffer = list()


def ReportFromDatabase():
    while True:
        print("Izaberite izvestaj:")
        print("1.Potrosnja po mesecima za odredjeni grad")
        print("2.Potrosnja po mesecima za konkretno brojilo")
        print("3.Exit")
        option = input("Unesite opciju: ")
        if int(option) == 1:
            city = input("Unesite ime grada: ")
            try:
                variable = Option(option, city)
                data_as_dict = vars(variable)
                data_string = json.dumps(data_as_dict)
                s.send(data_string.encode(encoding="utf-8"))
                time.sleep(1)
                print('Data Sent to DatabaseCRUD')
                # ovde prima podatke
                time.sleep(1)
                data_encoded = s.recv(4096)
                data_string = data_encoded.decode(encoding="utf-8")
                bufferdba = json.loads(data_string)

            except:
                break
            print("Prosecna potrosnja za grad %s po mesecima:" % (city))
            print("(Ukoliko grad ne postoji bice ispisani gradovi koji postoje u bazi!!!)")
            for i in bufferdba:
                print(i)


        elif int(option) == 2:
            brojilo = input("Unesite id brojila: ")
            try:
                # slanje
                variable = Option(option, brojilo)
                data_as_dict = vars(variable)
                data_string = json.dumps(data_as_dict)
                s.send(data_string.encode(encoding="utf-8"))
                time.sleep(1)
                print('Data Sent to DatabaseCRUD')
                # prijem
                time.sleep(3)
                data_encoded = s.recv(4096)
                data_string = data_encoded.decode(encoding="utf-8")
                bufferdba = json.loads(data_string)
            except:
                break
            print("Prosecna potrosnja za brojilo %d po mesecima:" % (int(brojilo)))
            print("(Ukoliko id brojila ne postoji bice ispisan id brojila koja postoje u bazi!!!)")
            for i in bufferdba:
                print(i)
        elif int(option) == 3:
            break
        else:
            continue

    s.close()


if __name__ == "__main__":
    ReportFromDatabase()
    print("Zavrseno listanje izvestaja!!!")
