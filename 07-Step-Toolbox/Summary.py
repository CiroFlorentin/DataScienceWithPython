import os 

df = os.path.join(os.path.dirname(os.path.abspath(__file__)),'src', 'world_ind_pop_data.csv')
# with open(df) as file:
#     file.readline()
#     counts_dict = {}
    
#     for j in range(1000):
#         line = file.readline().split(',')    

#         first_col = line[0]
        
#         if first_col in counts_dict.keys():
#             counts_dict[first_col] += 1
#         else:
#             counts_dict[first_col] = 1
            
# print(counts_dict)


# def read_large_file(file_object):
#     while True:
#         data = file_object.readline()
#         if not data:
#             break
#         yield  data

# counts_dict = {}      
# with open(df) as file:
#     for line in read_large_file(file):
#         row = line.split(",")
#         first_col = row[0]
        
#         if first_col in counts_dict.keys():
#             counts_dict[first_col] += 1
#         else:
#             counts_dict[first_col] = 1
            
# print(counts_dict)

# ! With pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# urb_pop_reader = pd.read_csv(df,chunksize = 1000)

# df_urb_pop = next(urb_pop_reader)

# df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode']=='CEB']

# pops = list(zip(df_pop_ceb['Total Population'],df_pop_ceb['Urban population (% of total)']))
# # print(pops)

# df_pop_ceb['Total Urban Population'] = [int(tup[0]*tup[1]*0.01) for tup in pops]

# df_pop_ceb.plot(kind='scatter',x='Year',y='Total Urban Population')
# plt.show()

# urb_pop_reader = pd.read_csv(df,chunksize = 1000)
# data = pd.DataFrame()

# for df_urb_pop in urb_pop_reader:
#     df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
#     pops = list(zip(df_pop_ceb['Total Population'],
#                 df_pop_ceb['Urban population (% of total)']))
#     df_pop_ceb['Total Urban Population'] = [int(tup[0]*tup[1]*0.01) for tup in pops]
#     data = pd.concat([data,df_pop_ceb])
    
# data.plot(kind='scatter', x='Year', y='Total Urban Population')
# plt.show()

def plot_pop(filename,country_code):
    urb_pop_reader = pd.read_csv(filename,chunksize = 1000)
    data = pd.DataFrame()

    for df_urb_pop in urb_pop_reader:
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]
        pops = list(zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)']))
        df_pop_ceb['Total Urban Population'] = [int(tup[0]*tup[1]*0.01) for tup in pops]
        data = pd.concat([data,df_pop_ceb])
    
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# plot_pop(df,'CEB')
# plot_pop(df,'ARB')


