#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:15:45 2018

@author: kate
"""

from netCDF4 import MFDataset, Dataset
import xarray as xr
import pandas as pd
from mpl_toolkits.basemap import Basemap, addcyclic
import matplotlib.pyplot as pyplot
import numpy
import numpy.ma as ma

# =============================================================================
# ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*01.nc', concat_dim ='time')
# ds.mean
# =============================================================================


ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/PhytoDOAS-PFT-v3.3_200301.nc')
#ds=xr.open_dataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\PhytoDOAS-PFT-v3.3_200208.nc')



df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)


new_df = df.pivot(index='Lon', columns='Lat', values='CYA')


lon = numpy.arange(-179.75, 180, 0.5)
lat = numpy.arange(-89.75, 90, 0.5)
data = new_df





# transform lon/lat to coordinate grid

lon,lat = numpy.meshgrid(lon,lat, sparse=True)


# Set up the map

map=Basemap(projection='robin',lon_0=-130,lat_0=0)

f=pyplot.figure()


# plot the data

col=map.pcolormesh(lon,lat,data, latlon=True,cmap=pyplot.get_cmap('viridis'),vmin=0,vmax=0.3,linewidth=0,rasterized=True)

col.set_edgecolor('face')
                                                                           

# improve the map

map.drawcoastlines(color='black')

map.drawcountries(color='black')


# add a color bar

cb = map.colorbar(col, "bottom")















# =============================================================================
# # draw the map background
# fig = pyplot.figure(figsize=(8, 8))
# 
# #m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)
# m = Basemap(projection='robin',lon_0 = -180,lat_0 = -60)
# 
# m.drawcoastlines(color = "black")
# m.drawcountries(color = "black")
# 
# 
# # scatter CYA data
# #m.scatter(lon, lat, latlon=True, c=data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=0.3, s=20)
# 
# 
# # hide land data points
# m.fillcontinents(color='white')
# 
# 
# # create colorbar and legend
# pyplot.colorbar(label=r'CYA')
# =============================================================================

