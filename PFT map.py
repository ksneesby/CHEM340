#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:15:45 2018

@author: kate
"""

from netCDF4 import MFDataset, Dataset
import xarray as xr
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as pyplot
import numpy



ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/PhytoDOAS-PFT-v3.3_200208.nc')
#ds=xr.open_dataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\PhytoDOAS-PFT-v3.3_200208.nc')



df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)



lon = df["Lon"].values
lat = df["Lat"].values
data = df["CYA"].values


# draw the map background
fig = pyplot.figure(figsize=(8, 8))

#m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)
m = Basemap(projection='robin',lon_0 = -180,lat_0 = -60)

m.drawcoastlines(color = "black")
m.drawcountries(color = "black")


# scatter Isoprene data
m.scatter(lon, lat, latlon=True, c=data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=0.2, s=20)


# hide land data points
m.fillcontinents(color='white')


# create colorbar and legend
pyplot.colorbar(label=r'CYA')

