import pandas as pd
from sklearn import svm

# Laden Sie Ihre Daten in ein DataFrame
data = pd.read_csv('path/to/your/data.csv')

# Extrahieren Sie die Features und Labels aus den Daten
X = data[['feature1', 'feature2', ...]]
y = data[0]

# Erstellen Sie einen SVM-Klassifikator
clf = svm.SVC()

# Trainieren Sie den Klassifikator mit Ihren Daten
clf.fit(X, y)

# Verwenden Sie den Klassifikator, um Vorhersagen für neue Daten zu treffen
y_pred = clf.predict([[new_feature1, new_feature2, ...]])

import pandas as pd

# Laden Sie Ihre Daten in ein DataFrame
data = pd.read_csv('path/to/your/data.csv')

# Extrahieren Sie die Features und Labels aus den Daten
X = data[['temperature_2m (°C)', 'relativehumidity_2m (%)', 'rain (mm)', 'surface_pressure (hPa)', 'cloudcover (%)', 'windspeed_100m (km/h)', 'winddirection_10m (°)']]
y = data['time']
