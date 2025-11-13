import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

# ? Leer el archivo CSV
# news_dogs = pd.read_csv(csv_path)

# news_dogs['BMI'] = news_dogs['weight_kg'] / (news_dogs['height_cm'] / 100) ** 2

# ? Guardar el DataFrame en un archivo CSV
# news_dogs.to_csv(os.path.join(script_dir, "src", "dogsWithBMI.csv"), index=False)