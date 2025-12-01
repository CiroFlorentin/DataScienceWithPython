

#? Relación entre variables
#* x = variable independiente/explicativa
#* y = variable dependiente/respuesta

#? Coeficiente de correlación
#* Indica la fuerza y dirección de la relación entre variables
#* Número entre -1 y 1 
#* La magnitud indica la fuerza de la relación
#* El signo indica la dirección de la relación

#? Visualización de correlación
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt

csv_path = os.path.join(os.path.dirname(__file__), 'src', 'sleep.csv')
msleep = pd.read_csv(csv_path)

#* sns.scatterplot(x='x', y='y', data=df)
# sns.scatterplot(x='sleep_total', y ='sleep_rem', data=msleep)
# sns.lmplot(x='sleep_total', y ='sleep_rem', data=msleep, ci=None)  #ci=None quita la linea de confianza
# plt.show()

#? Calcular correlación
#* Correlación producto-cociente dePearson
#* mide la relación lineal entre variables continuas y aproximadamente normales. Sensible a outliers
print(msleep['sleep_total'].corr(msleep['sleep_rem'])) # da igual el orden de las variables


#* Correlación de Spearman
#* Basado en rango, detectando relaciones monótonas e ideal cuando hay outliers o distribuciones no normales
print(msleep['sleep_total'].corr(msleep['sleep_rem'], method='spearman'))

#* Correlación de Kendall
#* Mide concordancia entre rangos, ideal para variables ordinales
print(msleep['sleep_total'].corr(msleep['sleep_rem'], method='kendall'))

#! Ejemplo 
csv_path_world = os.path.join(os.path.dirname(__file__), 'src', 'world_happiness.csv')
world_happiness = pd.read_csv(csv_path_world)

# sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)
# plt.show()

# print(world_happiness['life_exp'].corr(world_happiness['happiness_score']))