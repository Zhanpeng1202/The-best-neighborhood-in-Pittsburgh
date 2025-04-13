from CallAPI import judge_hood_all
import pandas as pd



rank_df = pd.read_csv("PittsburghCensus/rank_sum.csv")
citation_df = pd.read_csv("PittsburghCensus/summary_all.csv")
print(rank_df.head(5))

# we only process the top 5 neighborhoods
#         NEIGHBORHOOD  crime_rank  facility_rank  steps_rank  park_rank  tree_rank  student_rank  rank_sum
# 0  CENTRAL NORTHSIDE        61.0           18.0        42.0       54.0       62.0          48.0     285.0
# 1        POLISH HILL        42.0           56.0        60.0       55.0       40.0          12.0     265.0
# 2      REGENT SQUARE        59.0           59.0        10.0       58.0       58.0          17.0     261.0
# 3         GREENFIELD        39.0           27.0        53.0       46.0       39.0          50.0     254.0
# 4       POINT BREEZE        55.0           39.0        11.0       59.0       47.0          26.0     237.0


score_list = []


for i in range(5):
    hood_name = rank_df.iloc[i]["NEIGHBORHOOD"]
    crime_score = rank_df.iloc[i]["crime_rank"]
    facility_score = rank_df.iloc[i]["facility_rank"]
    steps_score = rank_df.iloc[i]["steps_rank"]
    park_score = rank_df.iloc[i]["park_rank"]
    tree_score = rank_df.iloc[i]["tree_rank"]
    student_score = rank_df.iloc[i]["student_rank"]
    score_sum = rank_df.iloc[i]["rank_sum"]

    score_record = f"""
    All the scores are higher the better.
    In neighborhood {hood_name},
    the crime score is {crime_score},
    the facility score is {facility_score},
    the steps score is {steps_score},
    the park score is {park_score},
    the tree score is {tree_score},
    the student score is {student_score},
    the total score sum up to {score_sum}
    """
    score_list.append(score_record)

ctr_north = citation_df[citation_df["NEIGHBORHOOD"] == "Central North Side"]["SUMMARY"].to_string()
pohill    = citation_df[citation_df["NEIGHBORHOOD"] == "Polish Hill"]["SUMMARY"].to_string()
rsqure    = citation_df[citation_df["NEIGHBORHOOD"] == "Regent Square"]["SUMMARY"].to_string()
gfiled    = citation_df[citation_df["NEIGHBORHOOD"] == "Greenfield"]["SUMMARY"].to_string()
pbreeze   = citation_df[citation_df["NEIGHBORHOOD"] == "Point Breeze"]["SUMMARY"].to_string()

records = [ctr_north, pohill, rsqure, gfiled, pbreeze]

final_result = []

for i in range(5):
    final_result.append(score_list[i] + "The detailed crime records are: " + records[i])
    print(final_result[i])

result = judge_hood_all(final_result)
print(result)








