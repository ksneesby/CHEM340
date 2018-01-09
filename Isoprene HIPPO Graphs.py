# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as pyplot

# read data file
df = pd.read_csv('/home/kate/Documents/CHEM340/HIPPO/HIPPO_discrete_continuous_merge_20121129.tbl', sep=' ') 

#sort data file according to altitude
df.sort_values(['GGALT'], ascending=True, inplace=True)
df.reset_index(inplace = True, drop=True)

#find row in which altitude is above 2000
counter = 0

for i in range (len(df["GGALT"])):
    if df["GGALT"][i] <= 2000:
        counter = counter + 1

# plot graphs using data where altitude is below 2000
pyplot.figure(1)
pyplot.plot(df["UTC"][:counter],df["Isoprene_AW"][:counter],"o", ms=2, color="red")
pyplot.xlabel ("Time (UTC seconds since midnight)")
pyplot.ylabel ("Isoprene")

pyplot.figure(2)
pyplot.plot(df["GGALT"][:counter],df["Isoprene_AW"][:counter],"o",ms=2, color="blue")
pyplot.xlabel ("Altitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(3)
pyplot.plot(df["GGLAT"][:counter],df["Isoprene_AW"][:counter],"o",ms=2, color="green")
pyplot.xlabel ("Latitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(4)
pyplot.plot(df["GGLON"][:counter],df["Isoprene_AW"][:counter],"o",ms=2, color="purple")
pyplot.xlabel ("Longitude")
pyplot.ylabel ("Isoprene")



pyplot.show()