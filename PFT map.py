#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:15:45 2018

@author: kate
"""


# =============================================================================
# ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*01.nc', concat_dim ='time')
# ds.mean
# =============================================================================

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pandas import DataFrame

plt.figure(figsize=(8, 8))

m = Basemap(lon_0 = 130,lat_0 = -60)

#m = Basemap(llcrnrlon = -180, llcrnrlat = -90, urcrnrlon = 180, urcrnrlat = 90)
m.drawcoastlines()
m.drawcountries(color = "black")

ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/PhytoDOAS-PFT-v3.3_200301.nc')
#ds=xr.open_dataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\PhytoDOAS-PFT-v3.3_200208.nc')



df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)


new_df = df.pivot(index='Lon', columns='Lat', values='CYA')


lon = np.array(df.drop_duplicates(subset='Lon')['Lon'])
lat = np.array(df.drop_duplicates(subset='Lat')['Lat'])
data = new_df
data=data.T


# you have to write just like here to convert coordinates
x,y = m(lon,lat)



col = m.pcolormesh(x,y,data,cmap=plt.get_cmap('viridis'), latlon=True,vmin=0,vmax=0.2,linewidth=0,rasterized=True)

# hide land data points
m.fillcontinents(color='white')

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

