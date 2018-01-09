#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:15:45 2018

@author: kate
"""

import xarray as xr
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as pyplot
import numpy


ds=xr.open_dataset('/home/kate/Documents/CHEM340/PhytoDOAS-PFT-v3.3/PhytoDOAS-PFT-v3.3_200208.nc')


lat = ds.Lat
lon = ds.Lon
DIA = ds.DIA
COC = ds.COC
CYA = ds.CYA



# =============================================================================
# CYA_site = CYA.sel(lat=-180,lon=-60,method='nearest')
# 
# CYA_site.plot()
# =============================================================================






