import pandas as pd
import numpy as np



df = pd.read_csv("richard/pittsburghArrest.csv")

df = df[["AGE", "INCIDENTNEIGHBORHOOD"]]
df = df.dropna(subset=["AGE", "INCIDENTNEIGHBORHOOD"])
df["AGE"] = pd.to_numeric(df["AGE"], errors="coerce")
df = df.dropna(subset=["AGE"])

df["AGE_GROUP"] = df["AGE"].apply(lambda x: "<18" if x < 18 else "18+")

grouped = df.groupby(["INCIDENTNEIGHBORHOOD", "AGE_GROUP"]).size().unstack(fill_value=0)

grouped["Total_Count"] = grouped["<18"] + grouped["18+"]
grouped["Under_18_Percent_Local"] = grouped["<18"] / grouped["Total_Count"]
grouped["Over_18_Percent_Local"] = grouped["18+"] / grouped["Total_Count"]

total_under_18 = grouped["<18"].sum()
total_over_18 = grouped["18+"].sum()

grouped["Under_18_Percent_Global"] = grouped["<18"] / total_under_18
grouped["Over_18_Percent_Global"] = grouped["18+"] / total_over_18

result = grouped.reset_index().rename(columns={
    "INCIDENTNEIGHBORHOOD": "NEIGHBORHOOD",
    "<18": "Under_18_Count",
    "18+": "Over_18_Count"
})

result = result[
    ["NEIGHBORHOOD", "Under_18_Count", "Over_18_Count", "Total_Count",
     "Under_18_Percent_Local", "Over_18_Percent_Local",
     "Under_18_Percent_Global", "Over_18_Percent_Global"]
]

result.to_csv("summaryPittArrest.csv", index=False)
