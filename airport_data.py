#Load datafile
"""Contains one function, "airports_data.airports". It reads the airport info from "airport_info.csv" and returns a list of the IATA codes, cities, countries, latitudes and longitudes as separate sublists """
import numpy as np
import matplotlib.mlab as ml

def airports():
	filename = 'airport_info.csv'
	#tab=np.loadtxt(filename, delimiter=',', dtype=str)
	tab=ml.csv2rec(filename)

	#Extract IATA codes and other info for the airports from the datafile
	ap_codes=[]
	ap_cities=[]
	ap_countries=[]
	ap_latitudes=[]
	ap_longitudes=[]
	for i in range(0,len(tab),1):
		ap_codes.append(tab[i][0])
		ap_cities.append(tab[i][1])
		ap_countries.append(tab[i][3])
		ap_latitudes.append(tab[i][5])
		ap_longitudes.append(tab[i][6])

	airports=[]
	airports.append(ap_codes)
	airports.append(ap_cities)
	airports.append(ap_countries)
	airports.append(ap_latitudes)
	airports.append(ap_longitudes)
	
	return airports