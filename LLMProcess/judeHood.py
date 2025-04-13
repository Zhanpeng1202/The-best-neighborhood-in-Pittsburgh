from CallAPI import judge_hood_crime
import pandas as pd


citation_df = pd.read_csv("PittsburghCensus/summary_all.csv")
ctr_north = citation_df[citation_df["NEIGHBORHOOD"] == "Central North Side"]
pohill    = citation_df[citation_df["NEIGHBORHOOD"] == "Polish Hill"]
rsqure    = citation_df[citation_df["NEIGHBORHOOD"] == "Regent Square"]
gfiled    = citation_df[citation_df["NEIGHBORHOOD"] == "Greenfield"]
pbreeze   = citation_df[citation_df["NEIGHBORHOOD"] == "Point Breeze"]


records_ctr_north = ctr_north["SUMMARY"].to_string()
records_pohill    = pohill["SUMMARY"].to_string()
records_rsqure    = rsqure["SUMMARY"].to_string()
records_gfiled    = gfiled["SUMMARY"].to_string()
records_pbreeze   = pbreeze["SUMMARY"].to_string()

# print(records_ctr_north)
# print(records_pohill)
# print(records_rsqure)
# print(records_gfiled)
# print(records_pbreeze)


# print(crime_records)

# crime_keywords, hood_name = judge_hood_crime(hood_name="Central North Side", crime_records=crime_records)
# print(crime_keywords)
# print(hood_name)



keywords_list = []
neighborhood_list = []

keywords_list.append(judge_hood_crime(hood_name="Central North Side", crime_records=records_ctr_north))
neighborhood_list.append("Central North Side")

keywords_list.append(judge_hood_crime(hood_name="Polish Hill", crime_records=records_pohill))
neighborhood_list.append("Polish Hill")

keywords_list.append(judge_hood_crime(hood_name="Regent Square", crime_records=records_rsqure))
neighborhood_list.append("Regent Square")

keywords_list.append(judge_hood_crime(hood_name="Greenfield", crime_records=records_gfiled))
neighborhood_list.append("Greenfield")

keywords_list.append(judge_hood_crime(hood_name="Point Breeze", crime_records=records_pbreeze))
neighborhood_list.append("Point Breeze")


for i in range(len(keywords_list)):
    print(neighborhood_list[i])
    print(keywords_list[i])
    print("--------------------------------")


