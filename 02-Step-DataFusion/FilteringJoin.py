import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_genres = os.path.join(script_dir, 'src', 'Music', 'generos_120.csv')
csv_path_tracks = os.path.join(script_dir, 'src', 'Music', 'tracks_150.csv')

genres = pd.read_csv(csv_path_genres)
top_tracks = pd.read_csv(csv_path_tracks)


# ! Semi Join
# genres_tracks = genres.merge(top_tracks, on='gid')
# # print(genres['gid'].isin(genres_tacks['gid'])) #Nos muestra true si en genres_tacks contiene el gid de genres

# top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
# print(top_genres.head())

#! Anti Join
genres_tracks = genres.merge(top_tracks, on='gid',how='left',indicator=True)
gid_list= genres_tracks.loc[genres_tracks['_merge']=='left_only','gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]

print(non_top_genres.head())