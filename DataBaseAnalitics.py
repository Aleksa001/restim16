import socket, json
import time

HOST = 'localhost'
PORT = 50010
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    print("Izaberite izvestaj:")
    print("1.Potrosnja po mesecima za odredjeni grad")
    print("2.Potrosnja po mesecima za konkretno brojilo")
    option=input("Unesite opciju 1 ili 2: ")
    if int(option) == 1 :
        try:
            s.sendall(option)
            time.sleep(1)
            print('Data Sent to Server')
        except:
            break
        #prijem

    elif int(option) == 2 :
        try:

            # Map your object into dict
            data_as_dict = vars(option)

            # Serialize your dict object
            data_string = json.dumps(data_as_dict)

            # Send this encoded object
            s.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            #
            print('Data Sent to Server')
        except:
            break
    else:
        print("Uneta opcija ne postoji!!!")




