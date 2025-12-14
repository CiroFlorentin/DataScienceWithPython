import matplotlib.pyplot as plt
import numpy as np

year = np.arange(1950, 2101)

# Procedural con crecimiento gradual y algo de variación
rng = np.random.default_rng(seed=42)
base = np.linspace(2, 12, num=151)
noise = rng.uniform(-0.3, 0.3, size=151)  # Pequeña variación aleatoria
pop = base + noise
pop = np.clip(pop, 2, 12)  



plt.plot(year, pop)


plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth")
plt.yticks([0,2, 4, 6, 8, 10, 12],['0','2B','4B','6B','8B','10B','12B'])
plt.text(2000, 10, "Population Growth")
plt.grid(True)

plt.show()

