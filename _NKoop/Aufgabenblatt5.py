# 1 Schreibe ein Programm, das alle Zahlen zwischen 1 und der einer vom Benutzer definierten Zahl (input) ausgibt.
#   Achtung: Fehlerfälle berücksichtigen (Bedingungen)
Zahl1 = 1
Zahl2 = int(input("Gib eine Zahl ein : \n"))
Liste = list(range(Zahl2))
print(Liste)
    
# 2 Schreibe ein Programm, das alle Primzahlen zwischen 1 und 1000 ausgibt.
#   Primzahlen sind so definiert, dass sie nur durch sich selbst und 1 teilbar sind. Beispiel: 1, 2, 3, 5, 7 ....
for numberToCheck in range(1, 1000):
	if numberToCheck > 1:
		for i in range(2, int(numberToCheck / 2) + 1):
			if (numberToCheck % i) == 0:
				break
		else:
			print(numberToCheck, "ist eine Primzahl")
	else:
		print(numberToCheck, "ist keine Primzahl")

# 3 Schreibe ein Programm, das alle Zeichen eines Benutzer-definierten (input) strings (Bedingung) in jeweils einer Zeile ausgibt.
#Liste = list()
Benutzereingabe = str(input("Gib deinen Namen ein: \n"))
print("/n")
for element in Benutzereingabe:
	print(element)

#---------------------------------------------------------------------------------------notes
#for element in range(0,10):
#    if element == 3:
#        print(element)
#        print("x")
#---------------------------------------------------------------------------------------notes
#def input_int(text):
#	neuer_Text = int(input(text))
#	print("Test")
#	return(neuer_Text)
#
#zahl = input_int("Gib eine Zahl ein")
#print(type(zahl))
#---------------------------------------------------------------------------------------notes
#def add(a):
#	return a / 10
#import (Name der Datei)
#x = 100
#ergebnis = helper.add(x)
#print(ergebnis)