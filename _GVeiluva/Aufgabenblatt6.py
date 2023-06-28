# 1 Schreibe eine Funktion (Mit dem Namen add), die zwei Zahlen als Uebergabeparameter hat. Die Funktion soll diese beiden Zahlen addieren und dann das Ergebnis zurueckgeben.
#   Verwende diese Funktion in einem Programm, dass zwei Zahlen einliesst (input), diese Zahlen der Funktion (add) uebergibt und anschliessend das Ergebnis ausgibt (print).
def add(Zahl1, Zahl2):
	return Zahl1 + Zahl2

zahl1=int(input("Gib die erste Zahl ein:"))
zahl2=int(input("Gib die zweite Zahl ein:"))
ergebnis=add(zahl1,zahl2)
print(ergebnis)

# 2 Schreibe eine Funktion, die eine Zahl als Uebergabeparameter hat. Ueberpruefe in der Funktion, ob die Zahl eine Primzahl ist. (Inhalt der Funktion ist in Primzahlen.py-Datei)
#   Kopiere das Programm von Aufgabenblatt5-Aufgabe2 und schreibe es mit deiner neuen Funktion um.
#   Rueckgabeparameter der Funktion soll ein bool sein. (True oder False)
def ist_es_Primzahl(Zahl):
	if Zahl > 1:
		for i in range(2, int(Zahl / 2) + 1):
			if (Zahl % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False

zahl=int(input("Zahl:"))
Ergebnis=ist_es_Primzahl(zahl)
print(Ergebnis)



# 3 Schreibe eine Funktion in einem neuen Programm (neue Datei), die den Rueckgabeparameter der input-Funktion immer in einen int umwandelt.
#   Nenne diese Funktion "input_int".
#   Das verwenden dieser Datei in einem anderem Programm mittels "import Dateiname" am Anfang der Datei. (Achtung: Dateiname ist ein Platzhalter und muss durch den tatsaechlichen Namen der Datei ersetzt werden)
#   Anschliessend kann ein Aufruf der Funktion ueber "Dateiname.Funktionsname" stattfinden.
#   Teste diese Funktion in dem Programm, in dem du Aufgabe 1 und 2 geloest hast. (D.h. die Funktion einmal ausfuehren)

import input
Ergebnis=input.input_int("Gib eine Zahl ein:")
print(Ergebnis)
