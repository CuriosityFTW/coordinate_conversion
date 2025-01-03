import math
from statistics import mean

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Difference in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat/2)**2 + (math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    n1 = 1.007874451319323
    n2 = 1.0038409765615648
    n3 = 1.0046376067278482
    
    avg = mean([n1, n2, n3])

    # Calculate distance in meters
    # distance = R * c * 1000
    distance = R * c * 1000 / avg
    return distance

# bangalore
lat1 = 12.9719 
lon1 = 77.5937

#chennai (288)
# lat2 = 13.0827
# lon2 = 80.2707

#mumbai (842)
# lat2 = 19.0760
# lon2 = 72.8777

#delhi (1742)
lat2 = 28.7041
lon2 = 77.1025

# lat1 = 13.0047358
# lon1 = 77.6812407
# lat2 = 13.0047357
# lon2 = 77.6812407

distance = haversine(lat1, lon1, lat2, lon2)
print(distance/1000)
print(distance)