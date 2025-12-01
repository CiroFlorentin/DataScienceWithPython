import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_stock= os.path.join(script_dir, 'src/Query', 'Stock.csv')
csv_path_stockLong= os.path.join(script_dir, 'src/Query', 'StockLong.csv')

stock= pd.read_csv(csv_path_stock)
stockLong= pd.read_csv(csv_path_stockLong)

#! With query
# print(stock.query('nike >= 95'))
#? With AND , OR 
# print( stock.query('nike >= 95 and disney < 152'))
# print(stock.query('nike >= 95 or disney < 145'))

print(stockLong.query('stock == "disney" or (stock =="nike" and close <90)'))