import Database 
verbindung= Database.database_verbindung()
import Hauptmaneu
import Update



def delete():
        try:
         while True:
                id = int(input("Geben Sie die ID: "))
                Update.getIdBy(id)
                mycursor = verbindung.cursor()
                sql ="DELETE from produkte WHERE produkt_id=%s"
                value = (id,)
                mycursor.execute(sql,value)
                verbindung.commit()
                print(mycursor.rowcount, "record(s) deleted")
                Hauptmaneu.checkWeiter_1("Löschen")
        except Exception as ex:
                 print("Fehler: " ,ex)
        
