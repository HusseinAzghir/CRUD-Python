

def craete_database():
    try:
        host = str(input("Geben Sie bitte den Host ein_______: "))
        user = str(input("Geben Sie bitte den Username ein_______: "))
        passwort = str(input("Geben Sie bitte den Password ein_______: "))
        database = str(input("Geben Sie bitte den Datenbanknamen ein_______: "))
        import Database
        verbindung = Database.database_Create(host, user, passwort)
        Abfrage = verbindung.cursor()
        sql = "CREATE DATABASE {}".format(database)
        Abfrage.execute(sql)
        print("Database: {} wurde erstellt.".format(database))
        Weiter()
    except Exception as ex:
        print(ex)



def Weiter():
        print("Bitte Wählen.")
        print("[1] Tabllen und Spalten erstellen.")
        print("[2] Zum Hauütmenü.")
        print("[3] Drop Database")
        print("[Anykey] Exit")
        eingabe = int(input())
        if eingabe == 1:
            import Create_Table1
            Create_Table1.create_tabllen_spalten()
        elif eingabe == 2:
            import Hauptmaneu
            Hauptmaneu.hauptmaneu()
        elif eingabe == 3:
            import Drop_database
            Drop_database.drop_database()
        else:
            exit(0)
    