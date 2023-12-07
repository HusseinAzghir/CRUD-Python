import Database 
verbindung= Database.database_verbindung()

def insert():
    try:
        while True:
            import Hauptmaneu 
            p_n = int(input("geben Sie die Produktnummer: "))
            p_name = input("geben Sie den Produktnamen: ")
            p_b = input("geben Sie die Beschreibung: ")
            p_a = int(input("geben Sie die Anzahl: "))
            p_p = float(input("geben Sie den Preis: "))
            Abfrage = verbindung.cursor()
            sql = "INSERT INTO produkte (produkt_nummer, produkt_name, beschreibung, anzahl, preis) VALUES (%s, %s, %s, %s, %s)"
            val = (p_n, p_name, p_b, p_a, p_p)
            Abfrage.execute(sql, val)
            verbindung.commit()
            print(Abfrage.rowcount, "wurde eingefügt.")
            Hauptmaneu.checkWeiter_1("einfügen")
    except Exception as ex:
        print("Fehler: ", ex)


