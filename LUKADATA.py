import mysql.connector
import socket, json
import threading

# Ale.01Sto
# DataBase CRUD ce koristiti ovu funkciju za manipulisanje bazom
# F-ja vraca objekat mycur preko kog se izvrsavaju upiti za bazu podataka pomocu metode mycur.execute("Upit")
db = mysql.connector.connect(
    host="localhost",
    user="Luka",
    password="5628460460Aa",
    database="projekat"
)
mycur = db.cursor()


def insertInDatabase(id, value, month):
    try:
        mycur.execute(
            "INSERT INTO Potrosnjabrojila (IDBrojila, Potrosnja, Mesec) VALUES (%d, %f, '%s')" % (id, value, month))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()


def deleteFromDatabase(id):
    try:
        mycur.execute("DELETE from Potrosnjabrojila where IDBrojila=%d" % (id))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()


def updateInDatabase(id, value, month):
    try:
        mycur.execute(
            "Update Potrosnjabrojila set Potrosnja= %f where IDBrojila= %d && Mesec='%s'" % (value, id, month))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()


def readAllInDatabase():
    mycur.execute("SELECT * FROM Potrosnjabrojila")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        print(item)


# Prvi zahtev izvestaja, potrosnja po mesecima za grad
def consumptionForCity(city):
    bufferAnalitics = list()
    mycur.execute("select Potrosnjabrojila.Mesec, avg(Potrosnjabrojila.Potrosnja) AS ProsecnaPotrosnja " +
                  "from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila " +
                  "where Brojilo.Grad='%s' " % (city) +
                  "group by Potrosnjabrojila.Mesec ;")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        bufferAnalitics.append(item)

    return bufferAnalitics


# Drugi zahtev, potrosnja po mesecima za konkretno brojilo
def consumptionForBrojilo(id):
    bufferAnalitics = list()
    mycur.execute("select Potrosnjabrojila.Mesec, avg(Potrosnjabrojila.Potrosnja) AS Potrosnja" +
                  " from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila" +
                  " where Brojilo.IDBrojila=%d " % (id) +
                  "group by Potrosnjabrojila.Mesec ;")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        bufferAnalitics.append(item)

    return bufferAnalitics


# parametri za prijem podataka


bufferCRUD = list()


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", clientAddress)
        # self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            try:
                data_encoded = self.csocket.recv(4096)
                data_string = data_encoded.decode(encoding="utf-8")
                bufferCRUD = json.loads(data_string)
                print('Data received from client')
            except:
                continue
            for i in bufferCRUD:
                # print("from client", i["personal_id"], i["monthly_value"], i["month"])
                id = int(i["personal_id"])
                value = float(i["monthly_value"])
                insertInDatabase(id, value, "%s" % (i["month"]))
        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 50009
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
    print(threading.active_count())
