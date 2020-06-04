# install basemap
conda install basemap

# import
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
________________________________________________________________________________


# general workflow
1. Create a new basemap instance with the specific map projection we want to use and how much of the map we want included:
basemap_instance = Basemap(projection = 'merc', llcrnrlat = -80, urcrnrlat = 80, llcrnrlon = -180, urcrnrlon = 180)
# projection: the map projection.
# llcrnrlat: latitude of lower left hand corner of the desired map domain
# urcrnrlat: latitude of upper right hand corner of the desired map domain
# llcrnrlon: longitude of lower left hand corner of the desired map domain
# urcrnrlon: longitude of upper right hand corner of the desired map domain
________________________________________________________________________________


2. Convert spherical coordinates to Cartesian coordinates using the basemap instance:
x, y = basemap_instance(longitudes, latitudes) # method, long and lat have to be LISTS of values, pass in long before lat always
________________________________________________________________________________


3. Use the matplotlib and basemap methods to customize the map:
# create a scatter plot with the values
basemap_instance.scatter(x, y) # method,

# change the size of the points
basemap_instance.scatter(x, y, s = int) # s is optional

# draw coastlines on the scatter map projection
basemap_instance.drawcoastlines() # method

# draw countries on a scatter map projection
basemap_instance.drawcountries() # method

# draw great circles on the projection, the shortest circle connecting 2 points on a sphere
basemap_instance.drawgreatcircles(lon1, lat1, lon2, lat2) # method
# lon1 - longitude of the starting point.
# lat1 - latitude of the starting point.
# lon2 - longitude of the ending point.
# lat2 - latitude of the ending point.
## note: Cannot handle situations in which the great circle intersects the edge of the map projection domain, and then re-enters the domain.
## i.e the difference between lat1 and lat2 have to be less than 180, same for lon1 and lon2
________________________________________________________________________________


4. Display the map:
# display the plot map
plt.show() # method
