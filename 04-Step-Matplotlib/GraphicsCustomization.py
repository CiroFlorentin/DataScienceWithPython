import matplotlib.pyplot as plt
import os
import pandas as pd


csv_path_austin = os.path.join(os.path.dirname(__file__), 'src', 'austin_weather.csv')


austin_weather = pd.read_csv(csv_path_austin)

fig, ax = plt.subplots()
ax.plot(austin_weather['DATE'], austin_weather['MLY-TAVG-NORMAL'],marker='v',linestyle='--',color='r')
ax.set_xlabel('Time (months)')
ax.set_ylabel('Average temperature (F)')
ax.set_title('Austin Weather')
ax.set_xticks(range(0, len(austin_weather['DATE']))) #Setea los valores del eje x
ax.set_xticklabels(('Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar')) #Cambia los valores del eje x
plt.show() 