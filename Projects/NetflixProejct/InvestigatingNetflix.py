import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "netflix_data.csv")

netflix_df = pd.read_csv(csv_path, index_col=0)
# ! Consigna 1:
netflix_df.loc[:, 'duration'] = pd.to_numeric(netflix_df.loc[:, 'duration'])

filter_netflix_decade= np.logical_and(
    netflix_df.loc[:, 'type'] == 'Movie', 
        np.logical_and(
            netflix_df.loc[:, 'release_year'] >= 1990,
            netflix_df.loc[:, 'release_year'] < 2000)
        )

movies_decade = netflix_df[filter_netflix_decade]

duration = (movies_decade.loc[:, 'duration'].mode())
duration = duration[0]
print(f'The mode movie duration in the 1990s was {duration} minutes')

# ! Consigna 2:

filter_action_movies = np.logical_and(
    movies_decade.loc[:,'genre'] == 'Action',
    movies_decade.loc[:,'duration'] < 90
)
short_movie_count = len(movies_decade[filter_action_movies])
print(f'There are {short_movie_count} action movies in the 1990s that are less than 90 minutes long')


# ! Consigna 3:

filter_netflix_2000 = np.logical_and(
    netflix_df.loc[:, 'type'] == 'Movie', 
    netflix_df.loc[:, 'release_year'] >= 2000
)

movies_2000 = netflix_df[filter_netflix_2000]


plt.hist(movies_2000.loc[:, 'duration'], bins = 40)
plt.title('Distribución de Duraciones de Películas (2000+)')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')


if not os.path.exists(os.path.join(script_dir, 'src', 'duration_2000.png')):
    plt.savefig(os.path.join(script_dir, 'src', 'duration_2000.png'))
else:
    print('The duration_2000.png file already exists')
    
plt.clf()
# ! Consigna 4:

genre_count = netflix_df.loc[:, 'genre'].value_counts().head(5)


plt.barh(genre_count.index, genre_count.values)
plt.title('Top 5 Géneros de Películas')
plt.xlabel('Cantidad')
plt.ylabel('Género')

if not os.path.exists(os.path.join(script_dir, 'src', 'top_5_genres.png')):
    plt.savefig(os.path.join(script_dir, 'src', 'top_5_genres.png'))
else:
    print('The top_5_genres.png file already exists')
    
plt.clf()


# ! Consigna 5

# Separar el año de la fecha agregada
netflix_df.loc[:, 'date_added'] = netflix_df.loc[:, 'date_added'].str.split(',').str[1].str.strip()

netflix_df.loc[:, 'date_added'] = pd.to_numeric(netflix_df.loc[:, 'date_added'])

# Contar el contenido agregado por año
netflix_date_type = netflix_df[['date_added', 'type']].value_counts()

netflix_pivote = netflix_date_type.unstack().fillna(0)

# Gráfica el contenido agregado por año
plt.figure(figsize = (12, 6))
plt.plot(netflix_pivote.index , netflix_pivote['Movie'] , label = 'Movie' , marker = 'o' , color = 'blue')
plt.plot(netflix_pivote.index , netflix_pivote['TV Show'] , label = 'TV Show' , marker = 'x' , color = 'green')
plt.title('Contenido agregado por año')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.legend()
plt.grid(True)

if not os.path.exists(os.path.join(script_dir, 'src', 'content_added.png')):
    plt.savefig(os.path.join(script_dir, 'src', 'content_added.png'))
else:
    print('The content_added.png file already exists')
    
plt.clf()

# ! Extra Mio 

genre_colors = {
    'Dramas': 'red',
    'Comedies': 'green',
    'Documentaries': 'blue',
    'Action': 'orange',
    'Children': 'purple',
    'Stand-Up': 'pink',
    'Horror Movies': 'gray',
    'International Movies': 'brown',
    'Classic Movies': 'cyan',
    'Uncategorized': 'magenta',
    'Thrillers': 'lime',
    'Independent Movies': 'yellow',
    'Anime Features': 'black',
    'Music': 'tab:blue',
    'Cult Movies': 'tab:olive',
    'Sci-Fi': 'tab:cyan',
    'Romantic Movies': 'tab:pink',
    'Sports Movies': 'lavender',
    'LGBTQ Movies': 'peachpuff',
}
netflix_movies = netflix_df[netflix_df.loc[:,'type'] == 'Movie']


movies_by_years = netflix_movies.groupby(['release_year', 'genre']).agg(
    count = ('title', 'count'),
    avg_duration = ('duration', 'mean'),
).reset_index()

pallet = movies_by_years.loc[:,'genre'].map(genre_colors)

bubble_size = movies_by_years['count'] * 10


legend_patches = [
    mpatches.Patch(color=color, label=label) 
    for label, color in genre_colors.items()
]

plt.figure(figsize = (12, 6))
plt.scatter(
    x = movies_by_years['release_year'],
    y = movies_by_years['avg_duration'],
    c = pallet,
    s = bubble_size,
    alpha = 0.8
)
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.title('Movie duration by release year')
plt.legend(handles = legend_patches,loc = 'center left', bbox_to_anchor = (1, 0.5) , fontsize = 'small', title = 'Genero')
plt.grid(True, linestyle='--', alpha=0.5)

if not os.path.exists(os.path.join(script_dir, 'src', 'movie_duration.png')):
    plt.savefig(os.path.join(script_dir, 'src', 'movie_duration.png'))
else:
    print('The movie_duration.png file already exists')
    
plt.clf()






