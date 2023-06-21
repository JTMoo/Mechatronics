# 1 Wenn ein Arbeiter am Tag 25 Steine von A nach B bringen kann, wie viele Steine
# bewegt er dann in der Stunde? (Achtung: hier muss eine Annahme getroffen werden)
# 2 Wie weit ist A von B entfernt? (Mehrere Annahmen nötig, Annahmen müssen begründet werden)
# 3 Ist ein anderer Arbeiter, der 15 Steine am Tag, über eine Entfernung von 1km trägt schneller oder langsamer?
# |---------------------------------------------------------------------------------------------|
# | Info zu Aufgaben 1-3:                                                                       |
# | - Alle Ergebnisse mit einem print ausgeben                                                  |
# | - Es muss eine ausführbare Datei erstellt werden, die immer die gleichen Ergebnisse liefert |
# | - Für Aufgabe 3 müssen Vergleichsoperatoren ('<', '>' oder '==') verwendet werden           |
# |   Diese sind in der gleichnamigen Datei mit dieser Datei dokumentiert                       |
# |---------------------------------------------------------------------------------------------|

# geht die distanz von A B * 2 

steine = 25
einen_arbeits_tag = 8 
print(steine)
print(einen_arbeits_tag)
teilen = steine/einen_arbeits_tag
print(teilen)
print("er bewegt " + str(int(steine/einen_arbeits_tag)) + " steine pro stunde")

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

AB_am_tag = steine*2
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
