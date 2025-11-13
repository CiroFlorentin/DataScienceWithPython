import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

dogs = pd.read_csv(csv_path)


dogs_pivot = dogs.pivot_table('height_cm', index='breed', columns='color',fill_value=0)
# print(dogs_pivot)
# print(dogs_pivot.mean(axis='index'))
