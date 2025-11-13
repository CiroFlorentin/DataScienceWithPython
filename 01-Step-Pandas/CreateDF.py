import pandas as pd

#! Crear  Dataframe a partir de lista de diccionarios
#? Fila a Fila

# list_of_dicts =[
#     {"name":"Ginger", "breed":"Dachshund","height_cm":22 , "weight_kg":10,"date_of_birth":"2019-03-14" },
#     {"name":"Scout", "breed":"Dalmatian","height_cm":59 , "weight_kg":25,"date_of_birth":"2019-05-09" },
# ]
# new_dogs = pd.DataFrame(list_of_dicts)
# print(new_dogs) 

# ! Crear Dataframe a partir de un diccionario de listas
#? Columna a columna

# dict_of_lists ={
#     "name":['Ginger','Scout'],
#     "breed":['Dachshund','Dalmatian'],
#     "height_cm":[22,59],
#     "weight_kg":[10,25],
#     "date_of_birth":["2019-03-14","2019-05-09"]
# }
# new_dogs = pd.DataFrame(dict_of_lists)
# print(new_dogs)