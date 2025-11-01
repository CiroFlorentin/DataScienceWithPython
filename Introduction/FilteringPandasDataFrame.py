import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "brics.csv")

BRICS = pd.read_csv(csv_path, index_col=0)

# # Step 1 : Get Column
# is_huge = BRICS.loc[:, "area"] > 8
is_huge = np.logical_and(BRICS.iloc[:, 2] > 8, BRICS.iloc[:, 2] < 10)

# # Step 2 : Subset DF
print(BRICS[is_huge])

# ExtraStep : Filter in a line
# print(BRICS[BRICS.iloc[:, 2] > 8])


