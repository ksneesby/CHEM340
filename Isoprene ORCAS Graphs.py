# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as pyplot

df = pd.read_csv('/home/kate/Downloads/ORCASall.mergeTOGA.tbl', sep=' ', na_values = "-888") #Setting values outside detection limit as NA values


pyplot.figure(1)
pyplot.plot(df["UTC"],df["Isoprene_TOGA"],"o", ms=2, color="red")
pyplot.xlabel ("Time (UTC seconds since midnight)")
pyplot.ylabel ("Isoprene")

pyplot.figure(2)
pyplot.plot(df["ALTG_SRTM"],df["Isoprene_TOGA"],"o",ms=2, color="blue")
pyplot.xlabel ("Altitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(3)
pyplot.plot(df["LATC"],df["Isoprene_TOGA"],"o",ms=2, color="green")
pyplot.xlabel ("Latitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(4)
pyplot.plot(df["LONC"],df["Isoprene_TOGA"],"o",ms=2, color="purple")
pyplot.xlabel ("Longitude")
pyplot.ylabel ("Isoprene")

pyplot.figure(5)
pyplot.plot(df["CO.X"],df["Isoprene_TOGA"],"o",ms=2, color="orange")
pyplot.xlabel ("Carbon Monoxide")
pyplot.ylabel ("Isoprene")

pyplot.figure(6)
pyplot.plot(df["Acetaldehyde_TOGA"],df["Isoprene_TOGA"],"o",ms=2, color="cyan")
pyplot.xlabel ("Acetaldehyde")
pyplot.ylabel ("Isoprene")

pyplot.figure(7)
pyplot.plot(df["Butanal_TOGA"],df["Isoprene_TOGA"],"o",ms=2, color="brown")
pyplot.xlabel ("Butanal")
pyplot.ylabel ("Isoprene")


#Main one's to look at
pyplot.figure(8)
pyplot.plot(df["CH2O_TOGA"],df["Isoprene_TOGA"],"o",ms=2, color="red")
pyplot.xlabel ("Formaldehyde")
pyplot.ylabel ("Isoprene")

pyplot.figure(9)
pyplot.plot(df["MACR_TOGA"],df["Isoprene_TOGA"],"o",ms=2, color="navy")
pyplot.xlabel ("Methacrolein")
pyplot.ylabel ("Isoprene")

pyplot.figure(10)
pyplot.plot(df["MVK_TOGA"],df["Isoprene_TOGA"],"o",ms=2, color="green")
pyplot.xlabel ("Methyl vinyl ketone")
pyplot.ylabel ("Isoprene")


pyplot.show()