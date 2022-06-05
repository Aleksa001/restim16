import mysql.connector

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
        mycur.execute("INSERT INTO Potrosnjabrojila (IDBrojila, Potrosnja, Mesec) VALUES (%d, %f, '%s')" %(id,value,month))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()

def deletefromDatabase(id):
    try:
        mycur.execute("DELETE from Potrosnjabrojila where IDBrojila=%d" %(id))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()

def updateInDatabase(id,value,month):
    try:
        mycur.execute("Update Potrosnjabrojila set Potrosnja= %f where IDBrojila= %d && Mesec='%s'" %(value,id,month))
        db.commit()
    except:
        print("Error in operation!!!")
        db.rollback()


def readAllInDatabase():
    mycur.execute("SELECT * FROM Potrosnjabrojila")
    while True:
        item=mycur.fetchone()
        if item==None:
            break
        print(item)



