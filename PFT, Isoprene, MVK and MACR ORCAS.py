#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:42:01 2018

@author: kate
"""

import xarray as xr
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd





ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*01.nc', concat_dim = 'time')
#ds=xr.open_dataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\PhytoDOAS-PFT-v3.3_200208.nc')


df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)


meanCYA_df = df['CYA'].groupby([df['Lat'], df['Lon']]).mean().unstack()
meanCOC_df = df['COC'].groupby([df['Lat'], df['Lon']]).mean().unstack()
meanDIA_df = df['DIA'].groupby([df['Lat'], df['Lon']]).mean().unstack()

lon = np.array(df.drop_duplicates(subset='Lon')['Lon'])
lat = np.array(df.drop_duplicates(subset='Lat')['Lat'])
data = meanCYA_df




df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values
#df = pd.read_csv('C:\Users\Kate\Documents\CHEM340repository\CHEM340\ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values

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

condensed_df = DataFrame(data=[df["LONC"][:counter],df["LATC"][:counter],df["Isoprene_TOGA"][:counter],df["MVK_TOGA"][:counter],df["MACR_TOGA"][:counter]])
condensed_df = condensed_df.T

condensed_df.dropna(thresh=3, inplace=True)
condensed_df.reset_index(inplace = True, drop=True)

condensed_df['DIA'],condensed_df['COC'],condensed_df['CYA']=np.NaN,np.NaN,np.NaN

row=0

for i in range(len(condensed_df)):
    lon_value = condensed_df.iloc[i,0]
    lat_value = condensed_df.iloc[i,1]
    
    lon=list(meanCYA_df.columns.values)
    lat= list(meanCYA_df.index.values)
    
    counter=0
    loncount=[]
    latcount=[]
    while counter<len(lon):
        if (lon[counter]-lon_value)>-0.25 and (lon[counter]-lon_value)<0.25:
            loncount=counter
        counter+=1
        
    counter=0
    while counter<len(lat):
        if (lat[counter]-lat_value)>-0.25 and (lat[counter]-lat_value)<0.25:
            latcount=counter
        counter+=1
    
    condensed_df.loc[row,'DIA'] = meanDIA_df.iloc[loncount,latcount]
    condensed_df.loc[row,'COC'] = meanCOC_df.iloc[loncount,latcount]
    condensed_df.loc[row,'CYA'] = meanCYA_df.iloc[loncount,latcount]
    row +=1
    
mean_condensed_df = condensed_df.groupby('CYA', as_index=False).mean()

# =============================================================================
# plt.figure(1)
# plt.plot(mean_condensed_df["MACR_TOGA"],mean_condensed_df["CYA"],"o",ms=2, color="blue")
# plt.xlabel ("MACR")
# plt.ylabel ("CYA")
# plt.xlim(0,4)
# plt.ylim(0,0.1)
# =============================================================================
