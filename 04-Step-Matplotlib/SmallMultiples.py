import matplotlib.pyplot as plt
import os
import pandas as pd

csv_path_austin = os.path.join(os.path.dirname(__file__), 'src', 'austin_weather.csv')
csv_path_seattle = os.path.join(os.path.dirname(__file__), 'src', 'seattle_weather.csv')

austin_weather = pd.read_csv(csv_path_austin)
seattle_weather = pd.read_csv(csv_path_seattle)

fig, ax = plt.subplots(2,1,sharex=True,sharey=True)
ax[0].plot(austin_weather['DATE'], austin_weather['MLY-PRCP-NORMAL'],color='b')
ax[0].plot(austin_weather['DATE'], austin_weather['MLY-PRCP-25PCTL'],color='b',linestyle='--')
ax[0].plot(austin_weather['DATE'], austin_weather['MLY-PRCP-75PCTL'],color='b',linestyle='--')

ax[1].plot(seattle_weather['DATE'], seattle_weather['MLY-PRCP-NORMAL'],color='g')
ax[1].plot(seattle_weather['DATE'], seattle_weather['MLY-PRCP-25PCTL'],color='g',linestyle='--')
ax[1].plot(seattle_weather['DATE'], seattle_weather['MLY-PRCP-75PCTL'],color='g',linestyle='--')

ax[0].set_xticks(range(0, len(austin_weather['DATE']))) 
ax[0].set_xticklabels(('Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar')) 



ax[0].set_xlabel('Time (months)')
ax[0].set_ylabel('Precipitation (inches)')

ax[1].set_xlabel('Time (months)')
ax[1].set_ylabel('Precipitation (inches)')

plt.show()
