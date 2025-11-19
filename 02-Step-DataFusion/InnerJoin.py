import os
import pandas as pd

from Projects.NYC.NYCAnalyzing import csv_path

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_wards = os.path.join(script_dir, "src/Chicago", "Chicago_wards.csv")
csv_path_population = os.path.join(script_dir, "src/Chicago", "Chicago_census.csv")
csv_path_licenses = os.path.join(script_dir, "src/Chicago", "business_licenses.csv")
csv_path_grants = os.path.join(script_dir, "src/Chicago", "Small_Business_Grant_Agreements.csv")

wards = pd.read_csv(csv_path_wards)
population = pd.read_csv(csv_path_population)
licenses = pd.read_csv(csv_path_licenses)
grants= grants = pd.read_csv(csv_path_grants)


# ! Inner Join
wards_census= wards.merge(population, on="ward" , suffixes=("_ward", "_cen"))

# print(wards_census.shape)

#! one to many 

ward_licenses = wards.merge(licenses, on="ward" , suffixes=('_ward', '_lic'))

# ward_licenses.sort_values

#! More tables
grant_licenses_wards= grants.merge(licenses, on=['zip','address'])\
                            .merge(wards, on='ward', suffixes=('_bus','_ward'))

# grant_licenses_wards.groupby('ward').agg('sum').plot(kind='bar', y='grant')
# plt.show()