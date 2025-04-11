from CallAPI import summarize_citation
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from concurrent.futures import ThreadPoolExecutor, as_completed


citation_df = pd.read_csv("PittsburghCensus/summary_all.csv")

summary_String = citation_df["SUMMARY"].to_string(index=False)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(summary_String)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()