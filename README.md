## GPS2XY-helper
Simple coordinate transformation from (latitude, longitude) to (X, Y)

### Environment
Maintained by [miniconda](https://conda.io/miniconda.html)
* python: 3.5.2
* pyproj: 1.9.5.1
```
conda install pyproj
```

### Usage
Just run:
```
python gps2xy.py
```
Then output is:

![](https://user-images.githubusercontent.com/10651438/45730981-fd991700-bc0f-11e8-9ace-60e7b12b90eb.JPG)

### Description
This repository provides 2 types of coordinate transformation:
#### 1. Spherical Pseudo-Mercator projection
This is generic projection approach which is described in [wiki of OSM](https://wiki.openstreetmap.org/wiki/Mercator#Python). This result should be scaled up based on [(approx.) earth radius](https://en.wikipedia.org/wiki/Earth_radius), then final code becomes like [this blog post](https://towardsdatascience.com/exploring-and-visualizing-chicago-transit-data-using-pandas-and-bokeh-part-ii-intro-to-bokeh-5dca6c5ced10). Here is code:
```
def merc(lat,lon):
    r_major = 6378137.000 # earth radius
    x = r_major * math.radians(lon)
    scale = x/lon
    y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
    return (x, y)
```

#### 2. EPSG-based projection
This is more precise approach based on EPSG code. EPSG code is set per small area, so the code is changed by location. General explanation is described in [doc](https://jswhit.github.io/pyproj/). Logic is difficult, but how to use is easy. Here is example of Tokyo:
```
def merc_pyproj(lat,lon):
    EPSG4612 = pyproj.Proj("+init=EPSG:4612")
    EPSG2451 = pyproj.Proj("+init=EPSG:2451")
    y,x = pyproj.transform(EPSG4612, EPSG2451, lon,lat)
    return (x, y)
```
You just need to search correct EPSG code for your location.

### Reference (Japanese)
* [pyproj example](http://sanvarie.hatenablog.com/entry/2016/01/04/170242)
* [pyproj explanation](https://ikatakos.com/pot/programming/python/packages/pyproj)

This repository is linked to [my blog post](http://nobutobook.blogspot.com/2018/09/pythonxy.html) :-)
