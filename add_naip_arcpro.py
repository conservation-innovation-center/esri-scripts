# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:16:44 2023

@author: mevans

@description: This script will update the data source urls for layers in 
arcpro webmaps used to compare land cover change between two time points

"""

import json
import os
import glob
import arcpy

# Read current naip data json
naip_dictionaries = glob.glob("//chesconse-app01/k//GIS/CBP_Obj_1/Analysis/LCCAA/NAIP_services//NAIP_refresh*.json") 
latest_file = max(naip_dictionaries, key=os.path.getctime)

with open(latest_file) as json_file:
    layerData = json.load(json_file)

def replace_map_layers(Map, pattern):
    """Replace the layers on an arcpy.mp Map object matching given pattern
    
    Params
    ---
    Map: arcpy.mp.Map
        map object holding layers to be replaced
    pattern: str
        regular expression to be matched against layer names
    
    Return
    ---
    None: updates the specified layers in the Map
    """
    layers = Map.listLayers(pattern)
    for layer in layers:
        name = layer.name
        state = name[5:-5]
        print(state)
        subdict = layerData[state]
        Map.removeLayer(layer)
        newlayer = Map.addDataFromPath(subdict['T1url'])
        newlayer.name = name  
            
# get our arcpro projects, maps and layers
projects = glob.glob(r'\\chesconse-app01\K\GIS\CBP_Obj_1\Analysis\LCCAA\Reviewer_Projects\*.aprx')
for path in projects:
    # open the project
    project = arcpy.mp.ArcGISProject(path)
    # get the t1 and t2 maps
    t1map = project.listMaps('T1 Map')[0]
    t2map = project.listMaps('T2 Map')[0]
 
    # replace map1 layers
    replace_map_layers(t1map, 'NAIP*')
    
    # replace map2 layers
    replace_map_layers(t2map, 'NAIP*')

    # save the project
    project.save()