import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


#! Diagrama de dispersion

height = [62,64,69,75,66,68,65,71,76,73]

weight = [120,136,158,175,137,165,154,172,200,187]

sns.scatterplot(x=height,y=weight)
# plt.show()
plt.close()

#! Grafico de conteo
gender = ['Female','Female','Female','Female','Male','Male','Male','Male','Male','Male']

sns.countplot(x=gender)
# plt.show()
plt.close()

sns.countplot(y = gender).set_title('Gender Count')
# plt.show()
plt.close()

#! Pandas with Seaborn

masculinity = pd.read_csv(os.path.join(os.path.dirname(__file__),'src','masculinity.csv'))

sns.countplot(
    x='how_masculine',
    data=masculinity, 
    hue='how_masculine', 
    legend= False, 
    # palette='Paired',
    order = ['Somewhat', 'Very', 'Not at all','Not very','No answer']
    )
# plt.show()
plt.close()

#! Conjunto de datos propios

tips = sns.load_dataset('tips')
# print(tips.head())
tono = {
    'No':'red',
    'Yes':'green'
}

sns.scatterplot(
    x='total_bill',
    y='tip',
    data=tips,
    hue='smoker',
    palette=tono,
    size='total_bill'
    )

# plt.show()
plt.close()

sns.countplot(
    x='smoker',
    data=tips,
    hue='sex'
    )
# plt.show()
plt.close()

sns.jointplot(x='total_bill',y='tip',data=tips)
# plt.show()
plt.close()

sns.swarmplot(x='day',y='total_bill',hue='smoker',data=tips)
# plt.show()
plt.close()
