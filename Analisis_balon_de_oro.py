import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

read = pd.read_csv('balon_de_oro.csv')

ypoints = np.array(read['Puntos'].tail(5))
ypoints = ypoints.astype(int)
xpoints = np.array(read['Año'].tail(5))

#Etiquetas para el gráfico
plt.title('Puntos de los Ganadores del Balón de Oro\nÚltimos 5 años',loc='left')
plt.xlabel("Año")
plt.ylabel("Puntos")
plt.grid(axis='x')
plt.xticks(xpoints)
plt.ylim(350, 1400)

#Crear gráfico
plt.plot(xpoints, ypoints)

#Guardar como PNG
plt.savefig('grafico.png')

#Esta línea es opcional si estas en un archivo ipynb 
plt.show()
