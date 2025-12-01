import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path_movies = os.path.join(script_dir, 'src/Movies/movies.csv')
csv_path_genres = os.path.join(script_dir, 'src/Movies/movie_to_genres.csv')


movies = pd.read_csv(csv_path_movies ,index_col=0)
movie_to_genres = pd.read_csv(csv_path_genres ,index_col=0)

# ! Right Join
tv_genres = movie_to_genres[movie_to_genres['genre'] == 'TV Movie']
tv_movies = movies.merge(tv_genres, how='right', left_on='id', right_on='movie_id')

# print(tv_movies.head())

#! Outer Join
family = movie_to_genres[movie_to_genres['genre'] == 'Family'].head(3)
comedy = movie_to_genres[movie_to_genres['genre'] == 'Comedy'].head(3)

family_comedy = family.merge(comedy, on='movie_id', how='outer',suffixes=('_fam', '_com'))
print(family_comedy)

