import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'src', 'amir_deals.csv')

amir_deals = pd.read_csv(csv_path)

counts = amir_deals['product'].value_counts()

probs = counts / amir_deals.shape[0]

#? ESTABLECER SEMILLA
np.random.seed(24)


sample_without_replacement = amir_deals.sample(5)

sample_with_replacement = amir_deals.sample(5, replace=True)

