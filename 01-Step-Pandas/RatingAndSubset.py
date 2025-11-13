import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "dogs.csv")

df = pd.read_csv(csv_path)

# print(df.sort_values("weight_kg"))
# print(df.sort_values(["weight_kg", "height_cm"], ascending=[True,False])) 

is_lab=df['breed'] == 'Labrador'
is_brown=df["color"] == 'Brown'

dog = df[is_lab & is_brown] # & is the and operator

# print(dog)
is_black_or_brown = df['color'].isin(['Black', 'Brown']) # isin is the in operator 


# print(df[is_black_or_brown])

# ! PARA AÑADIR COLUMNAS
df['height_m'] = df['height_cm'] / 100
df['BMI'] = df['weight_kg'] / (df['height_m'] ** 2)

bmi_lt_100 = df[df['BMI'] < 100]
bmi_lt_100_height= bmi_lt_100.sort_values('height_cm', ascending=False)

# print(bmi_lt_100_height[['name','height_cm','BMI']])

