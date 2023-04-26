# Variablen mit Benutzereingaben
# name = input("Gib deinen Namen ein: \n")
# print("\n")
# print("Dein Name lautet: " + name)

# Bedingungen
#zahl = int(input("Gib eine Zahl ein: "))
#if zahl > 10:
#    print("Die Zahl ist größer 10")
#else:
#    print("Die Zahl ist kleiner 10")
# ---------------------------------------------- notizen


# 1 Erfasse deinen Namen mit einer Benutzereingabe und gebe diesen wieder aus.
name = input("Gib deinen Namen ein: \n")
print("\n")
print("Mein Name lautet: " + name)

# 2 Kopiere das gesamte Programm aus Aufgabenblatt2 hier her.
#   Passe die 1.Aufgabe in Aufgabenblatt2 so an, dass die Anzahl der Steine von Arbeiter1 als Benutzereingabe (input) erfasst wird. (Bisher immer 25 Steine)
#   Bestimme die Anzahl der Steine, bei dem der schnellere Arbeiter wechselt. (Beispiel: Wenn Arbeiter 1 15 Steine am Tag traegt, dann ist er schneller als Arbeiter 2)

Anzahl_Steine = int(input("Gib die Steinanzahl ein: \n"))
print("\n")
print("Gib die Steinanzahl ein:" + str(Anzahl_Steine))

if Anzahl_Steine > 15:
    print("Er ist schneller als Arbeiter 2")
else:
    print("Er ist langsamer als Arbeiter 2")

# Anzahl_Steine_Stunde = Anzahl_Steine/t
# print("Der Arbeiter trägt" + str(Anzahl_Steine_Stunde) + "Steine pro Stunde")

# v = 3
# s_amTag = v * t
# print("Der Arbeiter geht" + str(t) + "km am Tag")

# AB_amTag = Anzahl_Steine * 2
# s_AB = s_amTag / AB_amTag
# print("Die Strecke von A nach B beträgt" + str(s_AB) + "km")

# Steine2 = 15
# s_CD = 1
# CD_amTag = Steine2 * 2
# s_amTag = s_CD * CD_amTag
# print("Arbeiter2 läuft" + str(s_amTag) + "km am Tag")

# v2 = v
# t2 = s_amTag / v2
# print("Arbeiter2 insgesamt" + str(t2) + ("h am Tag arbeitet"))
# print("Die Aussage: Arberiter2 ist schneller ist:" + str(t2 < t))

# 3 Verwende eine Benutzereingabe, um eine Division durchzuführen.
zahl = int(input("Gib eine Zahl ein: \n"))
print("\n")
print("Gib die Zahl ein: "+ str(zahl))

if zahl / 2 == 5:
    print("Die eingegebene Zahl ist 10.")
else:
    print("Die eingegebene Zahl ist nicht 10.")

# 3.1 Muss die Benutzereingabe kontrolliert werden? Wenn ja, warum? (Hier muss nicht programmiert werden)
# Ja, sie muss kontrolliert werden, weil ansonsten kann irgendetwas eingegeben werden, was das System evtl kaputt machen könnte. Um das zu verhindern, benutzt man die Bedingungen.
# In dieser Aufgabe habe ich die Benutzereingabe nicht kontrolliert, weil ich das nach Versuchen leider nicht hinbekommen habe.