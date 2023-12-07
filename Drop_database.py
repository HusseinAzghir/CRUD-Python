import mysql.connector
import Database

def drop_database():
      try:
          while True:
               database = str(input("Geben Sie bitte  den Datenbanknamen die gelöscht wwird ein_______: "))
               host = str(input("Geben Sie bitte den Host ein_______: "))
               user = str(input("Geben Sie bitte den Username ein_______: "))
               passwort = str(input("Geben Sie bitte den Password ein_______: "))
               verbindung = Database.database_Create(host,user,passwort)
               sql = "DROP DATABASE {}".format(database)
               Abfrage = verbindung.cursor()
               Abfrage.execute(sql)
               if sql:
                    print(database , " Database wurde gelöscht.")

               import Hauptmaneu
               Hauptmaneu.checkWeiter_1_database("Dropen.")
      except Exception as ex:
           print("Fehler:" ,ex)
