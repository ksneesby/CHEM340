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


mean_df = df['CYA'].groupby([df['Lat'], df['Lon']]).mean().unstack()

lon = np.array(df.drop_duplicates(subset='Lon')['Lon'])
lat = np.array(df.drop_duplicates(subset='Lat')['Lat'])
data = mean_df




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

condensed_df['DIA'],condensed_df['COC'],condensed_df['CYA']=np.NaN,np.NaN,np.NaN
