# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:29:57 2023

@author: mevans

@description: This script will generate annual NAIP imagery tiles for each
CPW state in two different years based on an input json file
"""
import glob
import json
import os
from os.path import join
import datetime

#TODO: if we can create a single environment with gee and arcpy libraries
# we don't have to write an intermediate json file. This script can be
# combined directly with 'add_naip_arcpro.py
import ee

## GEE STUFF
# authenticate our ee client
ee.Authenticate()
ee.Initialize()

# get NAIP and TIGER catalogs
TIGER = ee.FeatureCollection("TIGER/2018/States")
# aoi = TIGER.filter(ee.Filter.inList('NAME', ['Delaware', 'District of Columbia', 'Maryland', 'Pennsylvania', 'New York', 'Virginia', 'West Virginia']))
NAIP = ee.ImageCollection("USDA/NAIP/DOQQ")#.filterBounds(aoi)

# define image visualization parameters
naip_viz_params = {
  'bands':['R', 'G', 'B'],
  'min': 0,
  'max': 200
}

# function to get tile urls
def get_map_url(collection, year, viz_params):
    """Generate GEE map tile urls
    
    Params
    ---
    collection: ee.ImageCollection
        Image collection to be visualized (e.g., NAIP)
    year: int
        Year of imagery to visualize
    viz_params: dict
        GEE visualization parameters dictionary
    
    Return
    ---
    str: url of imagery tiles
    """
    img = ee.ImageCollection(collection).filterDate(f'{year}-01-01', f'{year}-12-31').median()
    map_id_dict = ee.Image(img).getMapId(viz_params)
    tiles = map_id_dict['tile_fetcher'].url_format
    return tiles

## read the most recent NAIP tile json
wdir = "//chesconse-app01/k//GIS/CBP_Obj_1/Analysis/LCCAA/NAIP_services"
naip_dictionaries = glob.glob(join(wdir, "NAIP_refresh*.json")) 
latest_file = max(naip_dictionaries, key=os.path.getctime)

# get current datetime
now = datetime.datetime.now().strftime("%m-%d-%y-%H%M")

with open(latest_file) as json_file:
    layerData = json.load(json_file)

# loop through states and update gee tile urls
for state, data in layerData.items():
    year1 = data['T1']
    year2 = data['T2']
    tigername = data['TIGER']
    print(tigername)
    aoi = TIGER.filterMetadata('NAME', 'equals', tigername)
    naip = NAIP.filterBounds(aoi)
    tiles1 = get_map_url(naip, year1, naip_viz_params)
    tiles2 = get_map_url(naip, year2, naip_viz_params)
    data['T1url'] = tiles1
    data['T2url'] = tiles2
    
# write updated dictionary to new json file
new_filename = f'NAIP_refresh_{now}.json'
with open(join(wdir, new_filename), 'w') as f:
    json.dump(layerData, f)
    
