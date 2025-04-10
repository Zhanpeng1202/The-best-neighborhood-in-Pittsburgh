import pandas as pd

csv_path = "PittsburghCensus/cdbg_census.csv"

df = pd.read_csv(csv_path)
# sort the data by the column "objectid"
df = df.sort_values(by="objectid")
print(df.head())

# # save the sorted data to a new csv file
# df.to_csv("PittsburghCensus/cdbg_census_sorted.csv", index=False)





