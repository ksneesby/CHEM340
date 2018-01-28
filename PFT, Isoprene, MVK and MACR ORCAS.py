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
from scipy import stats



#ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*.nc', concat_dim = 'time')
ds=xr.open_mfdataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\*.nc', concat_dim = 'time')



df=ds.to_dataframe()
df.reset_index(inplace = True, drop = True)


meanCYA_df = df['CYA'].groupby([df['Lat'], df['Lon']]).mean().unstack()
meanCOC_df = df['COC'].groupby([df['Lat'], df['Lon']]).mean().unstack()
meanDIA_df = df['DIA'].groupby([df['Lat'], df['Lon']]).mean().unstack()

lon = np.array(df.drop_duplicates(subset='Lon')['Lon'])
lat = np.array(df.drop_duplicates(subset='Lat')['Lat'])
data = meanCYA_df




#df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values
df = pd.read_csv('C:\Users\Kate\Documents\CHEM340repository\CHEM340\ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values

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


# Remove outliers that are more than 3 standard deviations away from the mean

isoprene_mean = np.mean(condensed_df['Isoprene_TOGA'])
MVK_mean = np.mean(condensed_df['MVK_TOGA'])
MACR_mean = np.mean(condensed_df['MACR_TOGA'])

isoprene_std = np.std(condensed_df['Isoprene_TOGA'])
MVK_std = np.std(condensed_df['MVK_TOGA'])
MACR_std = np.std(condensed_df['MACR_TOGA'])




# Correlate Isoprene, MVK and MACR data with PFT values from closest lat/lon node

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


#Plot linear regression plots for combinations of each variable.

###################Set x and y#########################
x = mean_condensed_df["DIA"]
y = mean_condensed_df["Isoprene_TOGA"]
xlabel = "Diatoms (mgCHLa/m3)"
ylabel = "Isoprene"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(1)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.text(0.22,25,'r-squared = ' +str(r_value**2))
plt.ylim(0,30)

###################Set x and y#########################
x = mean_condensed_df["COC"]
y = mean_condensed_df["Isoprene_TOGA"]
xlabel = "Coccolithophores (mgCHLa/m3)"
ylabel = "Isoprene"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(2)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.text(0,25,'r-squared = ' +str(r_value**2))
plt.ylim(0,30)

###################Set x and y#########################
x = mean_condensed_df["CYA"]
y = mean_condensed_df["Isoprene_TOGA"]
xlabel = "Cyanobacteria (mgCHLa/m3)"
ylabel = "Isoprene"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(3)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,30)
plt.text(0.3,25,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LATC"]
y = mean_condensed_df["Isoprene_TOGA"]
xlabel = "Latitude"
ylabel = "Isoprene"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(4)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,30)
plt.text(-53,25,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LONC"]
y = mean_condensed_df["Isoprene_TOGA"]
xlabel = "Longitude"
ylabel = "Isoprene"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(5)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,30)
plt.text(-90,25,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["DIA"]
y = mean_condensed_df["MVK_TOGA"]
xlabel = "Diatoms (mgCHLa/m3)"
ylabel = "MVK"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(6)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,25)
plt.text(0.2,20,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["COC"]
y = mean_condensed_df["MVK_TOGA"]
xlabel = "Coccolithophores (mgCHLa/m3)"
ylabel = "MVK"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(7)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,25)
plt.text(0,20,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["CYA"]
y = mean_condensed_df["MVK_TOGA"]
xlabel = "Cyanobacteria (mgCHLa/m3)"
ylabel = "MVK"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(8)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,25)
plt.text(0.3,20,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LATC"]
y = mean_condensed_df["MVK_TOGA"]
xlabel = "Latitude"
ylabel = "MVK"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(9)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,25)
plt.text(-50,20,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LONC"]
y = mean_condensed_df["MVK_TOGA"]
xlabel = "Longitude"
ylabel = "MVK"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(10)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,25)
plt.text(-90,20,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["DIA"]
y = mean_condensed_df["MACR_TOGA"]
xlabel = "Diatoms (mgCHLa/m3)"
ylabel = "MACR"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(11)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,15)
plt.text(0.2,12,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["COC"]
y = mean_condensed_df["MACR_TOGA"]
xlabel = "Coccolithophores (mgCHLa/m3)"
ylabel = "MACR"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(12)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,15)
plt.text(0,12,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["CYA"]
y = mean_condensed_df["MACR_TOGA"]
xlabel = "Cyanobacteria (mgCHLa/m3)"
ylabel = "MACR"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(13)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,15)
plt.text(0.3,12,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LATC"]
y = mean_condensed_df["MACR_TOGA"]
xlabel = "Latitude"
ylabel = "MACR"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(14)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,15)
plt.text(-50,12,'r-squared = ' +str(r_value**2))

###################Set x and y#########################
x = mean_condensed_df["LONC"]
y = mean_condensed_df["MACR_TOGA"]
xlabel = "Longitude"
ylabel = "MACR"


# Generated linear fit
mask = ~np.isnan(x) & ~np.isnan(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask],y[mask])
line = slope*x+intercept

plt.figure(15)
plt.plot(x,y,"o", ms=2, color="blue")
plt.plot(x, intercept + slope*x, 'r')
plt.xlabel (xlabel)
plt.ylabel (ylabel)
plt.ylim(0,15)
plt.text(-90,12,'r-squared = ' +str(r_value**2))


 

