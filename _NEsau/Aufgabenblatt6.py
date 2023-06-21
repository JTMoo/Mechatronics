# 1 Schreibe eine Funktion (Mit dem Namen add), die zwei Zahlen als Uebergabeparameter hat. Addiere diese beiden Zahlen und gebe das Ergebnis zurueck.
#   Verwende diese Funktion in einem Programm, dass zwei Zahlen einliesst (input), diese Zahlen der Funktion (add) uebergibt und anschliessend das Ergebnis ausgibt (print).
def add(text):
    z=input(text)
    print("Aufgabe")

A=int(input("Gib eine Zahl: "))
B=int(input("Noch eine Zahl: "))
Zahl6=add(A + B)
print(type(Zahl6))
print(Zahl6)


# 2 Schreibe eine Funktion, die eine Zahl als Uebergabeparameter hat. Ueberpruefe in der Funktion, ob die Zahl eine Primzahl ist. (Inhalt der Funktion ist in Primzahlen.py-Datei)
#   Kopiere das Programm von Aufgabenblatt5-Aufgabe2 und schreibe es mit deiner neuen Funktion um.
#   Rueckgabeparameter der Funktion soll ein bool sein. (True oder False)
def Ist_Zahl_Primzahl(Zahl5):
    if Zahl5 > 1:
	    for i in range(2, int(Zahl5 / 2) + 1):
		    if (Zahl5 % i) == 0:
			    return False
	    else:
		    return True
    else:
	    return False
    
Zahl5=int(input("Zahl1: "))
ergebnis1=Ist_Zahl_Primzahl(Zahl5)
print(ergebnis1)




# 3 Schreibe eine Funktion in einem neuen Programm (neue Datei), die den Rueckgabeparameter der input-Funktion immer in einen int umwandelt.
#   Nenne diese Funktion "input_int".
#   Das verwenden dieser Datei in einem anderem Programm mittels "import Dateiname" am Anfang der Datei. (Achtung: Dateiname ist ein Platzhalter und muss durch den tatsaechlichen 
#   Namen der Datei ersetzt werden)
#   Anschliessend kann ein Aufruf der Funktion ueber "Dateiname.Funktionsname" stattfinden.
#   Teste diese Funktion in dem Programm, in dem du Aufgabe 1 und 2 geloest hast. (D.h. die Funktion einmal ausfuehren)

import Input
Antwort=Input.input_int("Eine Zahl1: ")
print(Antwort)



