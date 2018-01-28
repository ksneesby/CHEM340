#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:12:46 2018

@author: kate
"""



import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as pyplot
import numpy

#df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values
df = pd.read_csv('C:\Users\Kate\Documents\CHEM340repository\CHEM340\ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values

#sort data file according to altitude
df.sort_values(['ALTG_SRTM'], ascending=True, inplace=True)
df.reset_index(inplace = True)

#find row in which altitude is above 2000
counter = 0

for i in range (len(df["ALTG_SRTM"])):
    if df["ALTG_SRTM"][i] <= 2000:
        counter = counter + 1

alt = df["ALTG_SRTM"][:counter].values
lon = df["LONC"][:counter].values
lat = df["LATC"][:counter].values
data = df["Isoprene_TOGA"][:counter].values

# 1. Draw the map background
fig = pyplot.figure(figsize=(8, 8))
#m = Basemap(projection='robin',lon_0=-70,lat_0=0)

m = Basemap(projection='aeqd',lon_0 = -70,lat_0 = -70,width = 10000000,height = 10000000)

m.drawcoastlines(color='black')
m.drawcountries(color='black')


# 2. scatter Isoprene data
m.scatter(lon, lat, latlon=True, c=data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)

# 3. create colorbar and legend
pyplot.colorbar(label=r'Isoprene')

