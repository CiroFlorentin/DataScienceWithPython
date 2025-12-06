import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

tips = sns.load_dataset('tips')

#? Relplot

sns.relplot(
    x='total_bill',
    y='tip',
    data=tips,
    kind='scatter',
    # col='smoker',
    # row='time',
    col='day',
    col_wrap=2,
    hue='sex'
)

# plt.show()
plt.close()

#? Personalizar
sns.relplot(
    x='total_bill',
    y='tip',
    data=tips,
    kind='scatter',
    size = 'size',
    sizes=(20, 200),
    hue='size',
    alpha=0.7
)
# plt.show()
plt.close()

sns.relplot(
    x='total_bill',
    y='tip',
    data=tips,
    kind='scatter',
    hue='smoker',
    style='smoker'
)
# plt.show()
plt.close()

#? Graficos lineales
air_df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'air_df_mean.csv'))

# ! MAL USO - ya que no es una variable cuantitativa, sino una categórica
# sns.relplot(x='hour', y='NO_2_mean', data=air_df, kind='scatter')
# plt.show()
# plt.close()

# ! BIEN USO
sns.relplot(x='hour', y='NO_2_mean', data=air_df, kind='line', hue='location',style='location',markers=True)
# plt.show()
plt.close()

#? Intervalos de confianza

sns.relplot(x='hour', y='NO_2_mean',data=air_df, kind='line',ci='sd')
# plt.show()
plt.close()

#? Sin intervalos de confianza
sns.relplot(x='hour', y='NO_2_mean',data=air_df, kind='line',ci=None)
# plt.show()
plt.close()

