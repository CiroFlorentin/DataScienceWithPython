import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path_aapl= os.path.join(script_dir, 'src/Financial', 'StockDataApple.csv')
csv_path_mcd= os.path.join(script_dir, 'src/Financial', 'StockDataMcd.csv')

aapl= pd.read_csv(csv_path_aapl)
mcd= pd.read_csv(csv_path_mcd)


#! .merge() vs .merge_ordered() vs .merge_asof()
#? .merge()
#* on, left_on, right_on
#* how (left, right, inner, outer)
#* default inner
#* suffixes
#* PARA LLAMAR: df1.merge(df2)


#? .merge_ordered()
#* on, left_on, right_on
#* how (left, right, inner, outer)
#* default outer
#* suffixes
#* PARA LLAMAR: pd.merge_ordered(df1, df2)
#* fill_method('ffill', 'bfill', 'pad', 'backfill')
#* default 'ffill'


#? .merge_asof()
#* on, left_on, right_on
#* how (left, right, inner, outer)
#* default outer
#* suffixes
#* PARA LLAMAR: pd.merge_asof(df1, df2)
#* fill_method('ffill', 'bfill', 'pad', 'backfill')
#* default 'ffill'
#* direction('backward', 'forward', 'nearest')
#* default 'backward'
# VALORES MAS CERCANOS

# ! Example
# df_ordered= pd.merge_ordered(aapl, mcd, on='date', suffixes=('_aapl', '_mcd'))
# print(df_ordered)

#! Example 2 with fill_method
# df_ordered= pd.merge_ordered(aapl, mcd, on='date', suffixes=('_aapl', '_mcd'), fill_method='ffill')
# print(df_ordered)
