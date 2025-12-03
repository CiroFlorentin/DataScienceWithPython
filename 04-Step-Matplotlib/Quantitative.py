import os 
import matplotlib.pyplot as plt
import pandas as pd


csv_path_medals = os.path.join(os.path.dirname(__file__), 'src', 'medals_by_country_2016.csv')
medals = pd.read_csv(csv_path_medals, index_col=0)

csv_path_olympics = os.path.join(os.path.dirname(__file__), 'src', 'summer2016.csv')
olympics = pd.read_csv(csv_path_olympics, index_col=0)

#! Bar chart

# fig, ax = plt.subplots()
# ax.bar(medals.index, medals['Gold'], color='gold')
# ax.bar(medals.index, medals['Silver'], bottom=medals['Gold'], color='silver')
# ax.bar(medals.index, medals['Bronze'], bottom=medals['Gold'] + medals['Silver'], color='brown')

# ax.set_xticklabels(medals.index, rotation=90)
# ax.set_ylabel('Number of medals')
# ax.legend(['Gold', 'Silver', 'Bronze'])
# plt.show()

#! Histogram
# mens_rowing= olympics[(olympics['Sport'] == 'Rowing') & (olympics['Sex'] == 'M')]
# mens_gymnastics= olympics[(olympics['Sport'] == 'Gymnastics') & (olympics['Sex'] == 'M')]

# fig,ax = plt.subplots()
# #? Forma fea
# # ax.bar('Rowing', mens_rowing['Height'].mean())
# # ax.bar('Gymnastics', mens_gymnastics['Height'].mean())
# ax.hist(mens_rowing['Height'], label='Rowing',bins=[150,160,170,180,190,200,210], histtype='step')
# ax.hist(mens_gymnastics['Height'], label='Gymnastics',bins=[150,160,170,180,190,200,210], histtype='step')

# ax.set_xlabel('Height (cm)')
# ax.set_ylabel('# of observations')
# ax.legend()

# plt.show()

#! Scatter plot

csv_path_climates = os.path.join(os.path.dirname(__file__), 'src', 'climate_change.csv')
climate_change = pd.read_csv(csv_path_climates, parse_dates=['date'], index_col='date')

fig, ax = plt.subplots()

# ax.scatter(climate_change['co2'], climate_change['relative_temp'])
# ax.set_xlabel('CO2 (ppm)')
# ax.set_ylabel('Relative temperature (C)')
# plt.show()

#? Mostrar dos datos 
# eighties = climate_change['1980-01-01':'1989-12-31']
# nineties = climate_change['1990-01-01':'1999-12-31']

# ax.scatter(eighties['co2'], eighties['relative_temp'], label='80s', color='red')
# ax.scatter(nineties['co2'], nineties['relative_temp'], label='90s', color='blue')
# ax.set_xlabel('CO2 (ppm)')
# ax.set_ylabel('Relative temperature (C)')
# ax.legend(loc = 'upper left')
# plt.show()

#? encoding a third variable by color
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c=climate_change.index, alpha=0.6)

ax.set_xlabel('CO2 (ppm)')
ax.set_ylabel('Relative temperature (C)')
plt.show()
