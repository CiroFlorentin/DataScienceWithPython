import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import binom


#? El número de éxitos en un número fijo de intentos.

#* binom.rvs(# monedas, probabilidad de éxito, size = # simulaciones)

# print ( binom.rvs(1, 0.5, size = 1) ) #* 1 moneda, 50% de éxito, 1 simulación
# print(binom.rvs(1,0.5, size = 8)) #* 1 moneda, 50% de éxito, 8 simulaciones
# print(binom.rvs(8,0.5, size = 1)) #* 8 monedas, 50% de éxito, 1 simulación
# print(binom.rvs(3,0.5, size = 10)) #* 3 monedas, 50% de éxito, 10 simulaciones
# print(binom.rvs(3,0.25, size = 10)) #* 3 monedas, 25% de éxito, 10 simulaciones

#* binom.pmf(# éxitos, # monedas, probabilidad de éxito)  P(éxito = # éxitos)
# print(binom.pmf(7,10,0.5)) #* 7 éxitos, 10 monedas, 50% de éxito

#* binom.cdf(# éxitos, # monedas, probabilidad de éxito)  P(éxito <= # éxitos)
# print(binom.cdf(7,10,0.5)) #* 7 éxitos, 10 monedas, 50% de éxito

#* binom.sf(# éxitos, # monedas, probabilidad de éxito)  P(éxito > # éxitos)
# print(binom.sf(7,10,0.5)) #* 7 éxitos, 10 monedas, 50% de éxito

# * Valor esperado (expected value = n * p)
# print(10*0.5)

#! EJEMPLO:

np.random.seed(10)

single_deal = binom.rvs(1, 0.3, size=1)

deals_single_week = binom.rvs(3, 0.3, size=1)

deals_52_weeks = binom.rvs(3, 0.3, size=52)

#? Media de acuerdos por semana
print(deals_52_weeks.mean())

prob_3_deals = binom.pmf(3, 3, 0.3)

prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)

prob_more_than_1 = binom.sf(1, 3, 0.3) #* También se puede usar  1 - binom.cdf(1, 3, 0.3)

won_30pct = 3 * 0.3

won_25pct = 3 * 0.25

won_35pct = 3 * 0.35