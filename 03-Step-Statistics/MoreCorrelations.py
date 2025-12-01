import os 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

csv_path_sleep = os.path.join(os.path.dirname(__file__), 'src', 'sleep.csv')
msleep = pd.read_csv(csv_path_sleep)

# sns.scatterplot(x='bodywt', y='awake', data=msleep)
# plt.show()
# print(msleep['bodywt'].corr(msleep['awake']))
# msleep['bodywt'].hist(bins=10)

# plt.show()

#? transformacion logarítmica
# msleep['log_bodywt'] = np.log(msleep['bodywt'])

# sns.lmplot(x='log_bodywt', y='awake', data=msleep, ci=None)
# plt.show()

# print(msleep['log_bodywt'].corr(msleep['awake']))

#? transformacion raíz cuadrada
# msleep['sqrt_bodywt'] = np.sqrt(msleep['bodywt'])

# sns.lmplot(x='sqrt_bodywt', y='awake', data=msleep, ci=None)
# plt.show()

# print(msleep['sqrt_bodywt'].corr(msleep['awake']))

#? transformacion reciproca
# msleep['reciprocal_bodywt'] = 1 / msleep['bodywt']

# sns.lmplot(x='reciprocal_bodywt', y='awake', data=msleep, ci=None)
# plt.show()

# print(msleep['reciprocal_bodywt'].corr(msleep['awake']))

#! Estas se pueden combinar y sirven para estadísticas que se basan en variables con un relación lineal
#! con coeficiente de correlación y regresión lineal



# ! EJEMPLO:
csv_path_world = os.path.join(os.path.dirname(__file__), 'src', 'world_happiness.csv')
world_happiness = pd.read_csv(csv_path_world)

# sns.scatterplot(x='gdp_per_cap',y='life_exp',data=world_happiness)
# plt.show()

# cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])
# print(cor)

# sns.scatterplot(x='gdp_per_cap',y='happiness_score',data=world_happiness)
# plt.show()

# cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
# print(cor)

# world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# sns.scatterplot(x='log_gdp_per_cap',y='happiness_score',data=world_happiness)
# plt.show()

# print(world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score']))

sns.scatterplot(x='grams_sugar_per_day', y='happiness_score', data=world_happiness)
plt.show()

print(world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score']))