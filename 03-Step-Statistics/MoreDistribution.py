import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


#! Distribucion exponencial
# * Probabilidad de tiempo entre sucesos de Poisson
#* El tiempo entre dos eventos que ocurren a una tasa Poisson.

from scipy.stats import expon

#? expon.cdf(tiempo, scale=1/lambda) probabilidad de esperar x tiempo menos  
print(expon.cdf(1, scale=2))

#? 1 -  expon.cdf(tiempo, scale=1/lambda) probabilidad de esperar x tiempo mas
print(1 - expon.cdf(4, scale=2))

#? expon.cdf(x, scale=1/lambda) -  expon.cdf(y, scale=1/lambda) probabilidad de esperar entre x y y tiempo
print(expon.cdf(4, scale=2) - expon.cdf(1, scale=2))


#! Distribucion T (de Student)
#* menos df = mayor desviación típica
#* mas df = más cerca de la distribución normal 
from scipy.stats import t

#? t.cdf(x, df=(grados de libertad)) probabilidad de esperar x tiempo menos
print(t.cdf(1, df=1))

#? 1 - t.cdf(x, df=(grados de libertad)) probabilidad de esperar x tiempo mas
print(1 - t.cdf(1, df=1))

#? t.cdf(x, df) - t.cdf(y, df) probabilidad de esperar entre x y y tiempo
print(t.cdf(1, df=1) - t.cdf(0, df=1))

#! Distribución normal logarítmica
#* Distribución normal de variables que crecen exponencialmente
from scipy.stats import lognorm

#? lognorm.cdf(x, s=(desviación típica), scale=(media)) 
print(lognorm.cdf(1, s=1, scale=2))

#? 1 - lognorm.cdf(x, s=(desviación típica), scale=(media))
print(1 - lognorm.cdf(1, s=1, scale=2))

#? lognorm.cdf(x, s=, scale=) - lognorm.cdf(y, s= scale=)
print(lognorm.cdf(1, s=1, scale=2) - lognorm.cdf(0, s=1, scale=2))


#! Ejemplo
print(expon.cdf(1, scale=2.5))
print(1- expon.cdf(4,scale=2.5))
print(expon.cdf(4,scale=2.5) - expon.cdf(3,scale=2.5))