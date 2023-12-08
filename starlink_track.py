from skyfield.api import load
from skyfield.sgp4lib import EarthSatellite
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# # Load TLE data
# stations_url = 'http://celestrak.com/NORAD/elements/starlink.txt'
# satellites = load.tle_file(stations_url)

# # Choose a specific Starlink satellite
# satellite = satellites[0]  # for example, the first satellite in the list

# # Calculate position
# ts = load.timescale()
# t = ts.now()
# geocentric = satellite.at(t)

# # Print satellite's position
# print(geocentric.position.km)

def read_tle_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    satellites = {}
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()
        satellites[name] = (line1, line2)

    return satellites

def get_satellite_position(tle_line1, tle_line2):
    ts = load.timescale()
    t = ts.now()
    satellite = EarthSatellite(tle_line1, tle_line2)
    geocentric = satellite.at(t)
    subpoint = geocentric.subpoint()
    return subpoint.latitude.degrees, subpoint.longitude.degrees

# Path to your TLE file
file_path = 'starlink2.txt'

# Read TLEs from the file
satellites = read_tle_file(file_path)

# Create a map using Cartopy
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Draw coastlines, country boundaries, fill continents.
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)

# Plot satellite positions
for name, tle in satellites.items():
    lat, lon = get_satellite_position(*tle)
    ax.plot(lon, lat, 'bo', markersize=5, transform=ccrs.Geodetic())
    ax.text(lon, lat, name, fontsize=6, transform=ccrs.Geodetic())

# Title
plt.title("Starlink Satellite Positions")

plt.show()
 

