from Podatak import Electricity

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


with open('StrujaFile.txt') as f:
    contents = f.readlines()
    count = len(contents)
    i = 0

    while 1 > 0:
        if i == count:
            break
        one = Electricity(personal_id=contents[i], monthly_value=contents[i + 1], month=contents[i + 2])
        #ovde salje LB-u podatke
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(one)

        i = i+3


