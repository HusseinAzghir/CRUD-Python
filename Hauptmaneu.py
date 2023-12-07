
def hauptmaneu():
  
  print("BItte wählen sie ein.")
  print("[1] Insert.")
  print("[2] Select.")
  print("[3] Delete.")
  print("[4] Update.")
  print("[5] zum Hauptprogramm.")
  print("[6] Exit.")
  eingabe = int(input())

  match eingabe:
      case 1:
        import Insert
        Insert.insert()
      case 2:
          import Select
          Select.select()
      case 3:
          import Delete
          Delete.delete()
      case 4:
        import Update
        Update.update()
      case 5:
        import Launcher
        Launcher.myprogramm()
      case 6:
        exit(0)
      


def Database_bearbeiten():
  print("BItte wählen sie ein.")
  print("[1] Create Database.")
  print("[2] Create Table and Columen.")
  print("[3] Create Just Columen")
  print("[4] Drop Table.")
  print("[5] Drop Database.")
  print("[6] Zum Hauptprogramm.")
  print("[7] Exit.")
  eingabe_2 = int(input())

  match eingabe_2:
    case 1:
      import Create_Database
      Create_Database.craete_database()
    case 2:
      import Create_Table1
      Create_Table1.create_tabllen_spalten()
    case 3:
        import Create_Columen
        Create_Columen.craete_columen()
    case 4:
        import Drop_Table
        Drop_Table.drop_table()
    case 5:
        import Drop_database
        Drop_database.drop_database()
    case 6:
        import Launcher
        Launcher.myprogramm()
    case 7:
        exit(0)
        
      
        
        

def  checkWeiter_2():
  print("Bitte Wählen.")
  print("[1] Zum Hauptmenü.")
  print("[2] Exit")
  eingabe = int(input())
  if eingabe == 1:
    hauptmaneu()
  elif eingabe == 2:
    exit(0)


def checkWeiter_1(text):
  print("Bitte Wählen.")
  print("[1] Weiter {}.".format(text))
  print("[2] Zum Hauptmenü.")
  print("[3] Exit")
  eingabe = int(input())
  if eingabe == 1:
     True
  elif eingabe == 2:
     hauptmaneu()
  else:
     exit(0)


def checkWeiter_1_database(text):
  print("Bitte Wählen.")
  print("[1] Weiter {}.".format(text))
  print("[2] Zum Hauptmenü.")
  print("[3] Exit")
  eingabe = int(input())
  if eingabe == 1:
     True
  elif eingabe == 2:
     Database_bearbeiten()
  else:
     exit(0)


