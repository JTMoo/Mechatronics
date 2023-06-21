
# 1 Wenn bei der Division (Teilen) der 3. Aufgabe, die eingelesene Zahl im Nenner steht (eingelesene_Zahl = input().... div = Zahl2 / eingelesene_Zahl), in welchem Fall schlaegt die Division dann fehl?
#   Wie kann durch eine Bedingung, dieser Fall verhindert werden?
#   Schreibe dieses Programm.

# 2 Schreibe ein Programm, dass eine (beliebige) Frage ausgibt und dann eine Antwort des Benutzers abwartet.
#   Pruefe mihilfe einer Bedingung danach, ob die Frage richtig oder falsch beantwortet wurde und informiere den Benutzer mit der print-Funktion darueber.

# 3 Verbessere die Ausgabe des schnelleren Arbeiters aus der 3. Aufgabe in Aufgabenblatt2.
#   Verwende eine Bedingung, um unterschiedliche Ausgaben (print) im "Wenn" (if) und "Sonst" (else) Fall auszugeben.

#aufg.1
ersteZahl = input("Gebe eine Zahl aus. Diese Zahl wird durch die zweite geteilt. \n")


if ersteZahl == 0:
    print(str("Du solltest eine ZAHL ausgeben"))
else:
   print("Gut")


zweiteZahl = input("Gebe die zweite Zahl aus \n" )



if zweiteZahl == 0:
    print(str("Du solltest eine ZAHL ausgeben"))
else:
    print(str("Gut."))

division = int(ersteZahl) / int (zweiteZahl)
print(division)






#aufg.2
Antwort = input("Im welchen Land leben wir? \n")
print(type(Antwort))

if Antwort ==  "Paraguay":
    print(str("Ja, das stimmt."))
else:
    print(str("Nein, das stimmt nicht."))




    #aufg.3

anzahlDerSteine = input("gebe die Anzahl der Steine: \n")
print(anzahlDerSteine)

if anzahlDerSteine == 0:
    print(str("Nein, es sollte eine Zahl sein"))
else:
    print(str("Gut."))

steine = anzahlDerSteine
einen_arbeits_tag = 8 
print(steine)
print(einen_arbeits_tag)
teilen = int(steine)/(int(einen_arbeits_tag))
print(teilen)
print("er bewegt " + str(int(steine)/int(einen_arbeits_tag)) + " steine pro stunde")

geht_ohne_stein_kmh = 5
print(geht_ohne_stein_kmh)
geht_mit_stein_kmh = 3
print(geht_mit_stein_kmh)

bringt_in_einer_stunde = 3,125
print(bringt_in_einer_stunde)

v = 3 #hm/h
print(v)
Anzahl_Distanz_Stunde = bringt_in_einer_stunde * 2
print(Anzahl_Distanz_Stunde)
geht_in_einen_T = v*einen_arbeits_tag

print(v*einen_arbeits_tag)
print("er geht in einem tag ins gesammt " + str(geht_in_einen_T) + " KM")

AB_am_tag = int(steine)*2
print(AB_am_tag)

AB_Distanz = geht_in_einen_T/AB_am_tag
print(AB_Distanz)

steine2 = 15
print(steine2)
s_cd = 1 #hm
print(s_cd)

cd_am_tag = steine2*2
print(cd_am_tag)

s_am_tag = s_cd* cd_am_tag
print(s_am_tag)
print( "Arbeiter2 läuft " + str(s_am_tag) + " km am tag")

v2 = v
print(v2)
t2 = s_am_tag / v2
print(t2)

print( "Arbeiter2 arbeitet insgesamt " + str(t2) + " h am Tag")
print("Die Aussage: Arbeiter2 ist schneller ist: " + str(t2 < einen_arbeits_tag))

