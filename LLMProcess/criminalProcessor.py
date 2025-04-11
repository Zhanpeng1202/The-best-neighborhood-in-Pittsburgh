from CallAPI import summarize_citation
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from concurrent.futures import ThreadPoolExecutor, as_completed



criminal_df = pd.read_csv("PittsburghCensus/monthlyCriminal.csv")

sumary = criminal_df["NIBRS_Offense_Type"].to_string(index=False)

# wordcloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(sumary)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()