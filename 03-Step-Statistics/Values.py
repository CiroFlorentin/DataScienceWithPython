import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import iqr


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_sleep = os.path.join(script_dir, 'src', 'sleep.csv')

msleep = pd.read_csv(csv_path_sleep)


# Cuantos tiempo suelen dormir los mamíferos según este conjunto de datos
#? media central
# print(msleep.groupby('name')['sleep_total'].mean())
# print(f'El total es: {msleep["sleep_total"].mean().round(2)}')

#? la mediana (50% inferior y superior)  EL DATO QUE ESTA EN EL MEDIO
# print(msleep['sleep_total'].median())

#? MODA: valor que mas se repite
# print(msleep['sleep_total'].mode())
# print(msleep['vore'].mode())



#! EJEMPLO 

# print(msleep[msleep['vore'] == 'insecti']['sleep_total'].agg(['mean','median']))

#? Calcular la varianza
#* CALCULO MANUAL
dist = msleep['sleep_total']-msleep['sleep_total'].mean()
sq_dist = dist**2
sum_sq_dist = sq_dist.sum()
variance = sum_sq_dist / len(msleep['sleep_total'])
# print(variance)

#* CALCULO CON PANDAS
# print(msleep['sleep_total'].var(ddof=1))

#? Desviación típica
#* CALCULO MANUAL
# print(np.sqrt(np.var(msleep['sleep_total'], ddof=1)))
#* CALCULO CON PANDAS
# print(msleep['sleep_total'].std(ddof=1))

#? Desviación media absoluta 

dist = msleep['sleep_total']-msleep['sleep_total'].mean()
# print(np.mean(np.abs(dist)))


# ? CUANTILES
# print(msleep['sleep_total'].quantile(0.5))

# * SE SUELE USAR EN DIAGRAMA DE CAJAS
# plt.boxplot(msleep['sleep_total'])
# plt.show()

#* SE PUEDE USAR TAMBIEN ASI
# print(msleep['sleep_total'].quantile([0,0.2, 0.4, 0.6,0.8, 1]))
# print(np.quantile(msleep['sleep_total'], np.linspace(0, 1, 5)))

#? RANGO INTERCUARTÍLICO (IQR)
#* FORMA MANUAL
# print(np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25))
# * FORMA CON SCIPY
# print(iqr(msleep['sleep_total']))


#! UN VALOR ATÍPICO ES CUALQUIER VALOR QUE (DATA < Q1 -1.5 X IQR) O (DATA > Q3 + 1.5 X IQR)

#? EJEMPLO 
iqr = iqr(msleep['bodywt'])
lower_threshold = np.quantile(msleep['bodywt'],0.25)-1.5*iqr
upper_threshold = np.quantile(msleep['bodywt'],0.75)+1.5*iqr

# print(msleep[(msleep['bodywt'] < lower_threshold) | (msleep['bodywt'] > upper_threshold)])

#! LA MAYORIA SE PUEDE CALCULAR CON UN DESCRIBE
print(msleep['bodywt'].describe())


