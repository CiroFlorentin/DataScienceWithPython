import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path_tracks = os.path.join(script_dir, 'src/Integrity', 'Tracks.csv')
csv_path_specs = os.path.join(script_dir, 'src/Integrity', 'Specs.csv')
csv_path_inv_feb = os.path.join(script_dir, 'src/Vertical/Table2.csv')
csv_path_inv_mar = os.path.join(script_dir, 'src/Vertical/Table3.csv')

tracks = pd.read_csv(csv_path_tracks)
specs = pd.read_csv(csv_path_specs)
inv_feb = pd.read_csv(csv_path_inv_feb)
inv_mar = pd.read_csv(csv_path_inv_mar)

#* Validating merges
#  .merge(validate = 'one_to_one')
#  .merge(validate = 'one_to_many')
#  .merge(validate = 'many_to_one')
#  .merge(validate = 'many_to_many')

tracks_specs = tracks.merge(specs, on='tid', validate='one_to_many')
# print(tracks_specs)


# print(pd.concat([inv_feb, inv_mar], verify_integrity=True)) #* Corroborar que no hay duplicados

# print(pd.concat([inv_feb, inv_mar], verify_integrity=False))
#? Esto sirve para poder eliminar en caso de duplicidad 