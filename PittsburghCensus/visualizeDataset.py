import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

gdf = gpd.read_file("GeopandasTest/hood.geojson")
csv_path = "richard/summaryPitt_ALL_MERGED_UNIT.csv"

df_data = pd.read_csv(csv_path)
# get all columns from df_data
all_columns = df_data.columns.tolist()[1:]
print(all_columns)


# make the neighborhood colum in gdf to be all capitalized
gdf["hood"] = gdf["hood"].str.upper()


df_merge = pd.merge(gdf, df_data, left_on="hood", right_on="NEIGHBORHOOD", how="left")


# # plot the gdf
# df_merge.plot(column="Total_Crime_Count",
#          cmap="Blues",
#         #  norm=LogNorm(vmin=gdf['citation_count'].min(), vmax=gdf['citation_count'].max()),
#          legend=True)
# # plt.show()

# # save the plot
# plt.savefig("visualization/total_crime_count.png")


for column in all_columns:
    # do not show the coordinates an do not show the legend
    df_merge.plot(column=column,
             cmap="Blues")
    plt.axis('off')
    # save the plot
    fileBaseName = column.replace(" ", "_")
    fileBaseName = column.replace("/", "_")
    print(fileBaseName)
    plt.savefig(f"visualization/{fileBaseName}.png")