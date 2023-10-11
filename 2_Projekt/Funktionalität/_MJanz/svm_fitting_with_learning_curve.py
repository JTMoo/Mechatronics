from sklearn.svm import SVC

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.model_selection import LearningCurveDisplay, ShuffleSplit


# Extrahieren Sie die Features und Labels aus den Daten

data = pd.read_csv(r'\\WS2K19STD\perfiles$\manuel.janz\Documents\Schule\Robótica\historical_weather.csv')
data = data.dropna(how='any') #to drop if any value in the row has a nan
data = data[:1000]

X = data[['temperature_2m (°C)', 'relativehumidity_2m (%)', 'rain (mm)', 'surface_pressure (hPa)', 'cloudcover (%)', 'windspeed_100m (km/h)', 'winddirection_10m (°)']]
y = data['time']

svc = SVC(kernel="rbf", gamma=0.001)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 6), sharey=True)

common_params = {
    "X": X,
    "y": y,
    "train_sizes": np.linspace(0.1, 1.0, 5),
    "cv": ShuffleSplit(n_splits=50, test_size=0.2, random_state=0),
    "score_type": "both",
    "n_jobs": 4,
    "line_kw": {"marker": "o"},
    "std_display_style": "fill_between",
    "score_name": "Accuracy",
}

for ax_idx, estimator in enumerate([svc]):
    LearningCurveDisplay.from_estimator(estimator, **common_params, ax=ax[ax_idx])
    handles, label = ax[ax_idx].get_legend_handles_labels()
    ax[ax_idx].legend(handles[:2], ["Training Score", "Test Score"])
    ax[ax_idx].set_title(f"Learning Curve for {estimator.__class__.__name__}")