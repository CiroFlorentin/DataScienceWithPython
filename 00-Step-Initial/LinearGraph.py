import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

#! Gráfico Lineal

plt.plot(year,pop)  #Horizontal / Vertical
plt.show()
plt.clf() #Borra el gráfico actual

# Scatter Plot

plt.scatter(year, pop)
plt.show()