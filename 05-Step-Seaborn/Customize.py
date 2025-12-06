import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


tips = sns.load_dataset('tips')
sns.set_style('darkgrid') #dark , white , ticks, whitegrid, darkgrid
sns.set_context('notebook') #paper, notebook, talk, poster (rc = {}) (font_scale = float)
sns.set_palette('husl') #husl, deep, muted, bright, pastel, dark, colorblind

sns.catplot(data=tips, x='smoker',y='total_bill', kind='point')
plt.yticks(range(0,26,5))
# plt.show()
plt.close()


country = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'countries-of-the-world.csv'))

#! limpiar columnas
country.columns = country.columns.str.strip()
country['Region'] = country['Region'].str.strip()
country['Birthrate'] = country['Birthrate'].astype(str).str.replace(',', '.').astype(float)

g = sns.catplot(data=country, x='Region', y='Birthrate', kind='box',hue='Region')
g.fig.suptitle('Birthrate by Region', y=1)
# g.set_titles('this is 1')
g.set(xlabel='Region', ylabel='Birthrate')
g.set_xticklabels(rotation=90)
# plt.show()
plt.close()

#! Ejercicio
survey_data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'young-people-survey-responses.csv'))

sns.set_palette('Blues')
g = sns.catplot(data=survey_data, x='Gender', y='Age', kind='box', hue='Pets')
g.fig.suptitle('Age of Those Interested in Pets')
g.fig.savefig('05-Step-Seaborn/src/Age of Those Interested in Pets.svg')
plt.close()


sns.set_palette('dark')
g = sns.catplot(data=survey_data, x='Village - town',y='Techno', kind='bar', col='Gender',hue='Village - town')
g.fig.suptitle("Percentage of Young People Who Like Techno",y=1)
g.fig.savefig('05-Step-Seaborn/src/Percentage of Young People Who Like Techno.svg')
plt.close()

