import matplotlib.pyplot as plt
import os
import pandas as pd

csv_path_seattle = os.path.join(os.path.dirname(__file__), 'src', 'seattle_weather.csv')
seattle_weather = pd.read_csv(csv_path_seattle)

csv_path_austin = os.path.join(os.path.dirname(__file__), 'src', 'austin_weather.csv')
austin_weather = pd.read_csv(csv_path_austin)


plt.style.use('bmh')

fig,ax = plt.subplots()


ax.plot(seattle_weather['DATE'], seattle_weather['MLY-TAVG-NORMAL'])
ax.plot(austin_weather['DATE'], austin_weather['MLY-TAVG-NORMAL'])

ax.set_xlabel('Time (Months)')
ax.set_ylabel('Average Temperature (Fahrenheit)')


fig.set_size_inches([5,4])
fig.savefig('04-Step-Matplotlib/src/weather.svg', dpi=300) #jpg png pdf svg  | quality = 1 - 100 | dpi = 100 - 300
