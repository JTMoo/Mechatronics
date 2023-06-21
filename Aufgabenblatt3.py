# 1 Erfasse deinen Namen mit einer Benutzereingabe und gebe diesen wieder aus.
# |-------------------------------------------------------------|
# | Schaue dir die Funktion "input" mit help(input) genauer an  |
# | Verwende einen Zeilenumbruch im string mit '\n'             |
# |-------------------------------------------------------------|

# 2 Modifiziere die dritte Aufgabe in Aufgabenblatt2 so, dass die Anzahl der Steine als Benutzereingabe definiert ist.
#   Bestimme die Anzahl der Steine, bei dem der schnellere Arbeiter wechselt.

# 3 Verwende eine Benutzereingabe, um eine Division durchzuführen.
# 3.1 Muss die Benutzereingabe kontrolliert werden? Wenn ja, warum?

#aufg.1
help(input)

name = input("Gebe deinen Namen ein: \n")
print("du heisst " + name)

#aufg.2
anzahlDerSteine = input("gebe die Anzahl der Steine: \n")
print(anzahlDerSteine)

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

#aufg.3
ersteZahl = input("Gebe eine Zahl aus. Diese Zahl wird durch die zweite geteilt. \n")
print(ersteZahl)

zweiteZahl = input("Gebe die zweite Zahl aus \n" )
print(zweiteZahl)

teilen = int(ersteZahl)/int(zweiteZahl)
print(teilen)

#aufg.3.1
#Ja, es musst alles kontroliert werden denn wir können nicht davon ausgehen das der Benutzer die Regeln von Programm einhält