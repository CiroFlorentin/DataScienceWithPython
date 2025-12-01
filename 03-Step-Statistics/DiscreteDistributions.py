import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'src', 'die.csv')
csv_path2 = os.path.join(script_dir, 'src', 'restaurant_groups.csv')

die = pd.read_csv(csv_path)
restaurant_groups = pd.read_csv(csv_path2)

# np.random.seed(42)

# print(die['number'].mean())
# rolls_10 = die.sample(1000, replace=True)

# rolls_10['number'].hist(bins=np.linspace(1,7,7))

# plt.show()

#! TODO: diferencia entre la tiradas y la teórica
# print(rolls_10['number'].mean())
# print(die['number'].mean())
#* CUAN MAYOR EL TAMAÑO MUESTRAL, MAS CERCANO SE APLICA LA LEY DE LA MEDIA

#? Example
restaurant_groups['group_size'].hist(bins=[2,3,4,5,6])
# plt.show()

# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size']>= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])

