import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


csv_path_schools= os.path.join(os.path.dirname(__file__),"src", "schools.csv")
schools_df= pd.read_csv(csv_path_schools)

# 1
filter_avg = schools_df[schools_df['average_math'] >= 800 * 0.8]
best_math_schools = filter_avg[['school_name', 'average_math']].sort_values('average_math', ascending=False)
# print(best_math_schools)

#! Extra
fig,ax = plt.subplots()
ax.bar(best_math_schools['school_name'], best_math_schools['average_math'])
ax.set_title('Best Math Schools')
ax.set_xlabel('School Name')
ax.set_ylabel('Average Math Score')
ax.set_yticks(range(0, max(best_math_schools['average_math']) + 10, 250))
ax.set_xticks(range(len(best_math_schools['school_name'])),labels = best_math_schools['school_name'], rotation=90)

fig.set_size_inches(8,6)
fig.savefig("Projects/NYC_V2/src/best_math_schools.svg",dpi=300)

plt.close(fig)

# 2
schools_df['total_SAT'] = schools_df['average_math'] + schools_df['average_reading'] + schools_df['average_writing']
top_10_schools = schools_df[['school_name', 'total_SAT']].sort_values('total_SAT', ascending=False).head(10)
# print(top_10_schools)

#! Extra
fig,ax = plt.subplots()
ax.bar(top_10_schools['school_name'], top_10_schools['total_SAT'])
ax.set_title('Top 10 Schools by Total SAT Score')
ax.set_xlabel('School Name')
ax.set_ylabel('Total SAT Score')
ax.set_yticks(range(0, max(top_10_schools['total_SAT']) + 10, 250))
ax.set_xticks(range(len(top_10_schools['school_name'])),labels = top_10_schools['school_name'], rotation=90)

fig.set_size_inches(8,6)
fig.savefig("Projects/NYC_V2/src/top_10_schools.svg",dpi=300)

plt.close(fig)


# 3
largest_std_dev = schools_df.groupby('borough').agg(
    num_schools = ('school_name', 'count'),
    average_SAT = ('total_SAT', 'mean'),
    std_SAT = ('total_SAT', 'std')
).round(2).sort_values('std_SAT', ascending=False)
largest_std_dev = largest_std_dev.reset_index()
# print(largest_std_dev)


#! Extra 
boroughs = largest_std_dev['borough'].unique()

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

for borough in boroughs:
    borough_df = largest_std_dev[largest_std_dev['borough'] == borough]
    ax.bar(borough,borough_df['average_SAT'], yerr=borough_df['std_SAT'])

ax.set_ylabel('SAT Score')
ax.set_title('Average SAT Score by Borough')
ax.set_xticks(range(len(boroughs)),labels = boroughs, rotation=45, ha='center')

fig.set_size_inches(10,8)
fig.savefig("Projects/NYC_V2/src/boroughs_sat.svg",dpi=300)

