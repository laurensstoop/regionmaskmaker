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
PATH_TO_NUTS1 = PATH_TO_PRO

print('NOTIFY: Initialization is complete, Skynet active')
#%%
# =============================================================================
# Load in the base file where stuff can be, select the regions, save the files
# =============================================================================

# Load the shapefile
nuts = gpd.read_file(PATH_TO_SHAPEFILE)
# nuts.head()