# 1 Wenn bei der Division (Teilen) der 3. Aufgabe, die eingelesene Zahl im Nenner steht (eingelesene_Zahl = input().... div = Zahl2 / eingelesene_Zahl), 
#   in welchem Fall schlaegt die Division dann fehl?
Zahl2=12
Eingelesene_Zahl=input("Gebe eine Zahl ein: \n")
print("\n")
div= Zahl2 / int(Eingelesene_Zahl) 
print("Das Resultat lautet: " + str(div))
#Es schlägt fehl, wenn man str und int nicht richtig einsetzt.

#   Wie kann durch eine Bedingung, dieser Fall verhindert werden?
#   Schreibe dieses Programm.
Zahl2=12
Eingelesene_Zahl=input("Gebe eine Zahl ein: \n")
print("\n")
Eingelesene_Zahl=int(Eingelesene_Zahl) 
if Eingelesene_Zahl != 0:
    div = Zahl2 / int(Eingelesene_Zahl) 
    print(div)

# 2 Schreibe ein Programm, dass eine (beliebige) Frage ausgibt und dann eine Antwort des Benutzers abwartet.
#   Pruefe mihilfe einer Bedingung danach, ob die Frage richtig oder falsch beantwortet wurde und informiere den Benutzer mit der print-Funktion darueber.
Antwort1=input("Wie alt bist du?: \n")
print("\n")
Zahl=int(Antwort1)
if Zahl > 17:
    print("Mayor de edad")
else: 
    print("Menor de edad")

# 3 Verbessere die Ausgabe des schnelleren Arbeiters aus der 3. Aufgabe in Aufgabenblatt2.
#   Verwende eine Bedingung, um unterschiedliche Ausgaben (print) im "Wenn" (if) und "Sonst" (else) Fall auszugeben.
Steine1=input("Wie viele Steine trägt Arbeiter 1 in 10 Stunden?: \n")
Stunden1=10
div2=int(Steine1)/Stunden1
print(div2)
if div > 1.5:
    print("Arbeiter 1 ist schenller")
else:
    print("Arbeiter 2 ist schenller")
    
# Arbeiter 2 trägt 1.5 Steine pro Stunde.
