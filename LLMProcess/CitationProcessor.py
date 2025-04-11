from CallAPI import summarize_citation
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from concurrent.futures import ThreadPoolExecutor, as_completed



citation_df = pd.read_csv("PittsburghCensus/monthlyCriminal.csv")

# print all the columns
print(citation_df.columns)

# summary_list = []
# neighborhood_list = []
# with ThreadPoolExecutor(max_workers=500) as executor:  
#     futures = {executor.submit(summarize_citation, row["OFFENSES"], row["NEIGHBORHOOD"]): idx for idx, row in citation_df.iterrows()}
    
#     for future in as_completed(futures):
#         try:
#             result = future.result()
#             summary_list.append(result[0])
#             neighborhood_list.append(result[1])
#         except Exception as e:
#             print(f"Error occurred: {e}")
#             # results.append("ERROR")
#             # stop the loop
#             break


# summary_df = pd.DataFrame(summary_list, columns=["SUMMARY"])
# neighborhood_df = pd.DataFrame(neighborhood_list, columns=["NEIGHBORHOOD"])

# # merge the two dataframes
# summary_neighborhood_df = pd.concat([ neighborhood_df, summary_df], axis=1)

# # save the dataframe to a csv file
# summary_neighborhood_df.to_csv("PittsburghCensus/summary_all.csv", index=False)


