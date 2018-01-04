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


lon = df["LONC"].values
lat = df["LATC"].values
data = df["Isoprene_TOGA"].values




# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='robin',lon_0=-70,lat_0=0)


m.drawcoastlines(color='black')
m.drawcountries(color='black')


# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True, c=data, cmap='RdBu_r', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'Isoprene')
plt.clim(1, 744)