
def parse_tle(tle_str):
    lines = tle_str.strip().split('\n')
    line1, line2 = lines[0], lines[1]

    satellite_number = line1[2:7]
    classification = line1[8]
    launch_year = int(line1[9:11])
    launch_number = int(line1[11:14])
    piece_of_launch = line1[14:17]
    epoch_year = int(line1[18:20])
    epoch = float(line1[20:32])
    mean_motion_derivative = float(line1[33:43])
    mean_motion_sec_derivative = float(line1[44:52]) if line1[44] != ' ' else 0.0
    bstar_drag_term = float(line1[53:61]) if line1[53] != ' ' else 0.0
    ephemeris_type = int(line1[62])
    element_number = int(line1[64:68])

    inclination = float(line2[8:16])  # degrees
    right_ascension = float(line2[17:25])  # degrees
    eccentricity = float('.' + line2[26:33])
    argument_of_perigee = float(line2[34:42])  # degrees
    mean_anomaly = float(line2[43:51])  # degrees
    mean_motion = float(line2[52:63])  # revolutions per day
    revolution_number_at_epoch = int(line2[63:68])

    return {
        'satellite_number': satellite_number,
        'classification': classification,
        'launch_year': launch_year,
        'launch_number': launch_number,
        'piece_of_launch': piece_of_launch,
        'epoch_year': epoch_year,
        'epoch': epoch,
        'mean_motion_derivative': mean_motion_derivative,
        'mean_motion_sec_derivative': mean_motion_sec_derivative,
        'bstar_drag_term': bstar_drag_term,
        'ephemeris_type': ephemeris_type,
        'element_number': element_number,
        'inclination': inclination,
        'right_ascension': right_ascension,
        'eccentricity': eccentricity,
        'argument_of_perigee': argument_of_perigee,
        'mean_anomaly': mean_anomaly,
        'mean_motion': mean_motion,
        'revolution_number_at_epoch': revolution_number_at_epoch,
    }

# Example TLE data
tle_data = """
1 25544U 98067A   20077.53436287  .00000756  00000-0  34119-4 0  9991
2 25544  51.6416 137.4192 0001756 226.5465 133.5367 15.49510801222415
"""
orbit_parameters = parse_tle(tle_data)
print(orbit_parameters)

# Load TLE data
#stations_url = 'http://celestrak.com/NORAD/elements/starlink.txt'
#satellites = load.tle_file(stations_url)

# Choose a specific Starlink satellite
#satellite = satellites[0]  # for example, the first satellite in the list

# Calculate position
#ts = load.timescale()
#t = ts.now()
#geocentric = satellite.at(t)

# Print satellite's position
#print(geocentric.position.km)
