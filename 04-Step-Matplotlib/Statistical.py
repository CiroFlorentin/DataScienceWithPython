import os 
import matplotlib.pyplot as plt
import pandas as pd

csv_path_olympics = os.path.join(os.path.dirname(__file__), 'src', 'summer2016.csv')
olympics = pd.read_csv(csv_path_olympics, index_col=0)


#! Error bar

mens_rowing= olympics[(olympics['Sport'] == 'Rowing') & (olympics['Sex'] == 'M')]
mens_gymnastics= olympics[(olympics['Sport'] == 'Gymnastics') & (olympics['Sex'] == 'M')]

# fig,ax = plt.subplots()
# ax.bar('Rowing', mens_rowing['Height'].mean(),yerr = mens_rowing['Height'].std())
# ax.bar('Gymnastics', mens_gymnastics['Height'].mean(),yerr = mens_gymnastics['Height'].std())

# ax.set_ylabel('Height (cm)')

# plt.show()

#! Error plot

csv_path_seattle = os.path.join(os.path.dirname(__file__), 'src', 'seattle_weather.csv')
seattle_weather = pd.read_csv(csv_path_seattle)
csv_path_austin = os.path.join(os.path.dirname(__file__), 'src', 'austin_weather.csv')
austin_weather = pd.read_csv(csv_path_austin)

# fig,ax = plt.subplots()
# ax.errorbar(seattle_weather['DATE'], seattle_weather['MLY-TAVG-NORMAL'], yerr=seattle_weather['MLY-TAVG-STDDEV'])
# ax.errorbar(austin_weather['DATE'], austin_weather['MLY-TAVG-NORMAL'], yerr=austin_weather['MLY-TAVG-STDDEV'])

# ax.set_xlabel('Date')
# ax.set_ylabel('Temperature (F)')
# ax.legend(['Seattle', 'Austin'])
# plt.show()

#! Adding a box plot|   

fig,ax = plt.subplots()
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])
ax.set_xticklabels(['Rowing', 'Gymnastics'])
ax.set_ylabel('Height (cm)')
plt.show()


# Linea roja = media 50%
# Bordes del cuadrado = superior Q3 (75%) y inferior Q1 (25%)
# El cuadrado RIC = Rango InterCuartil = Q3 - Q1 (50% de los datos)
# Lineas verticales = Limites Inferiores y Superiores = Q1 - 1.5RIC y Q3 + 1.5RIC (outliers)
# Extremos = Maximo y Minimo
# Puntos = valores atipicos