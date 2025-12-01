import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import norm

#* norm.cdf( menos  que , media , desviación)
# print(norm.cdf(154,161,7)) #* Porcentaje de personas que miden menos de 154 cm
# print(1 - norm.cdf(154,161,7)) #* Porcentaje de personas que miden mas de 154 cm
# print(norm.cdf(157,161,7) - norm.cdf(154,161,7)) #* Porcentaje de personas que miden entre 154 y 157 cm

#* norm.ppf( %  , media , desviación)
# print(norm.ppf(0.9,161,7)) #* cual es la estatura del 90% de la población
# print(norm.ppf((1-0.9),161,7)) #* que altura supera el 90% de la población

#* norm.rvs(media , desviación, size)
# print(norm.rvs(161,7,10))

#! Ejemplo de uso
csv_path = os.path.join(os.path.dirname(__file__), 'src', 'amir_deals.csv')
amir_deals = pd.read_csv(csv_path)

# amir_deals['amount'].hist(bins=10)


prob_less_7500 = norm.cdf(7500,5000,2000)
prob_over_1000 = 1 - norm.cdf(1000,5000,2000)
prob_3000_to_7000 = norm.cdf(7000,5000,2000) - norm.cdf(3000,5000,2000)
pct_25 = norm.ppf(0.25,5000,2000)


# Calculate new average amount
new_mean = 5000 * 1.2

# Calculate new standard deviation
new_sd = 2000 * 1.3

# Simulate 36 new sales
new_sales = norm.rvs(new_mean,new_sd,size = 36)

# Create histogram and show
plt.hist(new_sales,bins = 10)
plt.show()