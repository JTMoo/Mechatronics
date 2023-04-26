# 3.1 Wenn ein Arbeiter am Tag 25 Steine von A nach B bringen kann, wie viele Steine
# bewegt er dann in der Stunde? (Achtung: hier muss eine Annahme getroffen werden)
t = 8
Steine = 25
Steine_pro_h = Steine / t
print("Der Arbeiter trägt " + str(Steine_pro_h) + " Steine pro Stunde")

# 3.2 Wie weit ist A von B entfernt? (Mehrere Annahmen nötig, Annahmen müssen begründet werden)
# Distanz (s) = v * t // km/h * h = km
V = 3
s_pro_Tag = V * t
print("Der Arbeiter geht " + str(t) + "km am Tag")

StreckeAB_am_Tag = Steine * 2
s_AB = s_pro_Tag / StreckeAB_am_Tag
print("Die Strecke von A nach B beträgt " + str(s_AB) + "km")

# 3.3 Ist ein anderer Arbeiter, der 15 Steine am Tag, über eine Entfernung von 1km trägt schneller oder langsamer?
Steine2 = 15
s = 1
s_amTag = Steine2 * 2
s_pro_Tag = s * s_amTag
print("Arbeiter2 läuft " + str(s_pro_Tag) + "km am Tag")

V2 = V
t2 = s_pro_Tag / V2
print("Arbeiter2 insgesamt " + str(t2) + ("h am Tag gearbeitet"))
print("Die Aussage: Arbeiter2 ist schneller, ist: " + str(t2 < t))

# |---------------------------------------------------------------------------------------------|
# | Info zu Aufgabe 3:                                                                          |
# | - Alle Ergebnisse mit einem print ausgeben                                                  |
# | - Es muss eine ausführbare Datei erstellt werden, die immer die gleichen Ergebnisse liefert |
# | - Für Aufgabe 3.3 müssen Vergleichsoperatoren ('<', '>' oder '==') verwendet werden         |
# |   Diese sind in der gleichnamigen Datei mit dieser Datei dokumentiert                       |
# |---------------------------------------------------------------------------------------------|