# The-best-neighborhood-in-Pittsburgh

> **Check our final Jupyter notebook file at:** `notebook/main.ipynb`

# Team Name
**Differential Octopus**

# Team Members
**Richard Xu**   zhx112@pitt.edu<br>(The notebook `notebook/richard.ipynb` )

**Zhanpeng Luo** ZhanpengLuo@pitt.edu<br>(All the python scripts)
# Datasets: 

**Numerical Data**
1. [City of Pittsburgh Trees](https://data.wprdc.org/dataset/city-trees)
2. [Pittsburgh Police Arrest Data](https://data.wprdc.org/dataset/arrest-data)
3. [City of Pittsburgh Steps](https://data.wprdc.org/dataset/city-steps)
4. [Pittsburgh Public Schools Enrollment](https://data.wprdc.org/dataset/pittsburgh-public-schools-enrollment)
5. [City of Pittsburgh Parks](https://data.wprdc.org/dataset/parks)
6. [City of Pittsburgh Facilities](https://data.wprdc.org/dataset/city-of-pittsburgh-facilities)

**Text Data**
1. [Non-Traffic Citations](https://data.wprdc.org/dataset/non-traffic-citations)
2. [Monthly Criminal Activity Dashboard](https://data.wprdc.org/dataset/monthly-criminal-activity-dashboard)

**Geographical Data**<br>
[2010 Census
Block Groups](https://data.wprdc.org/dataset/2010-census-block-groups)

# Simple Introduction:
This repository includes a jupyter notebook `notebook/main.ipynb` that analyzes the best neighborhood in Pittsburgh based on some criteria, and the supporting files.

# Content
- Introduction
- Metrics
- The Best Neighborhood
- Conclusion

# Proposed Pipeline 

**Geographical Data**<br>
We use the geojsons provided in this dataset to visualize the result.

**Numerical Data**<br>
For the numerical data part,

**Text Data**<br>
For the text data part, we choose to leverage the large language model API to process, reason, understand and finally give us an evaluation for the best neighborhood in Pittsburgh.
Specifically, we call [Doubao API](https://team.doubao.com/en/), a llm provide by bytedance. We choose doubao since there are more than 100,000 items in the total dataset, we have to find a model is fast, allowing for high-concurency and cheap. We use doubao to reason and generate a coarse summarization for the Non-Traffic Citations and Monthly Criminal Activity Dashboard to condense the information and summarize them into predefined labels. After we get the summarized item for each crime, we could visualize them with a word cloud. <br>

Next, we use [Sonar API](https://www.perplexity.ai/hub/blog/introducing-the-sonar-pro-api) provided by Perplexity, we choose it as our judge to final evaluate because 
 - It is a larger model and is suitable for complex reasoning
 - Perplexity is famous for online searching, we hope this might reduce the hallucination and help better evaluate the result
 - Perplexity provide 5 free credit for students!
To further reduce the context windows, we use a rank sum to get a coarse ranking for the processed data and we only ask model to choose between the 5 neighbourhoods.
