import pandas as pd
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

dogs = pd.read_csv(csv_path)

# ! Histograma
# dogs['height_cm'].hist() #Bins por defecto es 10
# plt.show()

#! Grafico de barras
# avg_weight = dogs.groupby('breed')['weight_kg'].mean()
# avg_weight.plot(kind='bar', title='Average Weight by Breed')
# plt.show()

#! Grafico de linea
# sully = dogs.head()
# sully.plot(x='date_of_birth', y='weight_kg', kind='line',rot=45) #kind es el tipo de gráfico
# plt.show()

# ! Grafico de dispersion
# dogs.plot(x='height_cm', y='weight_kg', kind='scatter')
# plt.show()

#! Tratamiento de valores nulos 
# dogs.isna().sum() # Muestra la cantidad de valores nulos por columna
# dogs.isna().any() # Muestra si hay valores nulos por columna
# dogs.dropna() # Elimina las filas con valores nulos
# dogs.fillna(0) # Rellena los valores nulos con un valor
