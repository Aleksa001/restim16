from Podatak import Electricity
import socket, json
import time
HOST = 'localhost'
PORT = 50007
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with open('StrujaFile.txt') as f:
    contents = f.readlines()
    count = len(contents)
    i = 0

    while True:
        if i >= count:
            break
        try:
            variable = Electricity(personal_id=contents[i], monthly_value=contents[i + 1], month=contents[i + 2])
            # Map your object into dict
            data_as_dict = vars(variable)

            # Serialize your dict object
            data_string = json.dumps(data_as_dict)

            # Send this encoded object
            s.send(data_string.encode(encoding="utf-8"))
            time.sleep(1)
            #
            print('Data Sent to Server')
        except:
            break

        i = i+3


s.close()