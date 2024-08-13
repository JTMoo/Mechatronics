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

PEpos,2i​\=sin(100002i/dmodel​pos​) PEpos,2i+1\=cos⁡(pos100002i/dmodel)PE\_{pos, 2i+1} = \\cos\\left(\\frac{pos}{10000^{2i/d\_{\\text{model}}}}\\right)PEpos,2i+1​\=cos(100002i/dmodel​pos​)
