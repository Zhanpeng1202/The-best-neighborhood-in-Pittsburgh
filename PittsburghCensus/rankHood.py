import pandas as pd

# Read the CSV file
hood_df = pd.read_csv("richard/summaryPitt_ALL_MERGED_UNIT.csv")

# Set NEIGHBORHOOD as index to ensure proper alignment
hood_df = hood_df.set_index("NEIGHBORHOOD")

# Create rank columns with descriptive names
hood_df["crime_rank"] = hood_df["total_crimes_UNIT"].rank(method="min", ascending=False)
hood_df["facility_rank"] = hood_df["facility_count_UNIT"].rank(method="min")
hood_df["steps_rank"] = hood_df["Total_Steps_UNIT"].rank(method="min" )
hood_df["park_rank"] = hood_df["non_park_count_UNIT"].rank(method="min")
hood_df["tree_rank"] = hood_df["tree_count_UNIT"].rank(method="min")
hood_df["student_rank"] = hood_df["TOTAL_STUDENTS_UNIT"].rank(method="min")

# Select only the rank columns for the output
rank_columns = ["crime_rank", "facility_rank", "steps_rank", "park_rank", "tree_rank", "student_rank"]
all_rank = hood_df[rank_columns].copy()




# Reset index to make NEIGHBORHOOD a regular column again
all_rank.reset_index(inplace=True) 

# add a new column "rank_sum"
all_rank["rank_sum"] = all_rank["crime_rank"] + all_rank["facility_rank"] + all_rank["steps_rank"] + all_rank["park_rank"] + all_rank["tree_rank"] + all_rank["student_rank"]

# sort the dataframe by rank_sum
all_rank = all_rank.sort_values(by="rank_sum", ascending=False)


# Save to CSV
all_rank.to_csv("PittsburghCensus/rank_sum.csv", index=False)


