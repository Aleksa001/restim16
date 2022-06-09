import mysql.connector
import socket, json

# DataBase CRUD ce koristiti ovu funkciju za manipulisanje bazom
# F-ja vraca objekat mycur preko kog se izvrsavaju upiti za bazu podataka pomocu metode mycur.execute("Upit")
db = mysql.connector.connect(
    host="localhost",
    user="Aleksa",
    password="Ale.01Sto",
    database="Projekat"
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
    mycur.execute("select Potrosnjabrojila.Mesec, avg(Potrosnjabrojila.Potrosnja) AS ProsecnaPotrosnja " +
                  "from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila " +
                  "where Brojilo.Grad='%s' "%(city) +
                  "group by Potrosnjabrojila.Mesec ;")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        print(item)

#Drugi zahtev, potrosnja po mesecima za konkretno brojilo
def consumptionForBrojilo(id):
    mycur.execute("select Potrosnjabrojila.Mesec, avg(Potrosnjabrojila.Potrosnja) AS Potrosnja" +
                  " from  Brojilo inner join Potrosnjabrojila " +
                  "on Brojilo.IDBrojila=Potrosnjabrojila.IDBrojila" +
                  " where Brojilo.IDBrojila=%d "%(id) +
                  "group by Potrosnjabrojila.Mesec ;")
    while True:
        item = mycur.fetchone()
        if item is None:
            break
        print(item)

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
            #print("from client", i["personal_id"], i["monthly_value"], i["month"])
            id=int(i["personal_id"])
            value=float(i["monthly_value"])
            insertInDatabase(id, value,"%s" %(i["month"]))

    except:
        break

conn.close()



