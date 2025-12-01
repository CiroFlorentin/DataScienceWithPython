import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_inv_jan = os.path.join(script_dir, 'src/Vertical/Table1.csv')
csv_path_inv_feb = os.path.join(script_dir, 'src/Vertical/Table2.csv')
csv_path_inv_mar = os.path.join(script_dir, 'src/Vertical/Table3.csv')


inv_jan = pd.read_csv(csv_path_inv_jan)
inv_feb = pd.read_csv(csv_path_inv_feb)
inv_mar = pd.read_csv(csv_path_inv_mar)


invoice = pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False ,keys=['jan','feb','mar'])
print(invoice)
