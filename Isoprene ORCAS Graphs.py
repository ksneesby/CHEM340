# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as pyplot

df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values


#sort data file according to altitude
df.sort_values(['ALTG_SRTM'], ascending=True, inplace=True)
df.reset_index(inplace = True, drop=True)

#find row in which altitude is above 2000
counter = 0

for i in range (len(df["ALTG_SRTM"])):
    if df["ALTG_SRTM"][i] <= 2000:
        counter = counter + 1



pyplot.figure(1)
pyplot.plot(df["ALTG_SRTM"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="blue")
pyplot.xlabel ("Altitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(2)
pyplot.plot(df["MACR_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="navy")
pyplot.xlabel ("MACR")
pyplot.ylabel ("Isoprene")

pyplot.figure(3)
pyplot.plot(df["MVK_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="green")
pyplot.xlabel ("MVK")
pyplot.ylabel ("Isoprene")

pyplot.figure(4)
pyplot.plot(df["DMS_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="brown")
pyplot.xlabel ("DMS")
pyplot.ylabel ("Isoprene")

pyplot.figure(5)
pyplot.plot(df["MethylNitrate_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="purple")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("Isoprene")

pyplot.figure(6)
pyplot.plot(df["MACR_TOGA"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="orange")
pyplot.xlabel ("MACR")
pyplot.ylabel ("MVK")

pyplot.figure(7)
pyplot.plot(df["DMS_TOGA"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="cyan")
pyplot.xlabel ("DMS")
pyplot.ylabel ("MVK")

pyplot.figure(8)
pyplot.plot(df["MethylNitrate_TOGA"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="green")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("MVK")

pyplot.figure(9)
pyplot.plot(df["DMS_TOGA"][:counter],df["MACR_TOGA"][:counter],"o",ms=2, color="red")
pyplot.xlabel ("DMS")
pyplot.ylabel ("MACR")

pyplot.figure(10)
pyplot.plot(df["MethylNitrate_TOGA"][:counter],df["MACR_TOGA"][:counter],"o",ms=2, color="red")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("MACR")




pyplot.show()