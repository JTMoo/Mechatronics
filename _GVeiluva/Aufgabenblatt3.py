# 1 Erfasse deinen Namen mit einer Benutzereingabe und gebe diesen wieder aus.

# |-------------------------------------------------------------|
# | Schaue dir die Funktion "input" mit help(input) genauer an  |
# | Verwende einen Zeilenumbruch im string mit '\n'             |
# |-------------------------------------------------------------|
name = input("Geb dein Name ein: \n")
print("\n")
print("Dein Name lautet: " + name)

# 2 Passe die 1.Aufgabe in Aufgabenblatt2 so an, dass die Anzahl der Steine von Arbeiter1 als Benutzereingabe erfasst wird. (Bisher immer 25 Steine)
steine = input("Geb die Anzahl der Steine ein: \n")
print("\n")
print("Die Anzahl der Steine lautet: " + steine)
eingabe=input("Gib eine Zahl ein:")
zahl=int(eingabe)
if zahl > 15:
    print("Arbeiter 1 ist schneller")
    zahl=25

else:
    print("Arbeiter 2 ist schneller")
    zahl=15
print(zahl)



#   Bestimme die Anzahl der Steine, bei dem der schnellere Arbeiter wechselt. (Beispiel: Wenn Arbeiter 1 15 Steine am Tag traegt, dann ist er schneller als Arbeiter 2)
eingabe=input("Gib die Zahl ein:")
zahl=int(eingabe)
if zahl < 15:
    print("1° Arbeiter ist schneller")
    zahl=15
else:
    print("2° Arbeiter ist schneller")
    zahl=25
print(zahl)

# 3 Verwende eine Benutzereingabe, um eine Division durchzuführen. (Beispiel: Zahl1 = input und Zahl2 = 21321592 => division = Zahl2 / Zahl1)
zahl1=12
zahl2=4
print(12/4)

zahl1geteiltzahl2 = input("Geb das Resultat ein:\n")
print("\n")
print("Das Resultat lautet:" + zahl1geteiltzahl2)

# 3.1 Muss die Benutzereingabe kontrolliert werden? Wenn ja, warum? (Hier muss nicht programmiert werden)
# Ich würde behaupten, dass ja, um zu sehen, ob es funktioniert.
