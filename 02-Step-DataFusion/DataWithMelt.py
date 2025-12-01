import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_socialFin= os.path.join(script_dir, 'src/Melt', 'SocialFin.csv')

socialFin= pd.read_csv(csv_path_socialFin)


social_fin_tall =  socialFin.melt(id_vars=['financial','company'],value_vars=['2018','2017'],var_name='year',value_name='value')
print(social_fin_tall)
