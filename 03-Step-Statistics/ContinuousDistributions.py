import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import uniform


#! TODO: probabilidad de esperar menos de 7 minutos, (tiempo, min, max)
print(uniform.cdf(7,0,12))

#! TODO: probabilidad de esperar mas de 7 minutos
print(1 - uniform.cdf(7,0,12))

#? Esperar entre 4 y 7 minutos
print(uniform.cdf(7,0,12) - uniform.cdf(4,0,12))

#! TODO: Generar números aleatorios según distribution uniforme (min, max, size)
print(uniform.rvs(0,5, size=10))


#* PRACTICA:

np.random.seed(334)

min_time = 0
max_time = 30

prob_less_than_5 = uniform.cdf(5, min_time, max_time)

prob_greater_than_5 = 1 - uniform.cdf(5,min_time,max_time)

prob_between_10_and_20 = uniform.cdf(20,min_time,max_time) - uniform.cdf(10,min_time,max_time)


wait_times = uniform.rvs(0,30,size = 1000)

plt.hist(wait_times,)
plt.show()