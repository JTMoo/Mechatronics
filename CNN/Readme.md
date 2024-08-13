# Was ist eigentlich KI?
TODO: Hier Artikel verlinken.
# Aufbau eines Neuronalen Netzes:
![Neuronales Netz](https://github.com/JTMoo/Mechatronics/blob/main/CNN/image.png?raw=true)

# Autoencoder + LLMs (Large Language Models) + NLP (Natural Language Processing)

## Aufbau eines Autoencoders:
![Autoencoder](https://github.com/JTMoo/Mechatronics/blob/main/CNN/autoencoder_architecture.png?raw=true)

## Large Language Model (LLM)
Ein Large Language Model zum aktuellen Zeitpunkt (August 2024) meist in einer Transformator-Struktur aufgebaut. Das bedeutet konkret nichts anderes wie ein Autoencoder, komibiniert mit zusätzlichen Positionsdaten.

### Warum wird die Struktur bei Autoencodern verwendet?
Unter anderem können die Vorteile der PCA (Principal Component Analysis) genutzt werden. Das bedeutet, dass abstraktere Muster in Daten gefunden werden (sofern vorhanden), die eventuell in den ursprünglichen Daten / Faktoren nicht sichtbar gewesen wären. Zusätzlich findet eine Reduktion der Daten statt. 

### Positionsdaten bei Transformatoren

PE_pos,2i​ = sin(pos / (10000^(2i/d_model​))​)
PE_pos,2i+1 = cos⁡(pos / (10000^(2i/d_model)))

Wobei i die aktuelle Dimension beschreibt und d_model die Anzahl der Dimensionen, um die Objekte zu beschreiben, auf die die KI trainiert ist.
Dimensionen sind in diesem Kontext Faktoren, die die Objekte beschreiben.
Ein konkretes Beispiel: Wenn Tische die Objekte sind, dann sind Größe, Gewicht, Anzahl Beine, Farbe, Material etc. die Faktoren, die man nutzen kann, um das Objekt zu beschreiben.

Die Positionsdaten sind deshalb wichtig, da daraus zusätzliche Informationen gewonnen werden können, die der KI helfen eine genauere Vorhersage zu treffen.
Bezogen auf ein LLM bedeutet das: Welches Wort/Buchstabe kommt wahrscheinlich als nächstes in einem gewissen Satz oder Wort.

### Natural Language Processing
Die Wissenschaft um die Erfassung und Wiedergabe der natürlichen Sprache. Mehr dazu in einem anderen Unterricht.
