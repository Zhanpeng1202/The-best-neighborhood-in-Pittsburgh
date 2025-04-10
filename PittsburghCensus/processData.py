import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
gdf = gpd.read_file("GeopandasTest/hood.geojson")


citations_path = "PittsburghCensus/non-traffic-citation.csv"
citations_df = pd.read_csv(citations_path)

neighborhood_counts = citations_df["NEIGHBORHOOD"].value_counts().to_dict()
print(neighborhood_counts)

# make a new column in the gdf called "citation_count" and set it to the neighborhood_counts dictionary
gdf["citation_count"] = gdf["hood"].map(neighborhood_counts)

# plot the gdf
gdf.plot(column="citation_count",
         cmap="Blues",
         norm=LogNorm(vmin=gdf['citation_count'].min(), vmax=gdf['citation_count'].max()),
         legend=True)
plt.show()






