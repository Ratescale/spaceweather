import osmnx as ox
import pandas as pd
import geopandas as gpd

# Japan's bounding box coordinates (approximate)
north, south, east, west = 45.551483, 24.396308, 153.986672, 122.934570

# Define the number of chunks
num_chunks = 15

# Calculate the latitude range for each chunk
lat_ranges = pd.cut([north, south], bins=num_chunks).categories

# Initialize empty GeoDataFrames for the power lines and towers
power_lines = gpd.GeoDataFrame()
power_towers = gpd.GeoDataFrame()

# Download and append the data for each chunk
for i in range(num_chunks):
    print(f"Downloading data for chunk {i+1}/{num_chunks}...")
    chunk_north, chunk_south = lat_ranges[i].right, lat_ranges[i].left
    chunk_power_lines = ox.geometries.geometries_from_bbox(chunk_north, chunk_south, east, west, tags={'power': 'line'})
    print(type(chunk_power_lines)) 
    chunk_power_towers = ox.geometries.geometries_from_bbox(chunk_north, chunk_south, east, west, tags={'power': 'tower'})
    print(type(chunk_power_towers)) 
    power_lines = power_lines.append(chunk_power_lines)
    power_towers = power_towers.append(chunk_power_towers)

# Save the data to GeoJSON files
power_lines.to_file("power_lines.geojson", driver='GeoJSON')
power_towers.to_file("power_towers.geojson", driver='GeoJSON')