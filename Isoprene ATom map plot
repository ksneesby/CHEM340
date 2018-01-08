# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as pyplot
import numpy


# read in data file
df1 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160808_R5.ict', sep=',', skiprows=514, na_values = "-99999") 
df2 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160812_R5.ict', sep=',', skiprows=526, na_values = "-99999")
df3 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160815_R5.ict', sep=',', skiprows=526, na_values = "-99999")
df4 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170205_R3.ict', sep=',', skiprows=521, na_values = "-99999")
df5 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170210_R3.ict', sep=',', skiprows=521, na_values = "-99999")
df6 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170213_R3.ict', sep=',', skiprows=521, na_values = "-99999")

df = df1.append([df2, df3, df4, df5, df6])

lon = df["G_LONG"].values
lat = df["G_LAT"].values
data = df["Isoprene_TOGA"].values


# draw the map background
fig = pyplot.figure(figsize=(8, 8))

m = Basemap(projection='aeqd',lon_0 = -180,lat_0 = -60,width = 15000000,height = 15000000)


m.drawcoastlines(color = "black")
m.drawcountries(color = "black")


# scatter Isoprene data
m.scatter(lon, lat, latlon=True, c=data, cmap=pyplot.get_cmap('viridis'), vmin=0, vmax=4, s=20)


# hide land data points
m.fillcontinents(color='white')


# create colorbar and legend
pyplot.colorbar(label=r'Isoprene')





