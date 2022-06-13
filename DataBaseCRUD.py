import mysql.connector
import socket, json
import time
from Podatak import Option
#Ale.01Sto
#klasa za opciju




# DataBase CRUD ce koristiti ovu funkciju za manipulisanje bazom
# F-ja vraca objekat mycur preko kog se izvrsavaju upiti za bazu podataka pomocu metode mycur.execute("Upit")
db = mysql.connector.connect(
    host="localhost",
    user="Aleksa",
    password="Ale.01Sto",
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
#Prvi zahtev izvestaja, potrosnja po mesecima za grad
def consumptionForCity(city):
    bufferAnalitics=list()
    mycur.execute("select Potrosnjabrojila.Mesec, avg(Potrosnjabrojila.Potrosnja) AS ProsecnaPotrosnja " +
                  "from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila " +
                  "where Brojilo.Grad='%s' "%(city) +
                  "group by Potrosnjabrojila.Mesec;")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        bufferAnalitics.append(item)

    return bufferAnalitics

#Drugi zahtev, potrosnja po mesecima za konkretno brojilo
def consumptionForBrojilo(id):
    bufferAnalitics = list()

    mycur.execute("select Potrosnjabrojila.Mesec, Potrosnjabrojila.Potrosnja AS Potrosnja" +
                  " from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila" +
                  " where Brojilo.IDBrojila=%d "%(id) +
                  "group by Potrosnjabrojila.Mesec;")

    while True:
        item = mycur.fetchone()
        if item is None:
            break
        bufferAnalitics.append(item)

    return bufferAnalitics

def currentCities():
    buffer=list()
    mycur.execute("select Grad from Brojilo "
                      "group by Grad;")

    while True:
        item = mycur.fetchone()
        if item is None:
            break
        buffer.append(item)
    return buffer

def currentIds():
    buffer=list()
    mycur.execute("select IDBrojila from Brojilo "
                      "group by IDBrojila;")

    while True:
        item = mycur.fetchone()
        if item is None:
            break
        buffer.append(item)
    return buffer

# parametri za prijem podataka

HOST = 'localhost'
PORT = 50009
bufferCRUD = list()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('DataBaseCRUD started')
print('Waiting for connection...')
conn, addr = s.accept()

print('Connected by', addr)
while True:
    try:
        data_encoded = conn.recv(4096)
        data_string = data_encoded.decode(encoding="utf-8")
        bufferCRUD = json.loads(data_string)
        print('Data received from client')
        for i in bufferCRUD:
            id=int(i["personal_id"])
            value=float(i["monthly_value"])
            insertInDatabase(id, value,"%s" %(i["month"]))

    except:
        break


conn.close()



#parametri za slanje za DataBAse Analitics
def Analitics(option, parametar):
    result = list()
    if option == 1:
        result = consumptionForCity(parametar)
        return result
    elif option == 2 :
        result = consumptionForBrojilo(int(parametar))
        return result

#prijem podataka od Datbase Analitics
PORT2 = 50011
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((HOST, PORT2))
s2.listen(1)
conn, addr = s2.accept()

while True:
    try:
        #prima
        data_encoded = conn.recv(4096)
        data_string = data_encoded.decode(encoding="utf-8")
        data_variable = json.loads(data_string)
        print('Data received from client')
        print(data_variable)
        result = Analitics(int(data_variable["opt"]),data_variable["parametar"])
        #slanje
        if len(result) == 0:
            if int(data_variable["opt"])==1:
                result=currentCities()
                data_string2 = json.dumps(result)
                conn.sendall(data_string2.encode(encoding="utf-8"))
                time.sleep(1)
                print('Data Sent to Server')
            else:
                result=currentIds()
                data_string2 = json.dumps(result)
                conn.sendall(data_string2.encode(encoding="utf-8"))
                time.sleep(1)
                print('Data Sent to Server')
        else:
            data_string2 = json.dumps(result)
            conn.sendall(data_string2.encode(encoding="utf-8"))
            time.sleep(1)
            print('Data Sent to Server')
    except:
        print("Greska")
        break


conn.close()
