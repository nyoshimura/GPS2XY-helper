import math
import pyproj

lat, long = 35.632246, 139.880899 # Tokyo Disney Land
print("------------------------------------------------")
print("lat={}, lon={}".format(lat, long))

######################################
# Spherical Pseudo-Mercator projection
# base code is from wiki: https://wiki.openstreetmap.org/wiki/Mercator#Python
# values are scaled up based on (approx.) earth radius: https://en.wikipedia.org/wiki/Earth_radius
# then final code becomes like below
# ref: https://towardsdatascience.com/exploring-and-visualizing-chicago-transit-data-using-pandas-and-bokeh-part-ii-intro-to-bokeh-5dca6c5ced10
######################################
def merc(lat,lon):
    r_major = 6378137.000 # earth radius
    x = r_major * math.radians(lon)
    scale = x/lon
    y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
    return (x, y)

#########################################
# EPSG-based projection
# pyproj is required
# ref: https://gis.stackexchange.com/questions/247871/convert-gps-coordinates-to-web-mercator-epsg3857-using-python-pyproj
# more precise projection based on EPSG code
# ref in Japanese: http://sanvarie.hatenablog.com/entry/2016/01/04/170242
#########################################
def merc_pyproj(lat,lon):
    EPSG4612 = pyproj.Proj("+init=EPSG:4612")
    EPSG2451 = pyproj.Proj("+init=EPSG:2451")
    y,x = pyproj.transform(EPSG4612, EPSG2451, lon,lat)
    return (x, y)

x, y = merc(lat, long)
print("------------------------------------------------")
print("Pseudo-Mercator Projection:")
print("x={}, y={}".format(x, y))
x, y = merc_pyproj(lat, long)
print("------------------------------------------------")
print("EPSG-based Projection:")
print("x={}, y={}".format(x, y))

###################end of code########################
# base point is different between generic mercator projection and EPSG-based projection
# that is why coordinate values are totally different
# you can use any one as you want
