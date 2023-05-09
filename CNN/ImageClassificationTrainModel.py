from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# Bevor dieses Neuronale Netz funktionieren kann, muessen zuerst die Daten (v_data.zip) gedownloaded werden.
# Anschliessend muss der Inhalt des zips in den Ordner dieses Skripts kopiert werden.
# Beispiel: Skript liegt unter D:/Skripts - Dann muss nachher ein Ordner D:/Skripts/v_data existieren.

# Festlegung der Groesse der Bilder (in Pixel)
img_width, img_height = 224, 224

# Dateipfade fuer die Daten (Bilder) - In diesem Fall Autos und Flugzeuge
train_data_dir = 'v_data/train'
validation_data_dir = 'v_data/test'
# Anzahl der Bilder im Trainings- und Test-Datensatz
nb_train_samples = 400
nb_validation_samples = 100
# Spezifikationen zum Training (Laenge und die Anzahl pro Bilder in einer "Batch")
epochs = 10
batch_size = 16

# Kann man theoretisch ignorieren. Zur Erklaerung:
# Jeder Pixel hat in der Regel 3 Werte - Zum Beispiel RGB also Rot, Gruen, Blau -> Daraus ergibt sich die Farbe die dargestellt wird
# Wenn die Werte gespeichert werden, dann werden diese Werte allerdings separat gespeichert (Also ein Wert fuer Rot usw.)
# Das hier legt nur fest, wie diese Werte in einer Matrix gespeichert wurden.
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# Hier wird das Neuronale Netz erstellt
model = Sequential()
# Erstes Faltungs-Ebene
model.add(Conv2D(32, (2, 2), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Zweite Faltungs-Ebene
model.add(Conv2D(32, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Dritte Faltungs-Ebene
model.add(Conv2D(64, (2, 2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Sonstige Ebenen
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# Erstellung des Neuronalen Netzes
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Hier wird jetzt einiges gemacht, um die Daten (Bilder) zu laden
# Einmal fuer die Trainingsdaten und einmal fuer die Testdaten
train_datagen = ImageDataGenerator(
	rescale = 1. / 255, 
	shear_range = 0.2,
	zoom_range = 0.2,
	horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1. / 255)

train_generator = train_datagen.flow_from_directory(
	train_data_dir,
	target_size=(img_width, img_height),
	batch_size=batch_size,
	class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
	validation_data_dir,
	target_size=(img_width, img_height),
	batch_size=batch_size,
	class_mode='binary')

# Hier passiert die "Magie"
# Das sogenannte Model des Neueronalen Netzes wird trainiert.
# Dafuer werden alle Variablen, die bisher angelegt wurden verwendet.
model.fit_generator(
	train_generator,
	steps_per_epoch=nb_train_samples // batch_size,
	epochs=epochs,
	validation_data=validation_generator,
	validation_steps=nb_validation_samples // batch_size)

# Dann speichern wir die antrainierten Gewichte des Neuronalen Netzes ab, um Sie zu einem späteren Zeitpunkt zu verwenden.
# Dafuer einfach in dem anderen File in diesem Ordner nachschauen.
model.save_weights('model_saved.h5')
