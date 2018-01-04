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

df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values

lon,lat= df["LONC"],df["LATC"]

lons = lon[216]
lats = lat[216]
dats = data[216]

data = df["Isoprene_TOGA"]

map = Basemap(projection='robin',lon_0=-70,lat_0=0)

map.drawcoastlines(color = 'black')
map.drawcountries(color='black')


x, y = map(lons, lats)

map.scatter(lons, lats)


216-221


pyplot.show()
