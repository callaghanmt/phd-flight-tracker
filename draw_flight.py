from airport_coords import coordinates
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

def draw(x1,x2,x3,x4):

	map = Basemap(projection='robin', lat_0=0, lon_0=0, resolution='l', area_thresh=1000.0)
	map.drawcoastlines()
	map.drawcountries()
	map.fillcontinents(color='coral', lake_color='aqua')
	map.drawmapboundary(fill_color='aqua')

	map.drawmeridians(np.arange(0,360,30))
	map.drawparallels(np.arange(-90,90,30))

	#initiate ocean and icecap colours
	#map.bluemarble()

	#draw a blob on the map
	x,y = map(x2,x1)
	map.plot(x,y, 'bo', markersize=10)

	x,y = map(x4,x3)
	map.plot(x,y, 'bd', markersize=10)
	
	map.drawgreatcircle(x2,x1,x4,x3,linewidth=2,color='b')

	plt.show()