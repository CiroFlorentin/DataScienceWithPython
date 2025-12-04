import os
import pandas as pd
import matplotlib.pyplot as plt


csv_path_summer = os.path.join(os.path.dirname(__file__), 'src', 'summer2016.csv')
summer2016 = pd.read_csv(csv_path_summer)

sport = summer2016['Sport'].unique()
print(sport)

fig, ax = plt.subplots()

for sports in sport:
    sport_df = summer2016[summer2016['Sport'] == sports]
    ax.bar(sports,sport_df['Height'].mean(), yerr=sport_df['Height'].std())
    
ax.set_ylabel('Height (cm)')
ax.set_title('Average Height by Sport')
ax.set_xticks(range(len(sport)), labels=sport, rotation=90, ha='center')
fig.savefig("04-Step-Matplotlib/src/sports_weights.svg")
fig.savefig("04-Step-Matplotlib/src/sports_height.svg")