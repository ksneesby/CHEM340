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


#ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/syn_glb_level3_20020801.nc')
ds=xr.open_mfdataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\*.nc', concat_dim = 'time')



time = ds.time
lat = ds.variables['Lat'][:]
lon = ds.Lon
DIA = ds.DIA
COC = ds.COC
CYA = ds.CYA


# =============================================================================
# CYA_site = CYA.sel(lat = -70, lon = -160, method = 'nearest')
# CYA_site.plot()
# =============================================================================


pyplot.plot(time,CYA[:,150,300])
pyplot.show()






# =============================================================================
# # draw the map background
# fig = pyplot.figure(figsize=(8, 8))
# 
# m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)
# 
# m.drawcoastlines(color = "black")
# m.drawcountries(color = "black")
# 
# 
# # scatter Isoprene data
# m.scatter(lon, lat, latlon=True, c=CYA, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)
# 
# 
# # hide land data points
# m.fillcontinents(color='white')
# 
# 
# # create colorbar and legend
# pyplot.colorbar(label=r'CYA')
# 
# =============================================================================
