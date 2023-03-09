# Das ist eine Python-Datei.
# Python-Dateien sind durch die Endung .py gekennzeichnet.
# Python ist eine sogenannte sequentielle Programmiersprache.
# Sequentiell bedeutet, dass der Code von oben nach unten "interpretiert"*
# Den Effekt kann man anhand der folgenden Anweisungen erkennen:

x = 12      # In dieser Zeile wird die Variable 'x' mit dem Wert 12 initialisiert**.
x = 5       # Diese Zeile überschreibt den Wert der Variablen 'x' mit dem Wert 5.
print(x)    # Diese Zeile bestätigt das. Es wird '5' ausgegeben und der Wert '12 ist verloren.

# Merke: Es können im selben Kontext*** niemals 2 Variablen mit dem gleichen Namen existieren.



# *Interpretation in Python übernimmt ein sogenannter Compiler.
# Compiler sprechen in der Regel genau eine (Programmier-)Sprache und helfen der Kommunikation zwischen Mensch und Maschine.
# Stark vereinfacht kann man sagen, dass Maschinen nur Binärcode (0en und 1en) verstehen.
# Der Mensch kann eine Programmiersprache beherrschen und der Compiler interpretiert, den verfassten Code für die Maschine.
# Das bedeutet er übersetzt (oder compiled) den Code in Binärcode, der für die Maschine versändlich ist.

# **Initialisieren ist der Prozess der Erstellung einer neuen Variablen.
# Nur die erste Zuweisung einer Variablen wird als Initialisierung bezeichnet.
# Initial stammt vom lateinischen Wort 'initialis' was soviel bedeutet wie anfänglich, also der Ursprung der Variable.
# Dargestellt im Code sieht das folgendermaßen aus:
simpleVariable = 14     # Das ist eine Zuweisung und gleichzeitig die Initialisierung der Variablen 'simpleVariable'
simpleVariable = 14     # Das ist NUR eine Zuweisung. Der Wert, der der Variablen zugewiesen wird spielt KEINE Rolle.
x = 15                  # Das ist ebenfalls NUR eine Intialisierung. Die Variable 'x' wurde bereits oben in dieser Datei Initialisiert!

# ***Kontext ist ein wichtiger Begriff im Bereich der Programmierung.
# Dieser Begriff wird bei den Themen "Bedingungen, Schleifen/Loops, Funktionen und Klassen" besonders relevant.
# Der Kontext wird in Python durch die Einrückung bestimmt.
# Klarer wird das ganze in folgendem Code-Ausschnitt:
def methodName():   # Zuerst wird hier eine Methode/Funktion erstellt. Wie das genau funktioniert, wird im entsprechenden Block besprochen. 
    x = 28          # Hier wird eine Methode 'x' initialisiert
    print(x)        # Hier wird diese Variable ausgegeben

x = 15              # Hier wird eine weitere Variable mit dem Namen 'x' initialisiert. Das funktioniert, weil der Kontext (Die Einrückung) unterschiedlich ist.
methodName()        # Ausführung der Methode und damit Ausgabe des Werts '28'
print(x)            # Ausgeben des Werts für x -> '15'
