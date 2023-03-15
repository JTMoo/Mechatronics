# |-----------------------------------------------------------------|
# |Komma-Zahlen erhalten einen speziellen Typ: float                |
# |Initialisiere eine Float-Variable mit folgendem Befehl:          |
# | float(Zahl)                                                     |
# |Nachkommastellen bei dieser Initialisierung mit einem ".":       |
# | float(12.2)                                                     |
# |Zahlen können auch innerhalb einer "Operation" stattfinden:      |
# |Zahl / float(Zahl2)                                              |
# |-----------------------------------------------------------------|

# 1 Gebe das genaue Ergebnis der Rechnung 12/5 aus.
x=12
y=5
print(12/5)
Variable=float(12/5)
print(Variable)

# 2 Finde eine Operation (mithilfe einer Suchmaschine), die Zahlen runden kann.
# Gebe das Ergebnis von 1/3 auf 2 Nachkommastellen genau aus.
Variable=float(1/3)
print(int(Variable))

# 3.1 Wenn ein Arbeiter am Tag 25 Steine von A nach B bringen kann, wie viele Steine
# bewegt er dann in der Stunde? (Achtung: hier muss eine Annahme getroffen werden)
# 3.2 Wie weit ist A von B entfernt? (Mehrere Annahmen nötig, Annahmen müssen begründet werden)
# 3.3 Ist ein anderer Arbeiter, der 15 Steine am Tag, über eine Entfernung von 1km trägt schneller oder langsamer?
# |---------------------------------------------------------------------------------------------|
# | Info zu Aufgabe 3:                                                                          |
# | - Alle Ergebnisse mit einem print ausgeben                                                  |
# | - Es muss eine ausführbare Datei erstellt werden, die immer die gleichen Ergebnisse liefert |
# | - Für Aufgabe 3.3 müssen Vergleichsoperatoren ('<', '>' oder '==') verwendet werden         |
# |   Diese sind in der gleichnamigen Datei mit dieser Datei dokumentiert                       |
# |---------------------------------------------------------------------------------------------|

# Arbeiter
Arbeitereins=float(25)
Arbeiterzwei=float(15)
# Der Arbeiter arbeitet 10 Stunden und er bewegt 2,5 Steine pro Stunde
Steine=float(25/10)
print(Steine)
# Die Distanz von A bis B ist 4km.
Distanz=float(10/4)
print(Distanz)
# Der zweite Arbeiter arbeitet zehn Stunden täglich
# Seine Distanz von C nach D ist 1 km
# Er trägt 15 Steine
Steinee=float(15/10)
print(Steinee)
# Distanz von C nach D
Distanzz=float(10/1)
print(Distanzz)
# Der erste Arbeiter trägt mehr Steine am Tag
Arbeiter=float(Arbeitereins>Arbeiterzwei)
print(Arbeiter)
