import matplotlib.pyplot as plt
import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), 'src', 'climate_change.csv')
climate_change = pd.read_csv(csv_path, parse_dates=['date'], index_col='date')


# fig,ax = plt.subplots()

# ax.plot(climate_change.index, climate_change['co2'], color='b')
# ax.set_xlabel('Time')
# ax.set_ylabel('CO2 (ppm) ', color='b')
# ax.tick_params('y', colors='b')

# ax2 = ax.twinx()
# ax2.plot(climate_change.index, climate_change['relative_temp'], color='r')
# ax2.set_ylabel('Relative temperature (Celsius)', color='r')
# ax2.tick_params('y', colors='r')
# plt.show()


# #? zooming in on a specific time period
# sixties = climate_change['1960-01-01':'1969-12-31']

# ax.plot(sixties.index, sixties['co2'])
# ax.set_xlabel('Time')
# ax.set_ylabel('CO2 (ppm)')
# plt.show()

# sixty_nine = climate_change['1969-01-01':'1969-12-31']

# ax.plot(sixty_nine.index, sixty_nine['co2'])
# ax.set_xlabel('Time')
# ax.set_ylabel('CO2 (ppm)')
# plt.show()

#! Crear funcion para graficar
def plot_timeseries (ax , x , y, color, xlabel, ylabel):
    ax.plot(x, y, color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel, color=color)
    ax.tick_params('y', colors=color)
    
fig,ax = plt.subplots()

plot_timeseries(ax, climate_change.index, climate_change['co2'], 'b', 'Time', 'CO2 (ppm)')
ax2 = ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'r', 'Time', 'Relative temperature (Celsius)')
# plt.show()



#? annotations  xy=(pd.Timestamp(time), value)
ax2.annotate('>1 degree', xy= (pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2),arrowprops = {'arrowstyle':'->', 'color':'gray'})

plt.show()