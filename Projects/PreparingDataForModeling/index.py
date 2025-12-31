import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "train.csv"))
# print(df.head())


sns.set_style("darkgrid")

ax = sns.countplot(data=df, x="job_change", hue="job_change", legend=False)
ax.set_title("Job Change")
plt.savefig(os.path.join(os.path.dirname(__file__), "images", "job_change.png"))
plt.close()


ax = sns.countplot(
    data=df,
    y="education_level",
    hue="education_level",
    legend=False,
    order=df["education_level"].value_counts().index,
)
ax.set_title("Education Level")
plt.savefig(os.path.join(os.path.dirname(__file__), "images", "education_level.png"))
plt.close()


ax = sns.catplot(x="job_change", y="training_hours", hue="gender", data=df, kind="box")
ax.fig.suptitle("Horas de entrenamiento vs Cambios de trabajo", size=16)
ax.set_ylabels("Horas de entrenamiento")
ax.set_xlabels("Cambios de trabajo")
ax.fig.tight_layout()
plt.savefig(
    os.path.join(os.path.dirname(__file__), "images", "training_hoursVSjob_change.png")
)
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x="city_development_index",
    hue="job_change",
    kde=True,
    stat="density",
    element="step",
    common_norm=False,
)
plt.title("Distribución de City Development Index por Job Change")
plt.xlabel("Índice de Desarrollo de la Ciudad")
plt.ylabel("Densidad")
plt.savefig(
    os.path.join(
        os.path.dirname(__file__), "images", "city_development_indexVSjob_change.png"
    )
)
plt.close()
