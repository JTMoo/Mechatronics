def function1(var1):
  if var1 == 99:
    return
  
  function1(var1+1)
  print(var1)
  
var2 = 0
function1(var2)

# Diese Funktion zahlt von 99-1 rueckwarts zu null.
# Das Prinzip, dass sich hinter dieser Funktion verbirgt nennt man "Rekursion".
# Bei einer Rekursion ruft eine Funktion sich immer wieder selbst auf. (In unserem Fall ist der Aufruf von function1 in der Definition von function1 enthalten)
# Damit die Funktion nicht in einer Endlosschleife endet (Immer wiederkehrender Aufruf ohne Ende), ist ein Anker eingebaut, bei dem die Funktion abbricht.
# Auf den ersten Blick muesste das Programm eigentlich von 0 hoch zaehlen (Ausgabe von var1 im Programm). 
# Veranschauliche in einer Zeichnung (Von Hand, Paint oder Aehnliches), warum die Funktion von 99-1 abwaerts zeahlt.
