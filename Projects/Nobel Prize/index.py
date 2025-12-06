import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap

nobel = pd.read_csv(os.path.join(os.path.dirname(__file__), 'src', 'nobel.csv'))


# print(nobel.columns)


#! Ejercicio 1:
# ? Existen dos formas de obtener el valor mas común en una columna
top_gender = nobel['sex'].value_counts().head(10)
top_country = nobel['birth_country'].value_counts().head(10).index
top_country_df = nobel[nobel['birth_country'].isin(top_country)]
# print(top_gender)
# print(top_country)

#* Graficos

plt.style.use('ggplot')
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.countplot(y='birth_country', data = top_country_df, palette='viridis',hue='birth_country', order = top_country, ax=axes[0])
axes[0].set_title('Top 10 Country of Birth')
axes[0].set_xlabel('Quantity')
axes[0].set_ylabel('')

sns.countplot(x='sex' , palette='viridis',hue='sex',data=nobel, ax=axes[1])
axes[1].set_title('Distribution by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Quantity')
plt.tight_layout()

if not os.path.isfile('Projects/Nobel Prize/src/nobel_gender_country.svg'):
    plt.savefig('Projects/Nobel Prize/src/nobel_gender_country.svg', dpi=300)
plt.close()

#! Ejercicio 2:

nobel['decade']= (nobel['year']//10)*10

nobel["usa_born_winner"] = nobel['birth_country'] == 'United States of America'

prop_usa_winners = nobel.groupby('decade',as_index=False)['usa_born_winner'].mean()
prop_usa_winners['usa_born_winner'] = prop_usa_winners['usa_born_winner'] * 100

max_decade_usa = int(prop_usa_winners.loc[prop_usa_winners['usa_born_winner'].idxmax(), 'decade'])

# print(max_decade_usa)

g = sns.relplot(
    x='decade', 
    y='usa_born_winner', 
    data=prop_usa_winners, 
    kind='line', 
    palette='viridis',
    marker='o',
    color='navy'
)
g.set(xlabel='Decade', ylabel='Proportion (%)')
g.fig.suptitle('Proportion of Winners Born in the United States')
max_row = prop_usa_winners.loc[prop_usa_winners['usa_born_winner'].idxmax()]
g.ax.annotate(f"Maximum: {max_row['decade']:.0f} ({max_row['usa_born_winner']:.2f}%)", 
              xy=(max_row['decade'], max_row['usa_born_winner']),
              xytext=(max_row['decade'] -80, max_row['usa_born_winner']-1 ),
              arrowprops=dict(
                  arrowstyle="->", 
                  connectionstyle="arc3", 
                  color='black',
                  lw=1
                  )
              )
plt.tight_layout()


if not os.path.isfile('Projects/Nobel Prize/src/nobel_usa_winners.svg'):
    plt.savefig('Projects/Nobel Prize/src/nobel_usa_winners.svg', dpi=300)
plt.close()

#! Ejercicio 3:


nobel['female_winner'] = nobel['sex'] == 'Female'

prop_female_winners = nobel.groupby(['decade','category'],as_index=False)['female_winner'].mean()

prop_female_winners['female_winner'] = prop_female_winners['female_winner'] * 100

max_female_rox = prop_female_winners.loc[prop_female_winners['female_winner'].idxmax()]

max_female_dict = {
    int(max_female_rox['decade']):max_female_rox['category']
}

# print(prop_female_winners)


g = sns.relplot(
    kind = 'line',
    data = prop_female_winners,
    x = 'decade',
    y = 'female_winner',
    hue = 'category',
    marker = 'o',
)

g.legend.remove()
plt.legend(loc='upper left')
g.fig.suptitle('Proportion of Female Winners by Category and Decade', y=1)
g.set(xlabel='Decade', ylabel='Proportion (%)')
plt.tight_layout()

if not os.path.isfile('Projects/Nobel Prize/src/nobel_female_winners.svg'):
    plt.savefig('Projects/Nobel Prize/src/nobel_female_winners.svg', dpi=300)
plt.close()

#! Ejercicio 4:

female_winners = nobel[nobel['sex'] == 'Female'].sort_values('year')

first_woman= female_winners.iloc[0]


# print(first_woman['full_name'], first_woman['category'])


sns.set_style('white')

sns.relplot(
    kind = 'scatter',
    data = female_winners,
    x='year',
    y='category',
    s = 75,
    hue='category',
    legend= False,
    zorder = 2,
    height = 7,
    aspect = 1.5
)

plt.scatter(
    x=first_woman['year'],
    y=first_woman['category'],
    color='gold',
    s=500,
    zorder=3,
    marker='*',
    edgecolor='black',
    linewidth=1
)

plt.annotate(
    f'The first woman winner was {first_woman["full_name"]} in {first_woman["year"]} for {first_woman["category"]}',
    xy=(first_woman['year'], first_woman['category']),
    xytext=(first_woman['year']+ 5, first_woman['category']),
    arrowprops=dict(
        arrowstyle="->", 
        connectionstyle="arc3", 
        color='black',
    ),
    bbox=dict(
        boxstyle="square,pad=0.5", 
        fc="white", 
        ec="black",
        lw=1.5
    ),
    fontsize=10, 
    fontweight='bold',
    ha='left',
    va='center'
)

plt.title('Women Nobel Prize winners timeline')
plt.xlabel('Year')
plt.ylabel('Category')
plt.grid(axis='y', linestyle='--', alpha=0.3)
sns.despine(left=True)
plt.tight_layout()

if not os.path.isfile('Projects/Nobel Prize/src/timeline_women.svg'):
    plt.savefig('Projects/Nobel Prize/src/timeline_women.svg', dpi=300)
plt.close()
#! Ejercicio 5:

count_name = nobel['full_name'].value_counts()
repeat_list = count_name[count_name > 1].reset_index()
repeat_list.columns = ['full_name', 'count']

repeat_list['full_name_wrapped'] = repeat_list['full_name'].apply(
    lambda x: textwrap.fill(x, width=30)
)


g = sns.catplot(
    data=repeat_list,
    x='count',
    y='full_name_wrapped',
    kind='bar',
    hue = 'full_name_wrapped',
    aspect=1.5,
    height=5
    )
g.fig.suptitle('Nobel Prize winners with more than one win')
g.set(xlabel='Count', ylabel='')
g.set(xticks=range(0,5))
g.fig.subplots_adjust(left=0.3)
plt.tight_layout()

if not os.path.isfile('Projects/Nobel Prize/src/nobel_repeat_winners.svg'):
    plt.savefig('Projects/Nobel Prize/src/nobel_repeat_winners.svg', dpi=300)
plt.close()