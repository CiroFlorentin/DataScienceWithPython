import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import poisson

#* El número de eventos que ocurren en un intervalo de tiempo o espacio.
#* El proceso de Poisson es un proceso de conteo que describe el numero de eventos que ocurren en un intervalo de tiempo o espacio.
#* La probabilidad de que ocurra un número determinado de sucesos en un período de tiempo fijo ( lambda )


#? poisson.pmf(valorUnico, lambda) probabilidad de que ocurra un valor único
print(poisson.pmf(5,8))

#? poisson.cdf(valor, lambda) probabilidad de que ocurra un valor mayor o igual que
print(poisson.cdf(5,8))

#? 1 - poisson.cdf(valor, lambda) probabilidad de que ocurra un valor menor o igual que
print(1 - poisson.cdf(5,8))


#? muestreo a partir de una distribución de poisson poisson.rvs(lambda, size)
print(poisson.rvs(8, size=10))


#! Ejemplo
print(poisson.pmf(5,4))
print(poisson.pmf(5,5.5))
print(poisson.cdf(2,4))
print(1 - poisson.cdf(10,4))