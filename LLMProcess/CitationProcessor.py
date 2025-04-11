from CallAPI import summarize_citation
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from concurrent.futures import ThreadPoolExecutor, as_completed



citation_df = pd.read_csv("PittsburghCensus/non-traffic-citation.csv")
# citation_df["SUMMARY"] = citation_df["OFFENSES"].apply(summarize_citation)

results = []
with ThreadPoolExecutor(max_workers=20) as executor:  
    futures = {executor.submit(summarize_citation, row["OFFENSES"]): idx for idx, row in citation_df.head(100).iterrows()}
    
    for future in as_completed(futures):
        try:
            result = future.result()
            results.append(result)
        except Exception as e:
            print(f"Error occurred: {e}")
            # results.append("ERROR")
            # stop the loop
            break


pd.DataFrame(results, columns=["SUMMARY"]).to_csv("PittsburghCensus/non-traffic-citation-summary.csv", index=False)


















# # turn the summary column into a string
# summary_string = " ".join(results)

# wordcloud = WordCloud(width=800, height=400, background_color="white").generate(summary_string)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()























# # test first 10 rows
# for index, row in citation_df.head(10).iterrows():
#     print(row["OFFENSES"])
#     print(summarize_citation(row["OFFENSES"]))
#     print("-"*100)
