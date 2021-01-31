#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restructered on Thu 14 Jan 2021 12:58

@author: Laurens Stoop - l.p.stoop@uu.nl

Following example by Matteo de Felice: http://www.matteodefelice.name/post/aggregating-gridded-data/
"""

#%%
# =============================================================================
# Dependencies
# =============================================================================


## Importing modules
import xarray as xr 
import numpy as np
import regionmask
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Set the path for the data
PATH_TO_PROJECT = '/home/stoop/Documents/Project/regionmaskmaker/'
PATH_TO_NUTS0 = PATH_TO_PROJECT+'./data/raw/NUTS_RG_01M_2021_4326_LEVL_0.shp/NUTS_RG_01M_2021_4326_LEVL_0.shp'
PATH_TO_NUTS1 = PATH_TO_PROJECT+'./data/raw/NUTS_RG_01M_2021_4326_LEVL_1.shp/NUTS_RG_01M_2021_4326_LEVL_1.shp'

# Read NetCDF
FOLDER_WITH_NETCDF = '/emhires-data/data-warehouse/gridded/ERA5/'


print('NOTIFY: Initialization is complete, Skynet active')
#%%
# =============================================================================
# Load in the base file where stuff can be, select the regions, save the files
# =============================================================================

# Load the shapefile
nuts0 = gpd.read_file(PATH_TO_NUTS0)
nuts1 = gpd.read_file(PATH_TO_NUTS1)
# nuts.head() # to check the contents

# Load in the NetCDF
# d = xr.open_mfdataset(FOLDER_WITH_NETCDF+'era5-hourly-2m_temperature-2018-*.nc', chunks = {'time': 10})
# d = d.assign_coords(longitude=(((d.longitude + 180) % 360) - 180)).sortby('longitude')