# pythonistas = {'hugo':'Bowne-anderson', 'julio':'Crespo', 'carlos':'Garcia'}

# for key, value in pythonistas.items():
#     print(key, value)
    
    
    
avengers = ['hulk', 'spiderman', 'ironman']
names = ['hugo', 'julio', 'carlos']

# for index, value in enumerate(avengers):
#     print(index, value)

# for z1, z2 in zip(avengers, names):
#     # print(z1, z2)



#! big data

# import pandas as pd

# result = []

# for chunk in pd.read_csv('data.csv', chunksize=1000):
#     result.append(sum(chunk['x']))

# total = sum(result)
# print(total)

#? Ejemplo 2

import pandas as pd
import os

# counts_dict = {}

# for chunk in pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'tweets.csv'), chunksize=10):
#     for value in chunk['lang']:
#         if value in counts_dict:
#             counts_dict[value] += 1
#         else:
#             counts_dict[value] = 1

# print(counts_dict)

def count_entries(csv_file,c_size,colname):
    counts_dict = {}
    for chunk in pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', csv_file), chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict:
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict

result_counts = count_entries('tweets.csv',10,'lang')
print(result_counts)