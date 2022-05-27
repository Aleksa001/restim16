import mysql.connector



#DataBase CRUD ce koristiti ovu funkciju za manipulisanje bazom
#F-ja vraca objekat mycur preko kog se izvrsavaju upiti za bazu podataka pomocu metode mycur.execute("Upit")
def connection():
    db = mysql.connector.connect(
        host="localhost",
        user="Aleksa",
        password="Ale.01Sto",
    )
    mycur = db.cursor()

    return mycur
