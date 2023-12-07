def create_tabllen_spalten():
    try:
        while True:
            database = input("Geben sie die Database Name: ")
            import Database
            verbindung =  Database.database_zum_bearbeiter(database)
            Abfrage = verbindung.cursor()
            T_name = input("geben sie die Tablle name: ")
            spalten_erstellen  = input("Sie sollen ein oder mehrer Splaten ersten z.b(id INT AUTO_INCREMENT PRIMARY KEY,Spalten_N VARCHAR(255), Spalten_N VARCHAR(255)): \n")
            sql ="CREATE TABLE {} ({})".format(T_name,spalten_erstellen)  
            Abfrage.execute(sql)
            print("wurde erstellt.")

            import Hauptmaneu
            Hauptmaneu.checkWeiter_1_database("Tabellen erstellen.")
    except Exception as ex:
        print("Fehler:" , ex)


