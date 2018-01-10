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


# =============================================================================
# ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*01.nc', concat_dim ='time')
# ds.mean
# =============================================================================


ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/PhytoDOAS-PFT-v3.3_200301.nc')
#ds=xr.open_dataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\PhytoDOAS-PFT-v3.3_200208.nc')



df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)


lon = df["Lon"].values
lat = df["Lat"].values
data = df["CYA"].values


# repeat last data column to avoid white space    

#data,lon = addcyclic(data, lon)

    

# transform lon/lat to coordinate grid

lon,lat = numpy.meshgrid(lon,lat, sparse = True)

    

# Set up the map

map=Basemap(projection='robin',lon_0=-180,lat_0=-60)

f=pyplot.figure()

    

# plot the data

col=map.pcolormesh(lon,lat,data,latlon=True, cmap=pyplot.get_cmap('viridis'),linewidth=0, rasterized=True)

col.set_edgecolor('face')

                                                                                   

# improve the map

map.drawcoastlines(color='black')

map.drawcountries(color='black')



# add a color bar

cb = map.colorbar(col, "bottom")

cb.set_label(CYA.upper()+', ppt')
                                      
                                  

                                                                                   






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
# m.pcolormesh(lon, lat, data)
# 
# 
# # hide land data points
# m.fillcontinents(color='white')
# 
# 
# # create colorbar and legend
# pyplot.colorbar(label=r'CYA')
# =============================================================================

