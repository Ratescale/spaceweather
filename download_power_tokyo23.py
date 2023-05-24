import osmnx as ox

# Bounding box coordinates for Tokyo's 23 wards (approximate)
north, south, east, west = 35.774143, 35.627472, 139.910177, 139.594515

# Download the data for the power lines and towers
print("Downloading data for Tokyo's 23 wards...")
power_lines = ox.geometries.geometries_from_bbox(north, south, east, west, tags={'power': 'line'})
power_towers = ox.geometries.geometries_from_bbox(north, south, east, west, tags={'power': 'tower'})

# Convert list type columns to string
for col in power_lines.columns:
    if isinstance(power_lines[col].iloc[0], list):
        power_lines[col] = power_lines[col].apply(lambda x: ', '.join(map(str, x)))

for col in power_towers.columns:
    if isinstance(power_towers[col].iloc[0], list):
        power_towers[col] = power_towers[col].apply(lambda x: ', '.join(map(str, x)))

# Save the data to GeoJSON files
power_lines.to_file("tokyo_power_lines.geojson", driver='GeoJSON')
power_towers.to_file("tokyo_power_towers.geojson", driver='GeoJSON')