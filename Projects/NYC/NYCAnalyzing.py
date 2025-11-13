import pandas as pd
import os 

# Read in the data

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "src", "schools.csv")

schools_df = pd.read_csv(csv_path)


# Preview the data
# print(schools_df.columns)

#! Which NYC schools have the best math results?

# math_filter= schools_df["average_math"] >= 800*0.8

# best_math_schools = schools_df[math_filter].sort_values("average_math", ascending=False)[["school_name","average_math"]]

# ? Mas eficiente
best_math_schools = (
    schools_df.loc[schools_df['average_math']>= 800* 0.8, ["school_name","average_math"]]
    .sort_values("average_math", ascending=False)
    )

# print(best_math_schools)


# ! What are the top 10 performing schools based on the combined SAT scores?

# schools_df['total_SAT'] = schools_df['average_math'] + schools_df['average_reading'] + schools_df['average_writing']


# top_10_schools = schools_df.sort_values("total_SAT", ascending=False)[["school_name","total_SAT"]].head(10)

# ? Mas eficiente
schools_df['total_SAT'] =( 
    schools_df['average_math'] + 
    schools_df['average_reading'] + 
    schools_df['average_writing']
    )

#* nlargest() ordena los valores de mayor a menor
top_10_schools = schools_df.nlargest(10, "total_SAT")[["school_name","total_SAT"] ]

# print(top_10_schools)


# ! Which single borough has the largest standard deviation in the combined SAT score?

# maxDeviation = schools_df.groupby("borough")["total_SAT"].std().idxmax()
# numSchools = schools_df[schools_df["borough"] == maxDeviation].count().iloc[0]
# average_SAT = schools_df[schools_df["borough"] == maxDeviation]["total_SAT"].mean().round(2)
# std_SAT = schools_df[schools_df["borough"] == maxDeviation]["total_SAT"].std().round(2)

# std_dev = {
#     "borough": maxDeviation,
#     "num_schools": numSchools,
#     "average_SAT": average_SAT,
#     "std_SAT": std_SAT
# }

# largest_std_dev = pd.DataFrame(std_dev, index=[0])

#? Mas eficiente
stats = (
    schools_df.groupby("borough")['total_SAT']
    .agg(['mean','std','count'])
    .round(2)
    .rename(columns={'mean':'average_SAT','std':'std_SAT','count':'num_schools'})
)

largest_std_dev = stats.loc[[stats['std_SAT'].idxmax()]].reset_index()

# print(largest_std_dev)