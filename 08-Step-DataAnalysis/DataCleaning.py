import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'ds_salaries_clean.csv'))


sns.boxplot(data=df,x='Experience',y='Salary_USD',hue='Experience',order=['Executive','Senior','Mid','Entry'])
# plt.show()
plt.close()

# print(df.isna().sum())

threshold = len(df)*0.05
# print(threshold)

#! Eliminar columnas con valores nulos mayor al threshold (5%)
cols_to_drop = df.columns[df.isna().sum() <= threshold]
# print(cols_to_drop)

#! Eliminar nulos de las columnas seleccionadas
df.dropna(subset=cols_to_drop, inplace=True)

cols_with_missing_values= df.columns[df.isna().sum() > 0]
# print(cols_with_missing_values)

df_dict = df.groupby('Experience')['Salary_USD'].median().to_dict()
# print(df_dict)

df['Salary_USD'] = df['Salary_USD'].fillna(df['Experience'].map(df_dict))


#! Convertir y analizar datos categóricos


# print(df.select_dtypes('object').head())


top_5_professions = df['Designation'].value_counts().head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_professions.index, y=top_5_professions.values, hue=top_5_professions.index)
plt.title('Top 5 Profesiones con más empleados')
plt.xlabel('Profesión')
plt.ylabel('Cantidad de Profesionales')
plt.xticks(rotation=45)
# plt.show()
plt.close()


#! Extraer valores de categorías
# print(df['Designation'].str.contains('Scientist|AI'))

# print(df['Designation'].str.contains('^Data')) # Empieza con Data
# print(df['Designation'].str.contains('Data$')) # Termina con Data

job_categories = ['Data Science','Data Analytics','Data Engineering','Machine Learning','Managerial','Consultant']


data_science = 'Data Scientist|NLP'
data_analyst =  'Analyst|Analytics'
data_engineering = 'Data Engineer|ETL|Architect|Infrastructure'
ml_engineer = 'Machine Learning|ML|Big Data|AI'
manager = 'Manager|Head|Director|Lead|Principal|Staff'
consultant = 'Consultant|Freelance'

conditions = [
    (df['Designation'].str.contains(data_science)),
    (df['Designation'].str.contains(data_analyst)),
    (df['Designation'].str.contains(data_engineering)),
    (df['Designation'].str.contains(ml_engineer)),
    (df['Designation'].str.contains(manager)),
    (df['Designation'].str.contains(consultant))
]
df['job_category'] = np.select(conditions, job_categories, default='Other')

# print(df[['Designation','job_category']].head())


sns.countplot(data=df,x='job_category', hue="job_category")
plt.xticks(rotation=45)
# plt.show()
plt.close()

#! Datos Numéricos
# pd.Series.str.replace('Caracter a remover', 'Caracter de reemplazo')

df['std_dev'] = df.groupby('Experience')['Salary_USD'].transform(lambda x: x.std())
# print(df[['Experience','std_dev']].value_counts())

df['median_by_comp_size'] = df.groupby('Company_Size')['Salary_USD'].transform(lambda x: x.median())
# print(df[['Company_Size','median_by_comp_size']].value_counts())


#! Outliers
# print(df['Salary_USD'].describe())

IQR = df['Salary_USD'].quantile(0.75) - df['Salary_USD'].quantile(0.25)

lower_bound = df['Salary_USD'].quantile(0.25) - 1.5 * IQR
upper_bound = df['Salary_USD'].quantile(0.75) + 1.5 * IQR

outliers = df[(df['Salary_USD'] < lower_bound) | (df['Salary_USD'] > upper_bound)]\
    [['Experience','Salary_USD','Employee_Location']]
# print(outliers)

#*¨Una vez q los identificamos, nos preguntamos que hacemos con estos
#* Primero nos preguntamos cosas:
#* ¿Por que existen?
#* ¿Son Datos precisos?

#? Eliminar Outliers
no_outliers = df[(df['Salary_USD'] >= lower_bound) & (df['Salary_USD'] <= upper_bound)]

# print(no_outliers['Salary_USD'].describe())

fig, ax = plt.subplots(1,2, figsize=(12,6))
sns.histplot(data=df,x='Salary_USD',kde=True,ax=ax[0])
sns.histplot(data=no_outliers,x='Salary_USD',kde=True,ax=ax[1])
plt.show()
plt.close()

#* Vemos que se parece mas a una distribucion normal 