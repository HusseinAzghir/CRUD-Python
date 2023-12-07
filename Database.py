import mysql.connector


def database_verbindung():
    try:
        verbindung = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "myshop"
        )
        return verbindung
        print("Verbindung wurde gestellt....")
    except Exception as ex:
        print("Fehler: " , ex)

  


def database_zum_bearbeiter(db):
    try:
        global  verbindung 
        verbindung = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "{}".format(db)
        )
        return verbindung
        print("Verbindung mit {} wurde gestellt....".format(db))
    except Exception as ex:
        print("Fehler: " , ex)
     
def database_Create(h,u,p):
    try:
        verbindung = mysql.connector.connect(
        host = "{}".format(h),
        user = "{}".format(u),
        password = "{}".format(p))
        return verbindung
    except Exception as ex:
        print(ex)

