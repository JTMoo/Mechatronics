# 3.1 Wenn ein Arbeiter am Tag 25 Steine von A nach B bringen kann, wie viele Steine
# bewegt er dann in der Stunde? (Achtung: hier muss eine Annahme getroffen werden)
t = 8
Anzahl_Steine = 25
Anzahl_Steine_Stunde = Anzahl_Steine / t
print("Der Arbeiter trägt" + str(Anzahl_Steine_Stunde) + "Steine pro Stunde")

# 3.2 Wie weit ist A von B entfernt? (Mehrere Annahmen nötig, Annahmen müssen begründet werden)
# Distanz (s) = v * t // km/h * h = km
v = 3 #km/h wenn man bedenkt, dass er Pausen macht und nicht immer gleich schnell läuft.
s_amTag = v * t
print("Der Arbeiter geht" + str(t) + "km am Tag")

AB_amTag = Anzahl_Steine * 2
s_AB = s_amTag / AB_amTag
print("Die Strecke von A nach B beträgt" + str(s_AB) + "km")

# 3.3 Ist ein anderer Arbeiter, der 15 Steine am Tag, über eine Entfernung von 1km trägt schneller oder langsamer?
Steine2 = 15
s_CD = 1
CD_amTag = Steine2 * 2
s_amTag = s_CD * CD_amTag
print("Arbeiter2 läuft" + str(s_amTag) + "km am Tag")

v2 = v
t2 = s_amTag / v2
print("Arbeiter2 insgesamt" + str(t2) + ("h am Tag arbeitet"))
print("Die Aussage: Arberiter2 ist schneller ist:" + str(t2 < t))

# |---------------------------------------------------------------------------------------------|
# | Info zu Aufgabe 3:                                                                          |
# | - Alle Ergebnisse mit einem print ausgeben                                                  |
# | - Es muss eine ausführbare Datei erstellt werden, die immer die gleichen Ergebnisse liefert |
# | - Für Aufgabe 3.3 müssen Vergleichsoperatoren ('<', '>' oder '==') verwendet werden         |
# |   Diese sind in der gleichnamigen Datei mit dieser Datei dokumentiert                       |
# |---------------------------------------------------------------------------------------------|