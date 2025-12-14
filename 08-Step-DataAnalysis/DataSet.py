import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#! Exploración inicial
books = pd.read_csv(os.path.join(os.path.dirname(__file__),'src','clean_books.csv'))

# print(books.head())
# print(books.info())

#! Mirar columnas categóricas
# print(books.value_counts('genre '))

# print(books.describe())

#! Visualizar datos numéricos

sns.histplot(data=books,x='rating', binwidth=.1)
# plt.show()
plt.close()

#! Validación de datos

# print(books.dtypes)

# print(books[books['genre'].isin(['Fiction','Non Fiction'])].head())

sns.boxplot(data=books,x='year',y='genre',hue='genre')
# plt.show()
plt.close()


#! Data summary
# print(books[['genre','rating','year']].groupby('genre').mean())
# print(books[['rating','year']].agg(['mean','std']))

# print(books.agg({'rating':['mean','std'],'year':'median'}))

group = books.groupby('genre').agg(
    mean_rating=('rating','mean'),
    std_rating=('rating','std'),
    median_year=('year','median')
)
print(group)