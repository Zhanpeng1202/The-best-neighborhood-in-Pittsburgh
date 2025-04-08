import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("hood.geojson")
print(gdf.head())

gdf.plot()
plt.show()
