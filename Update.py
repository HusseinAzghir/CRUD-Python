import Database 
verbindung= Database.database_verbindung()

def update():
    try:
        while True:
            id = int(input("Geben Sie die ID: "))
            produkt_nummer, produkt_name, beschreibung, anzahl, preis = getIdBy(id)

            if checkUpdate("Wollen Sie die Produkt Nummer aktualisieren"):
                produkt_nummer = int(input("Geben Sie die Produkt Nummer: "))
                print()

            if checkUpdate("Wollen Sie den Produkt Namen aktualisieren"):
                produkt_name = input("Geben Sie den Produkt Namen: ")
                print()

            if checkUpdate("Wollen Sie die Produkt Beschreibung aktualisieren"):
                beschreibung = input("Geben Sie die Beschreibung: ")
                print()

            if checkUpdate("Wollen Sie die Anzahl aktualisieren"):
                anzahl = int(input("Geben Sie die Anzahl: "))
                print()

            if checkUpdate("Wollen Sie den Preis aktualisieren"):
                preis = float(input("Geben Sie den Preis: "))
                print()
            
            Abfrag = verbindung.cursor()
            sql = "UPDATE produkte SET produkt_nummer = %s, produkt_name = %s, beschreibung = %s, anzahl = %s, preis = %s WHERE produkt_id = %s"
            values = (produkt_nummer, produkt_name, beschreibung, anzahl, preis, id)

            Abfrag.execute(sql, values)

            verbindung.commit()

            print(Abfrag.rowcount, "record(s) affected")
            import Hauptmaneu
            Hauptmaneu.checkWeiter_1("Updaten")
    except Exception as e:
        print("Fehler:", e)






def getIdBy(id):
    try:
        Abfrag = verbindung.cursor()
        Abfrag.execute("SELECT * FROM produkte WHERE produkt_id = {}".format(id))

        erg = Abfrag.fetchall()
        for x in erg:
            print(x)
        if erg:
            produkt_nummer = erg[0][1]
            produkt_name = erg[0][2]
            beschreibung = erg[0][3]
            anzahl = erg[0][4]
            preis = erg[0][5]

            return produkt_nummer, produkt_name, beschreibung, anzahl, preis
        else:
            print("Produkt mit die ID: {} nicht auf lager".format(id))
            import Hauptmaneu
            Hauptmaneu.hauptmaneu()
            return None, None, None, None, None
    except Exception as e:
        print("Fehler:", e)



def checkUpdate(text):
    print(text)
    print("Bitte wählen.")
    print("[1] Ja")
    print("[2] Nein")
    eingabe = int(input())
   # return eingabe == 1
    if eingabe == 1:
        return True
    else:
        return False
