# 1 Erfasse deinen Namen mit einer Benutzereingabe und gebe diesen wieder aus.
# |-------------------------------------------------------------|
# | Schaue dir die Funktion "input" mit help(input) genauer an  |
# | Verwende einen Zeilenumbruch im string mit '\n'             |
# |-------------------------------------------------------------|
Name=input("Gebe deinen Namen ein: \n")
print("\n")
print("Dein Name lautet: " + Name)

# 2 Passe die 1.Aufgabe in Aufgabenblatt2 so an, dass die Anzahl der Steine als Benutzereingabe definiert ist.
steine=input("Geb die Anzahl der Steine ein: \n")
print("\n")
print ("Die Anzahl der steine lautet: " + steine)
eingabe=input("Gib eine Zahl ein: ")
zahl=int(eingabe)
if zahl > 15:
    print("Arbeiter 1 ist schneller")
    zahl=25

else:
    print("Arbeiter 2 ist schneller")
    zahl=0
print(zahl)

#   Bestimme die Anzahl der Steine, bei dem der schnellere Arbeiter wechselt. (Beispiel: Wenn Arbeiter 1 15 Steine am Tag traegt, dann ist er schneller als Arbeiter 2)
eingabe=input("Gib die Zahl ein:")
zahl=int(eingabe)
if zahl < 15:
    print("1ter Arbeiter ist schneller")
    zahl=15
else:
    print("2ter Arbeiter ist schneller")
    zahl=25
print(zahl)


# 3 Verwende eine Benutzereingabe, um eine Division durchzuführen.
#eingabe=input("Geb eine Zahl ein")
zahl1=12
zahl2=4
print(12/4)

Zahl1geteiltZahl2=input("Geb das Resultat ein: \n")
print("\n")
print("Das Resultat lautet:" + Zahl1geteiltZahl2)


# 3.1 Muss die Benutzereingabe kontrolliert werden? Wenn ja, warum? (Hier muss nicht programmiert werden)
# Ich glaube ja, da man sehen muss ob es richtig ist.
