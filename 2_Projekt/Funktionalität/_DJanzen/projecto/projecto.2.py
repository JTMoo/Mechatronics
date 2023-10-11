import pandas as pd
from sklearn import svm

# Einlesen der historischen Daten
data = pd.read_csv(r'\\WS2K19STD\perfiles$\daniel.janzen\Downloads\historical_weather.csv')

# alle zeilen auslöschen die ein NaN beinhalten
data = data.dropna(how='any')

# Zuordnung zu Features und Labels - Resultat: x enthaelt alle Wetterdaten /// y enthaelt alle Zeiten
x = data[['temperature_2m (°C)', 'relativehumidity_2m (%)', 'rain (mm)', 'surface_pressure (hPa)', 'cloudcover (%)', 'windspeed_100m (km/h)', 'winddirection_10m (°)']]
y = data['time']

# Initialisiern des Klassifikators
clf = svm.SVC()

# Trainieren des Klassifikators (fit = anpassen = Einstellen der Gewichte der KI)
clf.fit(x,y)

# aktulles daten aus der Api auslesen (get funktion)

# Vorhersage treffen mithilfe der uebergebenen Daten clf.predict(uebergebene_Daten) - Gleiche Struktur wie Daten in x, also Temperatur, Luffeuchtigkeit ...
y_pred = clf.predict(x)

# predict anpassen wetterdaten vorhergesagt werden
