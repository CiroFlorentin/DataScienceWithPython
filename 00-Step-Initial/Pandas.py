import pandas as pd
import os

#! Primer manera atreves de un diccionario
# dict = {
#     'country': ['brazil','Rusia','India','China','South Africa'],
#     'capital': ['Brasilia','Moscow','New Delhi','Beijing','Pretoria'],
#     'area': [8.516,17.10,3.286,9.597,1.221],
#     'population': [200.4,143.5,1252,1357,52.98]
# }

# BRICS = pd.DataFrame(dict)
# BRICS.index = ['BR','RU','IN','CH','SA']

# print(BRICS)

#! Segunda manera a traves de un archivo csv

# Encuentra la ruta del archivo actual
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "brics.csv")

BRICS = pd.read_csv(csv_path, index_col=0)

# print(BRICS)

# Acceder a una columna
# print(BRICS[['country']])

# Acceder a una fila NO IDEAL
# print(BRICS[1:4])

# ? LOC basado en etiquetas
# print(BRICS.loc['RU']) #* O CON DOBLE [[]]

#* Acceder a varias filas
# print(BRICS.loc[['RU','IN','CH']])

#* Acceder a varias filas y columnas
# print(BRICS.loc[['RU','IN','CH'], ['country','capital']])

# * Acceder a todas las filas, pero alguna columna
# print(BRICS.loc[:, ['country','capital']])

# ? ILOC basado en indices

# print(BRICS.iloc[[1]])

#* Acceder a varias filas
# print(BRICS.iloc[[1,2,3]])

#* Acceder a varias filas y columnas
# print(BRICS.iloc[[1,2,3], [0,1]])

# * Acceder a todas las filas, pero alguna columna
# print(BRICS.iloc[:, [0,1]])

# ! CONOCER EL INDICE DE UN PAÍS

indice = BRICS.index.get_loc('RU')

print(BRICS.iloc[[indice]])


