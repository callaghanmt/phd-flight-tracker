import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

from airport_data import airports

def coordinates():
    aeropuertos = airports()

    ind_from = []
    ind_to = []
    ap_from = raw_input("Where are you flying from? ")
    ap_to = raw_input("Where are you flying to? ")
    #Check indexes of the airports based on the IATA code
    for i, elem in enumerate(aeropuertos[0]):
        if ap_from in elem:
            ind_from.append(i)
    if len(ind_from) == 0:
        print 'Airport with the code '+ap_from+' not found in the list, sorry.'

    for j, eleme in enumerate(aeropuertos[0]):
        if ap_to in eleme:
            ind_to.append(j)
    if len(ind_to) == 0:
        print 'Airport with the code '+ap_to+' not found in the list, sorry.'

    print 'Coordinates for',aeropuertos[1][ind_from[0]],'[',ap_from,'] are (Lat / Lon):',aeropuertos[3][ind_from[0]],'/',aeropuertos[4][ind_from[0]]
    print 'Coordinates for',aeropuertos[1][ind_to[0]],'[',ap_to,'] are (Lat / Lon):',aeropuertos[3][ind_to[0]],'/',aeropuertos[4][ind_to[0]]
    
    lat_or = aeropuertos[3][ind_from[0]]
    long_or = aeropuertos[4][ind_from[0]]
    lat_dest = aeropuertos[3][ind_to[0]]
    long_dest = aeropuertos[4][ind_to[0]]
    origin = aeropuertos[1][ind_from[0]]
    destination = aeropuertos[1][ind_to[0]]
    
    return lat_or, long_or, lat_dest, long_dest, origin, destination 
