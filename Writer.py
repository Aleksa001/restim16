from Podatak import Electricity
import socket, json, time, os.path

#Parametri
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def ReadFromFile(nameoffile):
    with open(nameoffile) as f:
        contents = f.readlines()
        count = len(contents)
        i = 0

        while True:
            if i >= count:
                break
            try:
                variable = Electricity(contents[i], contents[i + 1], contents[i + 2])
                # Map your object into dict
                data_as_dict = vars(variable)

                # Serialize your dict object
                data_string = json.dumps(data_as_dict)

                # Send this encoded object
                s.send(data_string.encode(encoding="utf-8"))
                time.sleep(1)
                print('Data Sent to Load Balancer')
            except:
                break

            i = i + 3




# manuelni upis podataka
def ManualInput():
    while True:
        print("Manuelni unos podataka")
        print("Da li zelite da unesete podatke?(unesite da ili ne)")
        request = input()
        if request == 'da':
            id = int(input("ID brojila: "))
            if type(id) != int:
                print("Id mora biti broj!!!")
                continue
            value = float(input("Potrosnja: "))
            if type(value) != float:
                print("Value mora biti broj!!!")
                continue
            month = input("Mesec: ")
        elif request == 'ne':
            break
        else:
            print("Opcija ne postoji!!!")
            continue
        variable = Electricity(id, value, month)
        data_as_dict = vars(variable)
        data_string = json.dumps(data_as_dict)
        s.send(data_string.encode(encoding="utf-8"))
        time.sleep(1)
        print('Data sent from manual input to Load Balancer')


    s.close()

if __name__ == "__main__":
    while True:
        print("Unesite ime fajla: ")
        fileName = input()
        if os.path.exists(fileName):
            break
        print("Izabrani fajl ne postoji!!!")
    ReadFromFile('%s'%(fileName))
    ManualInput()
    print("Writer zavrsio posao!!!")
