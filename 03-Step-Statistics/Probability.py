import os
import pandas as pd
import numpy as np



script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'src', 'sales_counts.csv')

sales_counts = pd.read_csv(csv_path)

#? OBTENER UN VALOR ALEATORIO
# print(sales_counts.sample())

#! SEMILLA
# np.random.seed(10)


#* Sucesos dependientes
#? Muestreo sin reemplazo
# print(sales_counts.sample(2))

#* Sucesos independientes
#? Muestreo con reemplazo
# print(sales_counts.sample(2, replace=True))


