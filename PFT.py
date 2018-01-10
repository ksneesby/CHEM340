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



ds=xr.open_mfdataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/*.nc', concat_dim = 'time')
#ds=xr.open_mfdataset('C:\Users\Kate\Documents\CHEM340repository\CHEM340\PhytoDOAS-PFT-v3.3\*.nc', concat_dim = 'time')

time = ds.time
lat = ds.Lat
lon = ds.Lon
DIA = ds.DIA
COC = ds.COC
CYA = ds.CYA

pyplot.figure(1)
COC_site = COC.sel(lat = -180, lon = -60)
COC_site.plot(color = 'red')
pyplot.figure(2)
DIA_site = DIA.sel(lat = -180, lon = -60)
DIA_site.plot(color = 'blue')
pyplot.figure(3)
CYA_site = CYA.sel(lat = -180, lon = -60)
CYA_site.plot(color = 'green')




