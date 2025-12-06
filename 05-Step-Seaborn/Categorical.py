import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
from numpy import median

masculinity = pd.read_csv(os.path.join(os.path.dirname(__file__), "src", "masculinity.csv"))

#? Graficos categóricos 
#* incluye una variable categórica y habitualmente se hace comparaciones entre grupos
#! Grafico de recuento
cat_order = ['No answer','Not at all','Not very','Somewhat','Very']

sns.catplot(data=masculinity, x="how_masculine", kind="count", hue='how_masculine', order=cat_order)
# plt.show()
plt.close()
#! Grafico de barras

tips= sns.load_dataset("tips")

sns.catplot(data=tips, x="day", y="total_bill", kind="bar", hue='day') # La variable categórica se coloca en el eje x y la variable cuantitativa en el eje y
# plt.show()
plt.close()

#! Diagrama de cajas

sns.catplot(data=tips, x='day', y='total_bill', kind='box', hue='day') #whis define los bigotes (IQR)
# plt.show()
plt.close()

#! Grafico de puntos


masculinity['feel_masculine'] =  masculinity['how_masculine'].apply(lambda x: True if x == 'Very' or x == 'Somewhat' else False)

sns.catplot(data=masculinity, x='age', y='how_important', kind='point', hue='feel_masculine',join=False) 
# plt.show()
plt.close()

sns.catplot(data=tips, x='smoker',y='total_bill', kind='point', estimator=median, capsize=0.2)
plt.yticks(range(0,26,5))
# plt.show()
plt.close()