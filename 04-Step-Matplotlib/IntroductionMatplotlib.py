import matplotlib.pyplot as plt
import os
import pandas as pd

csv_path_seattle = os.path.join(os.path.dirname(__file__), 'src', 'seattle_weather.csv')
csv_path_austin = os.path.join(os.path.dirname(__file__), 'src', 'austin_weather.csv')

seattle_weather = pd.read_csv(csv_path_seattle)
austin_weather = pd.read_csv(csv_path_austin)

fig, ax = plt.subplots()
ax.plot(seattle_weather['DATE'], seattle_weather['MLY-TAVG-NORMAL'])
ax.plot(austin_weather['DATE'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()