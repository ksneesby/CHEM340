# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as pyplot
import numpy


# read in data file
df = pd.read_csv('/home/kate/Documents/CHEM340/HIPPO/HIPPO_discrete_continuous_merge_20121129.tbl', sep=' ') 

lon = df["GGLON"].values
lat = df["GGLAT"].values
data = df["Isoprene_AW"].values
alt = df["GGALT"]

# make new longitude, latitude and Isoprene data arrays for data collected at an altitude of 2000 or below

lowAlt_lon = numpy.zeros(5638)
lowAlt_lat = numpy.zeros(5638)
lowAlt_data = numpy.zeros(5638)

counter = 0

for i in range(len(alt)):
    if alt[i]<=2000:
        lowAlt_lon[counter] = lon[i]
        lowAlt_lat[counter] = lat[i]
        lowAlt_data[counter] = data[i]
        counter = counter + 1

# draw the map background
fig = pyplot.figure(figsize=(8, 8))

m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)

m.drawcoastlines(color = "black")
m.drawcountries(color = "black")


# scatter Isoprene data
m.scatter(lowAlt_lon, lowAlt_lat, latlon=True, c=lowAlt_data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)


# hide land data points
m.fillcontinents(color='white')


# create colorbar and legend
pyplot.colorbar(label=r'Isoprene')





