'''Script to calculate greater circle distances using the haversine formula between two points
central_angle needs to be in radians.luckily math trig functions return
in radians'''

import math as ma

def flight_distance(lat_1, lon_1, lat_2, lon_2):
    #lat_1, lon_1 = start
    #lat_2, lon_2 = finish

    dlat = (lat_2 - lat_1) #absolute difference in latitude between two airports, converted to radians
    dlon = (lon_2 - lon_1) #absolute diff in longitude between two airports

    earth_radius = 6367 #Earth's radius in km
    
    b = ma.sin(ma.radians(dlat/2))*ma.sin(ma.radians(dlat/2))+ \
	ma.cos(ma.radians(lat_1))*ma.cos(ma.radians(lat_2))*ma.sin(ma.radians(dlon/2))*ma.sin(ma.radians(dlon/2))
    
    
    central_angle = 2*ma.asin(ma.sqrt(b))

    arc_length = earth_radius*central_angle
   
    return arc_length
