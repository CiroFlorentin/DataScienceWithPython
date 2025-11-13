import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

dogs = pd.read_csv(csv_path)

# print(dogs)
# Establecer columna como índice
# dogs_ind = dogs.set_index('name')
# print(dogs_ind)
# dogs_ind.reset_index(drop=True) # reset_index() resetea el índice y drop=True borra la columna
# print(dogs_ind)


#! PARA QUE SIRVE

# print(dogs[dogs['name'].isin(['Bella','Stella'])])

# dogs_ind = dogs.set_index('name')
# print(dogs_ind.loc[['Bella','Stella']])

# dogs_ind = dogs.set_index(['breed','color']).sort_index()
# print(dogs_ind)
# print(dogs_ind.loc[('Labrador','Brown'):('Poodle','Black'),'name':'height_cm'])

dogs = dogs.set_index('date_of_birth').sort_index()
print(dogs.loc['2014':'2016'])