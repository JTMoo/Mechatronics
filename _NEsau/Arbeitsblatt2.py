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
Var=float(12/5)
print(Var)

# 2 Finde eine Operation (mithilfe einer Suchmaschine), die Zahlen runden kann.
# Gebe das Ergebnis von 1/3 auf 2 Nachkommastellen genau aus.
Vari=float(1/3)
print(int(Vari))


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

# Der Arbeiter arbeitet 10 Stunden täglich.
# Die Distanz zwischen A und B ist von 4km.
Steine1=25
Stunden1=10
print(Steine1/Stunden1)
# Er trägt 2.5 Steine pro Stunde.
Distanz1=float(10/4)

# Der zweite Arbeiter arbeitet 10 Stunden täglich.
# Seine Distanz zwischen C und D ist 1km.
# Er trägt 15 Steine.
Steine2=15
Stunden2=10
print(Steine2/Stunden2)
# Er trägt 1.5 Steine pro Stunde.
Distanz2=float(10/1)

# Der erste Arbeiter trägt seine Steine schneller als der zweite Arbeiter.
Arbeiter=float(Steine1>Steine2)
print(Arbeiter)

