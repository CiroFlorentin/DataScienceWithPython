import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

dogs = pd.read_csv(csv_path)

dogs['height_cm'].info() # info() muestra información sobre el DataFrame
dogs['height_cm'].describe() # describe() muestra estadísticas descriptivas
dogs['height_cm'].max() # MAXIMO
dogs['height_cm'].min() # MINIMO
dogs['height_cm'].mean() # MEDIA 
dogs['height_cm'].median() # MEDIANA
dogs['height_cm'].mode() # MODA 
dogs['height_cm'].std() # DESVIACIÓN ESTÁNDAR
dogs['height_cm'].var() # VARIANZA
dogs['height_cm'].quantile(0.25) # CUARTIL
dogs['weight_kg'].cumsum() # SUMA ACUMULADA
dogs['weight_kg'].cummax() # MAXIMO ACUMULADO
dogs['weight_kg'].cummin() # MINIMO ACUMULADO
# dogs['weight_kg'].cumcount() # CONTADOR ACUMULADO
dogs['weight_kg'].cumprod() # PRODUCTO ACUMULADO


dogs.drop_duplicates(subset=['breed' , 'name'])# drop_duplicates() elimina duplicados
dogs['breed'].value_counts(sort=True) # value_counts() cuenta los valores
dogs['breed'].value_counts(normalize=True) # normalize() normaliza los valores



def pct30(column):
    return column.quantile(0.3)
def pct40(column):
    return column.quantile(0.4)

# print(dogs[['weight_kg', 'height_cm']].agg(pct30)) # aplica funciones de agregación
# print(dogs[['weight_kg', 'height_cm']].agg([pct30, pct40])) # aplica varias funciones de agregación
# print(dogs[['weight_kg', 'height_cm']].apply(pct30)) # se utiliza para aplicar una función a lo largo de un eje


# !  Estadísticas resumidas agrupadas
# print(dogs.groupby('color')['weight_kg'].mean()) # mean() media
# print(dogs.groupby('color')['weight_kg'].agg(['min','max','sum'])) # agg() agrupa

# ! Tablas dinámicas
# print(dogs.pivot_table(values='weight_kg', index='color' , columns='breed' , fill_value=0 , margins=True )) # pivot_table() tablas dinámicas