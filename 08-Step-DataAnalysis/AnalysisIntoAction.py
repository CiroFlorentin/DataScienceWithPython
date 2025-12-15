import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
import re


planes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'planes.csv'),parse_dates=['Dep_Time','Arrival_Time'])

planes['Date_of_Journey'] = pd.to_datetime(planes['Date_of_Journey'], format='%d/%m/%Y')

#* Al realizar el EDA hay consignas que se deben cumplir independientemente de lo que hagamos posteriormente
#* 1. Debe ser representativo para la población que deseamos estudiar
#* PARA LOS DATOS CATEGÓRICOS
#* clases = labels

#! Observar frecuencia de los datos
# print(planes['Destination'].value_counts(normalize=True))

#! Cross tabulation
# pd.crosstab('select Column for Index','Select Column')

# print(pd.crosstab(planes['Source'], planes['Destination'],values=planes['Price'],aggfunc='median'))


#? Limpiar la duración



def convertir_a_minutos_totales(duracion):
    if pd.isna(duracion):
        return np.nan
    duracion_str = str(duracion).strip()
    horas_match = re.search(r'(\d+)\s*h', duracion_str)
    minutos_match = re.search(r'(\d+)\s*m', duracion_str)
    horas = int(horas_match.group(1)) if horas_match else 0
    minutos = int(minutos_match.group(1)) if minutos_match else 0
    return (horas * 60) + minutos

planes['Duration'] = planes['Duration'].apply(convertir_a_minutos_totales)


planes_to_dict = planes.groupby('Source')['Duration'].median().to_dict()
planes['Duration'] = planes['Duration'].fillna(planes['Source'].map(planes_to_dict))
planes = planes.dropna(subset=['Duration'])
planes['Duration'] = planes['Duration'].astype(float)

sns.heatmap(planes.corr(numeric_only=True),annot=True)
# plt.show()
plt.close()

# print(planes['Total_Stops'].value_counts())
planes['Total_Stops'] = planes['Total_Stops'].fillna('0')
planes['Total_Stops'] = planes['Total_Stops'].str.replace(' stops','')
planes['Total_Stops'] = planes['Total_Stops'].str.replace(' stop','')
planes['Total_Stops'] = planes['Total_Stops'].str.replace('non-stop','0')
planes['Total_Stops'] = planes['Total_Stops'].astype(int)


sns.heatmap(planes.corr(numeric_only=True),annot=True)
# plt.show()
plt.close()

# print(planes.dtypes)

planes['month'] = planes['Date_of_Journey'].dt.month
planes['weekday'] = planes['Date_of_Journey'].dt.weekday

# print(planes[['month','weekday','Date_of_Journey']].head())


planes['Dep_Hour'] = planes['Dep_Time'].dt.hour
planes['arrival_hour'] = planes['Arrival_Time'].dt.hour


sns.heatmap(planes.corr(numeric_only=True),annot=True)
# plt.show()
plt.close()

# print(planes['Price'].describe())

twenty_fifth = planes['Price'].quantile(0.25)
median = planes['Price'].median()
seventy_fifth = planes['Price'].quantile(0.75)
maximum = planes['Price'].max()

labels =['Economy','Premium Economy','Business Class','First Class']


bins = [0,twenty_fifth,median,seventy_fifth,maximum]

planes['Price_category'] = pd.cut(planes['Price'],bins=bins,labels=labels)

# print(planes[['Price','Price_category']].head())

sns.countplot(data=planes,x='Airline',hue='Price_category')
plt.tight_layout() 
# plt.show()
plt.close()


#! Generar hipótesis


sns.scatterplot(data=planes,x='Duration',y='Price',hue='Total_Stops')
plt.tight_layout() 
# plt.show()
plt.close()

sns.barplot(data=planes,x='Airline',y='Duration',hue='Airline')
plt.tight_layout() 
# plt.show()
plt.close()

sns.barplot(data=planes,x='Destination',y='Price',hue='Destination')
plt.tight_layout() 
plt.show()
plt.close()