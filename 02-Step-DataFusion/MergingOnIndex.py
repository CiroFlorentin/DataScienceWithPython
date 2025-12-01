import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path_movies = os.path.join(script_dir, 'src/Movies/movies.csv')
csv_path_taglines = os.path.join(script_dir, 'src/Movies/taglines.csv')
csv_path_genres = os.path.join(script_dir, 'src/Movies/movie_to_genres.csv')

taglines = pd.read_csv(csv_path_taglines, index_col=['id'])

genres = pd.read_csv(csv_path_genres, index_col=['movie_id'])
genres = genres.drop(columns=['Unnamed: 0'])

movies = pd.read_csv(csv_path_movies, index_col=['id'])
movies = movies.drop(columns=['Unnamed: 0'])

# movies_taglines = movies.merge(taglines,on='id',how='left')

movies_genres = movies.merge(genres, left_index=True, right_index=True)

print(movies_genres.head())
# print(movies_taglines.head())

