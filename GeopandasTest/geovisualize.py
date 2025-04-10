import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("GeopandasTest/hood.geojson")
print(gdf["hood"].unique())

# gdf.plot()
# ax = gdf.plot(figsize=(10, 10), color=gdf.index.map(lambda x: plt.cm.tab20(x % 20)))

# gdf.plot(
#     column='objectid',         # numeric column to base color on
#     cmap='Blues',              # color gradient: light to dark blue
#     legend=True,               # optional: add colorbar
#     edgecolor='black',         # optional: polygon borders
#     linewidth=0.5              # optional: border width
# )




# plt.show()
