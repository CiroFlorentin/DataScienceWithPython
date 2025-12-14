import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np


divorce = pd.read_csv(os.path.join(os.path.dirname(__file__),"src", "divorce.csv"),parse_dates=['divorce_date','dob_man','dob_woman','marriage_date']) 

# print(divorce.head())

df = divorce[['marriage_date','marriage_duration']].copy()

# df['marriage_date'] = pd.to_datetime(df['marriage_date'])
# print(df.dtypes)


# print(df['marriage_date'].dt.year[0])
# print(df['marriage_date'].dt.month[0])
# print(df['marriage_date'].dt.day[0])


sns.lineplot(data = df, x=df['marriage_date'].dt.month, y='marriage_duration')
# plt.show()
plt.close()

divorce['marriage_year'] = divorce['marriage_date'].dt.year

sns.lineplot(data = divorce, x='marriage_year', y='num_kids')
# plt.show()
plt.close()

#! correlación
# print(divorce.corr(numeric_only=True))

sns.heatmap(divorce.corr(numeric_only=True), annot =True)
plt.tight_layout() 
# plt.show()
plt.close()

# print(divorce['divorce_date'].min())
# print(divorce['divorce_date'].max())

sns.scatterplot(data = divorce, x='income_man', y='income_woman')
plt.tight_layout()
# plt.show()
plt.close()


sns.pairplot(data = divorce ,vars = ['income_man','income_woman','marriage_duration'])
plt.tight_layout()
# plt.show()
plt.close()

#! Variables Categóricas
# print(divorce['education_man'].value_counts())

#* No se ve del todo clara si hay relación entre la educación y la duración de la union
sns.histplot(data = divorce, x='marriage_duration',hue='education_man' ,binwidth=1, palette='husl')
plt.tight_layout()
# plt.show()
plt.close()

sns.kdeplot(data = divorce, x='marriage_duration',hue='education_man', palette='husl',cut=0, cumulative=True)
plt.tight_layout()
# plt.show()
plt.close()


divorce['man_age_marriage'] = divorce['marriage_year'] - divorce['dob_man'].dt.year
divorce['woman_age_marriage'] = divorce['marriage_year'] - divorce['dob_woman'].dt.year

sns.scatterplot(data = divorce, x='woman_age_marriage', y='man_age_marriage',hue='education_man')
plt.tight_layout()
# plt.show()
plt.close()