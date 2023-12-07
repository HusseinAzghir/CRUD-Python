import mysql.connector
import Hauptmaneu
def drop_table():
    while True:
        database = str(input("Geben Sie bitte den Datenbanknamen ein: "))
        import Database
        verbindung = Database.database_zum_bearbeiter(database)
        print("Verbindung mit die {} erfolgreich gestellt.".format(database))
        t_n = input("Geben sie bitte die table name die sie Löschen wollen: ")
        Abfrage = verbindung.cursor()
        Abfrage.execute("DROP TABLE {}".format(t_n))
        if Abfrage:
            print("Tabelle wurde gelöscht")
        else:
            print("Leiedr Kann nicht gelöscht werden")

        Hauptmaneu.checkWeiter_1_database("Databases Löschen")



drop_table()