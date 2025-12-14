import pandas as pd
import numpy as np
import os


tweets_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', "tweets.csv"))

result = list(filter(lambda x : x[0:2] == 'RT', tweets_df['text']))

# for tweet in result:
#     print(tweet)


def count_entries (df,col_name = 'lang'):
    
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    cols_count = {}
    try: 
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

result1 = count_entries(tweets_df, 'lang')
# result2 = count_entries(tweets_df, 'lang1')
print(result1)
# print(result2)
