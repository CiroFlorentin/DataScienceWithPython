import os
import pandas as pd



script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_movies = os.path.join(script_dir, "src/Movies", "movies.csv")
csv_path_taglines = os.path.join(script_dir, "src/Movies", "taglines.csv")

movies = pd.read_csv(csv_path_movies, index_col=0)
taglines = pd.read_csv(csv_path_taglines)


#! Left Join one to one
movies_taglines = movies.merge(taglines, on="id", how="left")

# ? Show first 5 rows
# print(movies_taglines.head())

# ? Count NaN values
print(movies_taglines['tagline'].isna().sum())