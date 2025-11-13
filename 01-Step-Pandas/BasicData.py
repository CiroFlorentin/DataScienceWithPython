import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

df = pd.read_csv(csv_path)



# print(df.head()) # Muestra las primeras 5 filas
# print(df.tail()) # Muestra las ultimas 5 filas
# print(df.info()) # Muestra información del DataFrame
# print(df.describe()) # Muestra estadísticas descriptivas del DataFrame
# print(df.shape) # Muestra la forma del DataFrame
# print(df.columns) # Muestra los nombres de las columnas del DataFrame
# print(df.values) # Muestra los valores del DataFrame
# print(df.index) # Muestra los índices del DataFrame
# df.sort_values(by="BMI", inplace=True, ascending=False) # Ordena el DataFrame por el valor de la columna BMI

