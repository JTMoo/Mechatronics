# 1 Schreibe ein Programm, das alle Zahlen zwischen 1 und der einer vom Benutzer definierten Zahl (input) ausgibt.
#   Achtung: Fehlerfaelle beruecksichtigen (Bedingungen)
y=input("Gib eine Zahl ein:")
y=int(y)
for zahl in range(1,y):
    print(zahl)

if zahl > 0:
    print("funktioniert es")
else:
    print("funktioniert es nicht")

# 2 Schreibe ein Programm, das alle Primzahlen zwischen 1 und 1000 ausgibt.
#   Primzahlen sind so definiert, dass sie nur durch sich selbst und 1 teilbar sind. Beispiel: 1, 2, 3, 5, 7 ....
Zahl = 1000
Liste=[]
Liste=range(Zahl)
for number in Liste:
	

	numberToCheck=number

	if numberToCheck > 1:
		for i in range(2, int(numberToCheck / 2) + 1):
			if (numberToCheck % i) == 0:
				break
		else:
			print(numberToCheck, "ist eine Primzahl")

# 3 Schreibe ein Programm, das alle Zeichen eines Benutzer-definierten (input) strings (Bedingung) in jeweils einer Zeile ausgibt.
Zeichen = input("Gib ein Zeichen ein:\n")
print("\n")
for einzeln in Zeichen:
	print(einzeln)
