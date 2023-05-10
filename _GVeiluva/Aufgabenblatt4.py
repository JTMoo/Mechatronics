# 1 Wenn bei der Division (Teilen) der 3. Aufgabe, die eingelesene Zahl im Nenner steht (eingelesene_Zahl = input().... div = Zahl2 / eingelesene_Zahl), 
#   in welchem Fall schlaegt die Division dann fehl?
zahl2 = 12
eingelesene_Zahl = input("Gebe eine Zahl ein:")
div = zahl2 / int(eingelesene_Zahl)
print("Das Resultat lautet:" + str(div))
# Wenn man (str) und (int) nicht richtig in der Aufgabe eingibt.

#   Wie kann durch eine Bedingung, dieser Fall verhindert werden?
#   Schreibe dieses Programm.
zahl2 = 12
if zahl2 < 100:
    print("Ist es wahr")
else:
    print("Ist es falsch")

# 2 Schreibe ein Programm, dass eine (beliebige) Frage ausgibt und dann eine Antwort des Benutzers abwartet.
#   Pruefe mihilfe einer Bedingung danach, ob die Frage richtig oder falsch beantwortet wurde und informiere den Benutzer mit der print-Funktion darueber.

#   Welcher Tag ist heute?
Tag = input("Gib den Tag ein:")
zahl= int(Tag)
if zahl > 5:
    print("Freitag")
else:
    print("Donnerstag")
print(zahl)

Tag = 2
if Tag < 5:
    print("Ist es richtig")
else:
    print("Ist es falsch")

# 3 Verbessere die Ausgabe des schnelleren Arbeiters aus der 3. Aufgabe in Aufgabenblatt2.
#   Verwende eine Bedingung, um unterschiedliche Ausgaben (print) im "Wenn" (if) und "Sonst" (else) Fall auszugeben.

# Der Arbeiter arbeitet 10 Stunden und er bewegt 2,5 Steine pro Stunde
Arbeiter1 = input("Gib etwas ein:")
zahl = int(Arbeiter1)
if zahl > 3:
    print("mehr geschafft als sonst")
else:
    print("weniger geschafft als sonst")

# Die Distanz von A bis B ist 4km.
Distanz = 4
if Distanz < 4:
    print("weinger gelaufen als üblich")
else:
    print("mehr gelaufen als üblich")


#Extra Übung
zahl1 = 12
zahl2 = input("Gib eine Zahl ein: ")
div = zahl1 / int(zahl2) * 2
print("Das Ergebnis lautet " + str(div))
