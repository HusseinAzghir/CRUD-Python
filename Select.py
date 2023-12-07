
import Database 


def select():
    try:
        verbindung= Database.database_verbindung()
        verbindung._open_connection()
        Abfrage = verbindung.cursor()
        Abfrage.execute("SELECT * FROM produkte")
        erg = Abfrage.fetchall()
        print("ID  ||  PRODUKT NUMMER  ||  PRODUKT NAME  ||  BESCHREIBUNG  ||  ANZAHL  ||   PREIS €")

        for x in erg:
            print(x)
            
        import Hauptmaneu
        Hauptmaneu.checkWeiter_2()
        Abfrage.close()
        verbindung.close()
    except Exception as ex:
        print("Fehler: ", ex)
            

                 



