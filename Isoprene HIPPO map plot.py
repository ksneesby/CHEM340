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

#sort data file according to altitude
df.sort_values(['GGALT'], ascending=True, inplace=True)
df.reset_index(inplace = True)

#find row in which altitude is above 2000
counter = 0

for i in range (len(df["GGALT"])):
    if df["GGALT"][i] <= 2000:
        counter = counter + 1
        
# use data collected at altitude of 2000 or below        
lon = df["GGLON"][:counter].values
lat = df["GGLAT"][:counter].values
data = df["Isoprene_AW"][:counter].values




# draw the map background
fig = pyplot.figure(figsize=(8, 8))

m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)

m.drawcoastlines(color = "black")
m.drawcountries(color = "black")


# scatter Isoprene data
m.scatter(lon, lat, latlon=True, c=data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)


# hide land data points
m.fillcontinents(color='white')


# create colorbar and legend
pyplot.colorbar(label=r'Isoprene')





