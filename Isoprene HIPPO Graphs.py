# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap, maskoceans
import matplotlib.pyplot as pyplot
import numpy

df = pd.read_csv('/home/kate/Documents/CHEM340/HIPPO/HIPPO_discrete_continuous_merge_20121129.tbl', sep=' ') 

lon = df["GGLON"].values
lat = df["GGLAT"].values
data = df["Isoprene_AW"].values


# 1. Draw the map background
fig = pyplot.figure(figsize=(8, 8))


#m = Basemap(projection='robin',lon_0=-70,lat_0=0)

m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)

m.drawcoastlines(color='black')
m.drawcountries(color='black')


new_data = maskoceans(lon, lat, data, inlands=False, resolution='l', grid=5)

# 2. scatter Isoprene data
m.scatter(lon, lat, latlon=True, c=new_data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)


# 3. create colorbar and legend
pyplot.colorbar(label=r'Isoprene')





