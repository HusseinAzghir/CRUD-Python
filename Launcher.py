import Update
import Database


def myprogramm():

    print("______________________________________________________________ Willkommen in SQL mit Python __________________________________________________________________")
    print()
    print("Bitte Wählen.")
    print("[1] CRUD mit Python.")
    print("[2] Database bearbeiten mit Python.")
    eingabe = int(input())
    match eingabe:
        case 1:
            import Hauptmaneu
            Hauptmaneu.hauptmaneu()
        case 2:
            import Hauptmaneu
            Hauptmaneu.Database_bearbeiten()


myprogramm()
