# -*- coding: utf-8 -*-
"""redneuronalbasic.ipynb



import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("comenzando entrenamiento....")
historial = modelo.fit(celsius, fahrenheit, epochs=500, verbose=False)
print("modelo entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("magnitud de perdida")
plt.plot(historial.history["loss"])

print("Hagamos una prediccion!")
resultado = modelo.predict([100.0])
print("El resultado es " + str(resultado) + " fahrenheit!")

print("variables internas del modelo")
print(capa.get_weights())
