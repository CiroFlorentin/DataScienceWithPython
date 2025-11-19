import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

final_tails= [0]

for x in range(10000):
    tails= [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])

final_tails = np.array(final_tails)
promedio =sum(final_tails[final_tails >= 4])/10000
print(promedio)

plt.hist(final_tails, bins = 10)
plt.show()
