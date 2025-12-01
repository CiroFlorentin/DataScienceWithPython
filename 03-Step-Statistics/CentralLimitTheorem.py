import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt



die = pd.Series([1,2,3,4,5,6])

# samp_5 = die.sample(5,replace=True)

# print(samp_5.mean())

#! Teorema Central del Limite (la distribución muestral se asemeja a una normal) - TLC
#* solo para estadísticas aleatorias e independientes
sample_means=  []
for i in range(1000):
    sample_means.append(np.mean(die.sample(5,replace=True)))
sample_means = [float(x) for x in sample_means] #los convierte en float

# print(sample_means)
# plt.hist(sample_means)
# plt.grid(True)
# plt.show()

#? Desviación típica y el TLC
simple_sds  = []
for i in  range(1000):
    simple_sds.append(np.std(die.sample(5,replace=True)))
simple_sds = [float(x) for x in simple_sds] 
# print(simple_sds) 

# plt.hist(simple_sds)
# plt.grid(True)
# plt.show()


#? Proporciones y el TLC
sales_team = pd.Series(['Amir','Brian','Claire','Damian'])

sample_proportions = []
for _ in range(1000):
    props = sales_team.sample(10,replace=True).value_counts(normalize=True)
    sample_proportions.append(props.get('Claire',0))

sample_proportions = [float(x) for x in sample_proportions] 
# print(sample_proportions)
# plt.hist(sample_proportions)
# plt.grid(True)
# plt.show()

# print(np.mean(sample_proportions))
# print(np.mean(sample_means)) 

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'src', 'amir_deals.csv')
amir_deals = pd.read_csv(csv_path)

# amir_deals['num_users'].hist() #* plt.hist(amir_deals['num_users']) 
# plt.grid(True)
# plt.show()

np.random.seed(104)
# samp_20 = amir_deals['num_users'].sample(20,replace=True)

# samp_20_mean  = np.mean(samp_20)

sample_means = []
for _ in range(100):
    samp_20 = amir_deals['num_users'].sample(20,replace=True)
    samp_20_mean  = np.mean(samp_20)
    sample_means.append(samp_20_mean)

sample_means_series = pd.Series(sample_means)
# sample_means_series.hist()
# plt.grid(True)
# plt.show()

# -------------------------
np.random.seed(321)

sample_means = []

for i in range(30):
  cur_sample = amir_deals['num_users'].sample(20,replace = True)
  cur_mean = cur_sample.mean()
  sample_means.append(cur_mean)
  
print(np.mean(sample_means))
print(amir_deals['num_users'].mean())

#* El numero de promedio de usuarios de Amir esta muy cerca del promedio general. Por lo que cumple las estadísticas