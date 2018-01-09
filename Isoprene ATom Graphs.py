# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as pyplot

# read in data file
df1 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160808_R5.ict', sep=',', skiprows=514, na_values = "-99999") 
df2 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160812_R5.ict', sep=',', skiprows=526, na_values = "-99999")
df3 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20160815_R5.ict', sep=',', skiprows=526, na_values = "-99999")
df4 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170205_R3.ict', sep=',', skiprows=521, na_values = "-99999")
df5 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170210_R3.ict', sep=',', skiprows=521, na_values = "-99999")
df6 = pd.read_csv('/home/kate/Documents/CHEM340/ATom/MER-TOGA_DC8_20170213_R3.ict', sep=',', skiprows=521, na_values = "-99999")

df = df1.append([df2, df3, df4, df5, df6])

#sort data file according to altitude
df.sort_values(['G_ALT'], ascending=True, inplace=True)
df.reset_index(inplace = True, drop = True)

#find row in which altitude is above 2000
counter = 0

for i in range (len(df["G_ALT"])):
    if df["G_ALT"][i] <= 2000:
        counter = counter + 1

# plot graphs using data where altitude is below 2000

pyplot.figure(1)
pyplot.plot(df["G_ALT"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="blue")
pyplot.xlabel ("Altitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(2)
pyplot.plot(df["MVK_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="orange")
pyplot.xlabel ("MVK")
pyplot.ylabel ("Isoprene")

pyplot.figure(3)
pyplot.plot(df["MACR_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="brown")
pyplot.xlabel ("MACR")
pyplot.ylabel ("Isoprene")

pyplot.figure(4)
pyplot.plot(df["DMS_TOGA"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="green")
pyplot.xlabel ("DMS")
pyplot.ylabel ("Isoprene")

pyplot.figure(5)
pyplot.plot(df["j[CH3ONO2->CH3O+NO2]"][:counter],df["Isoprene_TOGA"][:counter],"o",ms=2, color="purple")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("Isoprene")

pyplot.figure(6)
pyplot.plot(df["MACR_TOGA"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="pink")
pyplot.xlabel ("MACR")
pyplot.ylabel ("MVK")

pyplot.figure(7)
pyplot.plot(df["DMS_TOGA"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="aqua")
pyplot.xlabel ("DMS")
pyplot.ylabel ("MVK")

pyplot.figure(8)
pyplot.plot(df["j[CH3ONO2->CH3O+NO2]"][:counter],df["MVK_TOGA"][:counter],"o",ms=2, color="violet")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("MVK")

pyplot.figure(9)
pyplot.plot(df["DMS_TOGA"][:counter],df["MACR_TOGA"][:counter],"o",ms=2, color="red")
pyplot.xlabel ("DMS")
pyplot.ylabel ("MACR")

pyplot.figure(10)
pyplot.plot(df["j[CH3ONO2->CH3O+NO2]"][:counter],df["MACR_TOGA"][:counter],"o",ms=2, color="green")
pyplot.xlabel ("Methyl nitrate")
pyplot.ylabel ("MACR")

pyplot.show()