
import Hauptmaneu
import mysql.connector


def craete_columen():
    try:
        while True:
            database = input("Geben sie die Database Name: ")
            import Database
            verbindung = Database.database_zum_bearbeiter(database)
            Abfrage = verbindung.cursor()
            eingabe_1 = input("in welche Tabelle wollen sie Spalten erstellen: ")
            eingabe_2 = input("geben sie bitte Spalten name und Datentyp es darf nur ein Spalte erstellt werden (z.b eingabe [Email varchar(255),id INT AUTO_INCREMENT PRIMARY KEY]): \n")
            sql = "ALTER TABLE {} ADD {}".format(eingabe_1, eingabe_2)
            Abfrage.execute(sql)
            verbindung.commit()
            print( eingabe_2," wurde erstellt.")
            Hauptmaneu.checkWeiter_1_database("Spalten einfügen")
    except Exception as ex:
        print("Fehler: ", ex)
