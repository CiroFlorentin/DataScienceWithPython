import numpy as np
import pandas as pd
import os

world = {
    'Afghanistan' : 30.55,
    'Albania' : 2.77,
    'Algeria' : 39.21
}

# for key,value in world.items():
#     print(key + " -- " + str(value))


height = np.array([1.73,1.68,1.71,1.89,1.79])
weight = np.array([65.4,59.2,63.6,88.4,68.7])
meas = np.array([height,weight])

# Se imprime como dos matrices 1D
# for val in meas:
#     print(val)

# Se imprime como una matriz 2D
# for val in np.nditer(meas):
#     print(val)


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "brics.csv")

BRICS = pd.read_csv(csv_path, index_col=0)

# ! UNA FORMA PERO NO EFICIENTE
# for lab,row in BRICS.iterrows():
#     BRICS.loc[lab,"name_length"] = len(row["country"])

# ! UNA FORMA EFICIENTE
BRICS["name_length"] = BRICS["country"].apply(len)

print(BRICS)