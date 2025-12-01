import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path_sequels = os.path.join(script_dir, 'src/Movies/sequels.csv')

sequels = pd.read_csv(csv_path_sequels, index_col=0)

#* Join with itself (inner join)
# original_sequels = sequels.merge(sequels, left_on = 'sequel', right_on = 'id', suffixes= ('_org','_seq'))

#* Join with itself (left join)
# original_sequels_left = sequels.merge(sequels, left_on = 'sequel', right_on = 'id', suffixes= ('_org','_seq'), how='left')


#* Join with itself (right join)
# original_sequels_right = sequels.merge(sequels, left_on = 'sequel', right_on = 'id', suffixes= ('_org','_seq'), how='right')

#* Join with itself (outer join)
# original_sequels_outer = sequels.merge(sequels, left_on = 'sequel', right_on = 'id', suffixes= ('_org','_seq'), how='outer')

# print(original_sequels[['title_org','title_seq']].head())