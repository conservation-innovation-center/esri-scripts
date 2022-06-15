# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:58:14 2021
PotomacConservancy.py
@author: pmccabe
"""
# python \\chesconse-app01\k\GIS\Potomac_Conservancy\Scripts\PotomacConservancy.py
import arcpy
import os
import time
import sys
import pandas as pd
arcpy.env.overwriteOutput=True
arcpy.env.snapRaster = r"C:\Users\kwalker\Desktop\snapraster\Phase6_Snap.tif"
arcpy.env.outputCoordinateSystem = r"C:\Users\kwalker\Desktop\snapraster\Phase6_Snap.tif"
arcpy.env.parallelProcessingFactor = "75%"

md_cflist = [
        'alle_24001',
        'fred_24021', 
        'garr_24023',
        'wash_24043'
        ]
#MARYLAND
#Project MD Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD Parcels (14 seconds)')
MD_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\MD\August_2021_Parcels.gdb\parcel_polygons"
MD_Parcels_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\MD\August_2021_Parcels.gdb\MD_Parcels_Projected"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(MD_Parcels, MD_Parcels_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD Parcels')
#Select MD Parcels in desired counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Parcels in desired counties')
MD_Parcels_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\MD\MD_Parcels_Desired_Counties.shp"
# MD_Parcels_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(MD_Parcels_Projected, "NEW_SELECTION", "JURSCODE = 'ALLE' Or JURSCODE = 'GARR' Or JURSCODE = 'WASH' Or JURSCODE = 'FRED'")
# arcpy.CopyFeatures_management(MD_Parcels_Desired_Counties_Selection, MD_Parcels_Desired_Counties)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected MD Parcels in desired counties')
#Calculate MD Parcels in Desired Counties Acreage
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculating MD Parcels in Desired Counties Acreage ( minute)')
# arcpy.CalculateGeometryAttributes_management(MD_Parcels_Desired_Counties,[["Acreage","AREA"]],"","ACRES")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculated MD Parcels in Desired Counties Acreage')
#Select MD Parcels in Desired Counties >= 50 Acres
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Parcels in desired counties')
MD_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\MD\MD_Priority_Parcels.shp"
# MD_Priority_Parcels_Selection = arcpy.management.SelectLayerByAttribute(MD_Parcels_Desired_Counties, "NEW_SELECTION", "Acreage >= 50")
# arcpy.CopyFeatures_management(MD_Priority_Parcels_Selection, MD_Priority_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected MD Parcels in desired counties')
#Project MD SVI
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD SVI (14 seconds)')
MD_SVI = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\SVI2018_MARYLAND_county.shp"
MD_SVI_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_SVI_Projected.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(MD_SVI, MD_SVI_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD SVI')
#Select MD SVI in Desired Counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD SVI in desired counties')
MD_SVI_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_SVI_Desired_Counties.shp"
# MD_SVI_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(MD_SVI_Projected, "NEW_SELECTION", "COUNTY = 'Allegany' Or COUNTY = 'Garrett' Or COUNTY = 'Washington' Or COUNTY = 'Frederick'")
# arcpy.CopyFeatures_management(MD_SVI_Desired_Counties_Selection, MD_SVI_Desired_Counties)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected MD SVI in desired counties')
#Project US SVI Census Tracts
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD SVI (14 seconds)')
US_SVI = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\SVI2018_US\SVI2018_US_tract.shp"
US_SVI_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_Projected.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(US_SVI, US_SVI_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD SVI')
#Select US SVI in Desired MD Counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD SVI in desired counties')
US_SVI_MD_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_MD_Desired_Counties.shp"
# US_SVI_MD_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(US_SVI_Projected, "NEW_SELECTION", "STCNTY = '24001' Or STCNTY = '24023' Or STCNTY = '24043' Or STCNTY = '24021'")
# arcpy.CopyFeatures_management(US_SVI_MD_Desired_Counties_Selection, US_SVI_MD_Desired_Counties)
# arcpy.CalculateField_management(US_SVI_MD_Desired_Counties, "Value", "0", "PYTHON3")
# with arcpy.da.UpdateCursor(US_SVI_MD_Desired_Counties, ['RPL_THEMES', 'Value']) as cursor:
#     for row in cursor:
#         RPL = row[0]
#         if RPL <= 0:
#             row[1] = 1
#             cursor.updateRow(row)
#         if 0 < RPL <= 0.25:
#             row[1] = 2
#             cursor.updateRow(row)
#         if 0.25 < RPL <= 0.5:
#             row[1] = 3
#             cursor.updateRow(row)
#         if 0.5 < RPL <= 0.75:
#             row[1] = 4
#             cursor.updateRow(row)
#         if RPL > 0.75:
#             row[1] = 5
#             cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected MD SVI in desired counties')
#Create US_SVI_MD Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating US_SVI_MD Raster (9 minutes)')
US_SVI_MD_Desired_Counties_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_MD.tif"
# arcpy.PolygonToRaster_conversion(US_SVI_MD_Desired_Counties, "Value", US_SVI_MD_Desired_Counties_Raster, "CELL_CENTER","",1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created US_SVI_MD Raster')
#Project National Historic Landmarks
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project National Historic Landmarks (14 seconds)')
National_Historic_Landmarks = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\Base Data Sets\NationalHistoricLandmarks.shp"
National_Historic_Landmarks_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\National_Historic_Landmarks_Projected.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(National_Historic_Landmarks, National_Historic_Landmarks_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected National Historic Landmarks')
#Project National Register of Historic Sites and Places (NRHP)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project National Historic Landmarks (14 seconds)')
NRHP = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\Base Data Sets\NRHP.shp"
NRHP_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\NRHP_Projected.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(NRHP, NRHP_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected National Historic Landmarks')
#Project Water Quality Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Water Quality Raster (14 seconds)')
WQ_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\wq"
WQ_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\wq_proj.tif"
# arcpy.management.ProjectRaster(WQ_Raster, WQ_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "36.73 36.73", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Water Quality Raster')
#Project TNC Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project TNC Raster (14 seconds)')
TNC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\Resilient_and_Connected_Landscapes\Resilient_and_Connected_Landscapes\Resilient_and_Connected_Data.gdb\Resilient_and_Connected"
TNC_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\TNC.tif"
# arcpy.management.ProjectRaster(TNC_Raster, TNC_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "30 30", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected TNC Raster')
#Project Drinking Water Quality Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Drinking Water Quality Raster (14 seconds)')
DWQ_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\Land_Prioritization.gdb\CumPrio"
DWQ_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\DWQ.tif"
# arcpy.management.ProjectRaster(DWQ_Raster, DWQ_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "30 30", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Drinking Water Quality Raster')
#Project Maryland Development Vulnerability 2025 Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Maryland Development Vulnerability 2025 Raster (14 seconds)')
MD_DevV_2025_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\CIC_PotomacConservancy\md_cz_2021_dev_vulnerability_2025.tif"
MD_DevV_2025_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\MD_DevV_2025.tif"
# arcpy.management.ProjectRaster(MD_DevV_2025_Raster, MD_DevV_2025_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "30 30", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Maryland Development Vulnerability 2025 Raster')
#Project Baywide Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Baywide Trails (14 seconds)')
Baywide_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide Trails.shp"
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(Baywide_Trails, Baywide_Trails_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Baywide Trails')
#Project NHD Flowlines
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Baywide Trails (14 seconds)')
NHD_Flowlines = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\NHDPLUS_H_0207_HU4_GDB\NHDPLUS_H_0207_HU4_GDB.gdb\Hydrography\NHDFlowline"
NHD_Flowlines_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\NHDFlowline_Proj.shp"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(NHD_Flowlines, NHD_Flowlines_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Baywide Trails')
#Select StreamRivers
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select StreamRivers')
StreamRivers = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\StreamRiver.shp"
# StreamRiver_Selection = arcpy.management.SelectLayerByAttribute(NHD_Flowlines_Projected, "NEW_SELECTION", "FType = 460 OR FType = 558")
# arcpy.CopyFeatures_management(StreamRiver_Selection, StreamRivers)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected StreamRivers')
#Buffer StreamRivers by 100 Feet
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffering StreamRivers by 100 feet ( seconds)')
StreamRiver_Buffer = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\StreamRiver_Buffer.shp"
# arcpy.analysis.PairwiseBuffer(StreamRivers, StreamRiver_Buffer, "100 Feet","ALL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffered StreamRivers by 100 feet')
#Create List of MD LU rasters
MD_LU_Raster_List = []
for cf in md_cflist:
    print('############################')
    print('####### {} #########'.format(cf))
    print('############################')
    cf_LU_Raster = r"C:\Users\kwalker\Desktop\V1_MD_LU\{}_lu_2017_2018.tif".format(cf)
    MD_LU_Raster_List.append(cf_LU_Raster)
#Mosaic LU Rasters
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC LU Raster (14 minutes)')
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU", "MD_PC_LU.gdb")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\MD_PC_LU.gdb","MD_PC_LU_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\MD_PC_LU.gdb\MD_PC_LU_mosaic","Raster Dataset",MD_LU_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\MD_PC_LU.gdb\MD_PC_LU_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\MD_PC_LU.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC LU Raster')
#Create List of MD LC rasters
MD_LC_Raster_List = []
for cf in md_cflist:
    print('############################')
    print('####### {} #########'.format(cf))
    print('############################')
    cf_LC_Raster = r"C:\Users\kwalker\Desktop\V1_MD_LC\{}\{}_landcover_2018_June2021.tif".format(cf,cf)
    MD_LC_Raster_List.append(cf_LC_Raster)
#Mosaic LC Rasters
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC LC Raster (12 minutes)')
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC", "MD_PC_LC.gdb")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.gdb","MD_PC_LC_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "8_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.gdb\MD_PC_LC_mosaic","Raster Dataset",MD_LC_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.gdb\MD_PC_LC_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif","",255,255,"NONE","NONE","8_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC LC Raster')
#Create MD Tree Canopy Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC TC Raster (7 minutes)')
MD_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif"
MD_PC_TC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_TC.tif"
# TC_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 3")
# TC_Con.save(MD_PC_TC_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC TC Raster')
#Create MD Wetland Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC Wet Raster (6 minutes)')
MD_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif"
MD_PC_Wet_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_Wet.tif"
# Wet_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 2")
# Wet_Con.save(MD_PC_Wet_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC Wet Raster')
#Create MD Scrub\Shrub Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC SS Raster (7 minutes)')
MD_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif"
MD_PC_SS_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_SS.tif"
# SS_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 4")
# SS_Con.save(MD_PC_SS_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC SS Raster')
#Create MD Low Vegetation Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC LV Raster (7 minutes)')
MD_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif"
MD_PC_LV_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LV.tif"
# LV_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 5")
# LV_Con.save(MD_PC_LV_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC LV Raster')
#Create MD Water Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD PC Wat Raster (7 minutes)')
MD_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_LC.tif"
MD_PC_Wat_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_PC_Wat.tif"
# Wat_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 1")
# Wat_Con.save(MD_PC_Wat_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD PC Wat Raster')
#Create UID for MD Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Create UID (11 seconds)') 
# arcpy.AddField_management(MD_Priority_Parcels, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(MD_Priority_Parcels, ["FID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Created UID')
# Zonal Statistics as Table on MD Tree Canopy Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Tree Canopy within Priority Parcels (6 minutes)')
MD_TC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_TC_ZS.dbf"
# MD_TC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_PC_TC_Raster, MD_TC_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_TC_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(MD_Priority_Parcels, "LC_TC", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_TC", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_TC", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Tree Canopy within Priority Parcels')
# Zonal Statistics as Table on MD Wetland Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Wetland within Priority Parcels (7 minutes)')
MD_Wet_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_Wet_ZS.dbf"
# MD_Wet_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_PC_Wet_Raster, MD_Wet_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Wet_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(MD_Priority_Parcels, "LC_Wet", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_Wet", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_Wet", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Wetland within Priority Parcels')
# Zonal Statistics as Table on MD Scrub\Shrub Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Scrub\Shrub within Priority Parcels (6 minutes)')
MD_SS_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_SS_ZS.dbf"
# MD_SS_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_PC_SS_Raster, MD_SS_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_SS_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(MD_Priority_Parcels, "LC_SS", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_SS", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_SS", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Scrub\Shrub within Priority Parcels')
# Zonal Statistics as Table on MD Low Vegetation Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Low Vegetation within Priority Parcels (7 minutes)')
MD_LV_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_LV_ZS.dbf"
# MD_LV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_PC_LV_Raster, MD_LV_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_LV_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(MD_Priority_Parcels, "LC_LV", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_LV", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_LV", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Low Vegetation within Priority Parcels')
# Zonal Statistics as Table on MD Water Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Water within Priority Parcels (7 minutes)')
MD_Wat_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\MD_Wat_ZS.dbf"
# MD_Wat_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_PC_Wat_Raster, MD_Wat_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Wat_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(MD_Priority_Parcels, "LC_Wat", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_Wat", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "LC_Wat", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Water within Priority Parcels')
#Select Priority Parcels that have National Historic Landmarks
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Historic Landmarks (1 second)')
# National_Historic_Landmark_selection = arcpy.SelectLayerByLocation_management(MD_Priority_Parcels, 'INTERSECT', National_Historic_Landmarks_Projected)
MD_NHL_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\MD_NHL_Parcels.shp"
# arcpy.CopyFeatures_management(National_Historic_Landmark_selection, MD_NHL_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Historic Landmarks')
#Create NHL Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NHL Field ( second)')
# NHL_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_NHL_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NHL_Parcels_selection, "NHL", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NHL Field')
#Select Priority Parcels that have National Register of Historic Sites and Places (NRHP)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Register of Historic Sites and Places (NRHP) (1 second)')
# NRHP_selection = arcpy.SelectLayerByLocation_management(MD_Priority_Parcels, 'INTERSECT', NRHP_Projected)
MD_NRHP_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\MD_NRHP_Parcels.shp"
# arcpy.CopyFeatures_management(NRHP_selection, MD_NRHP_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Register of Historic Sites and Places')
#Create NRHP Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NRHP Field ( second)')
# NRHP_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_NRHP_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NRHP_Parcels_selection, "NRHP", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NRHP Field')
#Create Historic Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Historic Field ( second)')
# arcpy.management.CalculateField(MD_Priority_Parcels, "H_SUM", "!NHL! + !NRHP!", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(MD_Priority_Parcels, "Historic", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Historic", "!H_SUM! > 0", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["H_SUM"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["NHL"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["NRHP"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Historic Field ( second)')
# Zonal Statistics as Table on CBP WQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of CBP WQ within Priority Parcels ( minutes)')
# MD_WQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\MD_WQ_ZS.dbf"
# MD_WQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", WQ_Raster_Projected, MD_WQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_WQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(MD_Priority_Parcels, "WQP_Val", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP_Val", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(MD_Priority_Parcels, "WQP1", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP1", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP1", "!WQP_Val! >= 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQP2", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP2", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP2", "!WQP_Val! > 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQP3", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP3", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP3", "!WQP_Val! > 30", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQP4", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP4", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP4", "!WQP_Val! > 38", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQP5", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP5", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQP5", "!WQP_Val! > 48", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "CBP_WQP", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "CBP_WQP", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "CBP_WQP", "!WQP1! + !WQP2! + !WQP3! + !WQP4! + !WQP5!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQP1"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQP2"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQP3"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQP4"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQP5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of CBP WQ within Priority Parcels')
# Zonal Statistics as Table on TNC Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of TNC within Priority Parcels ( minutes)')
MD_TNC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\MD_TNC_ZS.dbf"
# MD_TNC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", TNC_Raster_Projected, MD_TNC_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_TNC_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(MD_Priority_Parcels, "TNC", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "TNC", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "TNC", "!MAJORITY! > 0", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of TNC within Priority Parcels')
# Zonal Statistics as Table on DWQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of DWQ within Priority Parcels ( minutes)')
MD_DWQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\MD_DWQ_ZS.dbf"
# MD_DWQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", DWQ_Raster_Projected, MD_DWQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_DWQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(MD_Priority_Parcels, "ICPRB_Val", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "ICPRB_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "ICPRB_Val", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(MD_Priority_Parcels, "WQ_30", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_30", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_30", "!ICPRB_Val! > 30", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQ_45", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_45", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_45", "!ICPRB_Val! > 45", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQ_60", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_60", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_60", "!ICPRB_Val! > 60", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQ_75", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_75", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_75", "!ICPRB_Val! > 75", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "WQ_Sum", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_Sum", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "WQ_Sum", "!WQ_30! + !WQ_45! + !WQ_60! + !WQ_75!", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "ICPRB_WQ", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "ICPRB_WQ", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "ICPRB_WQ", "!WQ_Sum! + 1", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQ_30"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQ_45"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQ_60"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQ_75"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["WQ_Sum"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of DWQ within Priority Parcels')
# Zonal Statistics as Table on MD Develompment Vulnerabilty Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of MD Develompment Vulnerabilty within Priority Parcels ( minutes)')
MD_DevV_2025_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\MD_DevV_2025_ZS.dbf"
# MD_DevV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_Priority_Parcels, "UID", MD_DevV_2025_Raster_Projected, MD_DevV_2025_ZS_Table, "DATA", "MAXIMUM")
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_DevV_2025_ZS_Table, "UID",["MAX"])
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_Val", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_Val", "!MAX!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["MAX"])
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_1", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_1", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_1", "!DevV_Val! > -1", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_2", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_2", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_2", "!DevV_Val! > 1", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_3", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_3", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_3", "!DevV_Val! > 2", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_4", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_4", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_4", "!DevV_Val! > 3", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "DevV_5", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_5", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV_5", "!DevV_Val! > 5", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "DevV", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "DevV", "!DevV_1! + !DevV_2! + !DevV_3! + !DevV_4! + !DevV_5!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["DevV_1"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["DevV_2"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["DevV_3"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["DevV_4"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["DevV_5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of MD Develompment Vulnerabilty within Priority Parcels')
#Select MD Priority Parcels Intersecting Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels Intersecting Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
MD_Parcels_Int_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\MD_Parcels_Int_PADUS.shp"
# MD_Parcels_Int_PADUS_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "INTERSECT", PADUS_Bay, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_Int_PADUS_Selection, MD_Parcels_Int_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels Intersecting Protected Areas')
#Select MD Priority Parcels .25 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels .25 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
MD_Parcels_QM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\MD_Parcels_QM_PADUS.shp"
# MD_Parcels_QM_PADUS_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_QM_PADUS_Selection, MD_Parcels_QM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels .25 mile from Protected Areas')
#Select MD Priority Parcels .5 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels .5 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
MD_Parcels_HM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\MD_Parcels_HM_PADUS.shp"
# MD_Parcels_HM_PADUS_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_HM_PADUS_Selection, MD_Parcels_HM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels .5 mile from Protected Areas')
#Select MD Priority Parcels 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
MD_Parcels_1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\MD_Parcels_1M_PADUS.shp"
# MD_Parcels_1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_1M_PADUS_Selection, MD_Parcels_1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels 1 mile from Protected Areas')
# #Select MD Priority Parcels Greater than 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels Greater Than 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
MD_Parcels_GreaterThan1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\MD_Parcels_GreaterThan1M_PADUS.shp"
# MD_Parcels_GreaterThan1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_GreaterThan1M_PADUS_Selection, MD_Parcels_GreaterThan1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels Greater Than 1 mile from Protected Areas')
#Create Adjacency to federal/state protected lands (Adj_PL) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Adjacency to federal/state protected lands (Adj_PL) Field ( second)')
# MD_Int_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_Int_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_Int_PADUS_Parcels_selection, "PL_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_QM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_QM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_QM_PADUS_Parcels_selection, "PL_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_HM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_HM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_HM_PADUS_Parcels_selection, "PL_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_1M_PADUS_Parcels_selection, "PL_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_GreaterThan1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_GreaterThan1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_GreaterThan1M_PADUS_Parcels_selection, "PL_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(MD_Priority_Parcels, "Adj_PL", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Adj_PL", "max([!PL_Int!, !PL_QM!, !PL_HM!,!PL_1M!,!PL_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PL_Int"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PL_QM"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PL_HM"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PL_1M"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PL_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Adjacency to federal/state protected lands (Adj_PL) Field')
#Select MD Priority Parcels Intersecting Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels Intersecting Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
MD_Parcels_Int_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\MD_Parcels_Int_Trails.shp"
# MD_Parcels_Int_Trails_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "INTERSECT", Baywide_Trails_Projected, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_Int_Trails_Selection, MD_Parcels_Int_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels Intersecting Trails')
#Select MD Priority Parcels .25 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels .25 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
MD_Parcels_QM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\MD_Parcels_QM_Trails.shp"
# MD_Parcels_QM_Trails_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_QM_Trails_Selection, MD_Parcels_QM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels .25 mile from Trails')
#Select MD Priority Parcels .5 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels .5 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
MD_Parcels_HM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\MD_Parcels_HM_Trails.shp"
# MD_Parcels_HM_Trails_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_HM_Trails_Selection, MD_Parcels_HM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels .5 mile from Trails')
#Select MD Priority Parcels 1 Miles from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
MD_Parcels_1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\MD_Parcels_1M_Trails.shp"
# MD_Parcels_1M_Trails_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_1M_Trails_Selection, MD_Parcels_1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels 1 mile from Trails')
#Select MD Priority Parcels Greater than 1 Mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select MD Priority Parcels Greater Than 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
MD_Parcels_GreaterThan1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\MD_Parcels_GreaterThan1M_Trails.shp"
# MD_Parcels_GreaterThan1M_Trails_Selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(MD_Parcels_GreaterThan1M_Trails_Selection, MD_Parcels_GreaterThan1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting MD Priority Parcels Greater Than 1 mile from Trails')
#Create Trail network expansion (Trail_exp) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Trail network expansion (Trail_exp) Field ( second)')
# MD_Int_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_Int_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_Int_Trails_Parcels_selection, "T_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_QM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_QM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_QM_Trails_Parcels_selection, "T_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_HM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_HM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_HM_Trails_Parcels_selection, "T_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_1M_Trails_Parcels_selection, "T_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# MD_GreaterThan1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(MD_Priority_Parcels, "ARE_IDENTICAL_TO", MD_Parcels_GreaterThan1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(MD_GreaterThan1M_Trails_Parcels_selection, "T_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(MD_Priority_Parcels, "Adj_T", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Adj_T", "max([!T_Int!, !T_QM!, !T_HM!,!T_1M!,!T_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["T_Int"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["T_QM"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["T_HM"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["T_1M"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["T_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Trail network expansion (Trail_exp) Field ')
#Convert MD SVI Desired Counties table to CSV
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Convert MD SVI Desired Counties table to CSV')
MD_SVI_Desired_Counties_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_SVI_Desired_Counties.dbf"
# arcpy.TableToTable_conversion(MD_SVI_Desired_Counties_Table, r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion", "MD_SVI_Desired_Counties.csv")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Converted MD SVI Desired Counties table to CSV')
#Create dictionary of MD SVI Desired Counties with County and RPL Themes
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create dictionary of MD SVI Desired Counties with County and RPL Themes')
# MD_SVI_County_dict = {'Allegany':'ALLE',
#                       'Frederick':'FRED',
#                       'Garrett':'GARR',
#                       'Washington':'WASH'
#     }
# def SVI_Rank_Func(row):
#     if row['RPL_THEMES'] <= 0:
#         val = 1
#     elif row['RPL_THEMES'] <= .25:
#         val = 2
#     elif row['RPL_THEMES'] <= .5:
#         val = 3
#     elif row['RPL_THEMES'] <= .75:
#         val = 4
#     else:
#         val = 5
#     return val
# MD_SVI_Desired_Counties_CSV = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_SVI_Desired_Counties.csv"
# MD_SVI_df = pd.read_csv(MD_SVI_Desired_Counties_CSV)
# MD_SVI_df = MD_SVI_df[['COUNTY','RPL_THEMES']]
# MD_SVI_df['JURSCODE'] = MD_SVI_df['COUNTY'].map(MD_SVI_County_dict)
# MD_SVI_df['SVI'] = MD_SVI_df.apply(SVI_Rank_Func, axis=1)
# MD_SVI_dict = MD_SVI_df.set_index('JURSCODE').to_dict()['SVI']
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created dictionary of MD SVI Desired Counties with County and RPL Themes')
# Create a EI Field and use dictionary to update the field with proper value
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create a SVI Field and use dictionary to update the field with proper value')
# arcpy.CalculateField_management(MD_Priority_Parcels, "SVI", "0", "PYTHON3")
# with arcpy.da.UpdateCursor(MD_Priority_Parcels, ['JURSCODE', 'SVI']) as cursor:
#     for row in cursor:
#         county = row[0]
#         if county in MD_SVI_dict:
#             row[1] = MD_SVI_dict[county]
#             cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created a SVI Field and use dictionary to update the field with proper value')
# Summarize Within on US_SVI_MD_Desired_Counties Polygon using Priority Parcels as Zones CANT FIGURE OUT WHY IT BREAKS
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for US_SVI and create SVI_US and SVI_Val field (1 minutes)')
MD_Parcels_SW_SVI = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_Parcels_SW_SVI.shp"
MD_Parcels_SW_SVI_Maj_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\MD_Parcels_SW_SVI_Maj.dbf"
# arcpy.gapro.SummarizeWithin(US_SVI_MD_Desired_Counties, MD_Parcels_SW_SVI, "POLYGON", '', None, MD_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, "Value", "ADD_MIN_MAJ", "NO_PERCENT", MD_Parcels_SW_SVI_Maj_Table)
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Parcels_SW_SVI, "UID",["MAJORITY_V"])
# arcpy.AddField_management(MD_Priority_Parcels, "SVI_US", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SVI_US", "!MAJORITY_V!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["MAJORITY_V"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within MD Priority Parcels for US_SVI and created SVI_US field')
#Create TCWetland Raster and Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Raster and Polygon (15 minutes)' ) 
MD_TCWetland_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_TCWetland.tif"
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams", "MD.gdb")
MD_TCWetland_NonTCWet_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\MD_TCWetland_NonTCWet"
# TCWtland_Con = arcpy.sa.Con(MD_PC_LC_Raster, 1, 0,"VALUE = 3 OR VALUE = 2")
# TCWtland_Con.save(MD_TCWetland_Raster)
# arcpy.RasterToPolygon_conversion(MD_TCWetland_Raster, MD_TCWetland_NonTCWet_Polygon, "NO_SIMPLIFY","VALUE") 
# MD_TCWetland_Selection = arcpy.management.SelectLayerByAttribute(MD_TCWetland_NonTCWet_Polygon, "NEW_SELECTION", "gridcode = 1")
MD_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\MD_TCWetland"
# arcpy.CopyFeatures_management(MD_TCWetland_Selection, MD_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Raster and Polygon' )
# Eliminate totally included areas on TCWetland Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminate totally included areas on MD TCWetland Polygons (1 minute)')
MD_TCWetland_Eliminated_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\MD_TCWetland_Eliminated"
# arcpy.EliminatePolygonPart_management(MD_TCWetland_Polygon, MD_TCWetland_Eliminated_Polygon, "AREA", 100000, "", "CONTAINED_ONLY")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminated totally included areas on MD TCWetland Polygons')
# Create TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Polygon (15 minutes)')
MD_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\MD_TCWetland_Holes"
# arcpy.SymDiff_analysis(MD_TCWetland_Eliminated_Polygon, MD_TCWetland_Polygon, MD_TCWetland_Holes_Polygon, "ALL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Polygon')
# Create TCWetland Holes Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Singlepart Polygon (1 minutes)')
MD_TCWetland_Holes_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\MD_TCWetland_Holes_Singlepart"
# arcpy.MultipartToSinglepart_management(MD_TCWetland_Holes_Polygon, MD_TCWetland_Holes_Singlepart_Polygon)
# arcpy.AddField_management(MD_TCWetland_Holes_Singlepart_Polygon, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(MD_TCWetland_Holes_Singlepart_Polygon, ["OBJECTID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Singlepart Polygon')
# Zonal Statistics as Table on MD Water LC Raster using TCWetland Holes Singlepart Polygon as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to determine Water/Non-Water Forest holes (1 hr 33 minutes)')
TCWetland_Hole_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\TCWetland_Hole_ZS.dbf"
# TCWetlandHoleZSaT = arcpy.sa.ZonalStatisticsAsTable(MD_TCWetland_Holes_Singlepart_Polygon, "UID", MD_PC_Wat_Raster, TCWetland_Hole_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(MD_TCWetland_Holes_Singlepart_Polygon, "UID", TCWetland_Hole_ZS_Table, "UID",["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to determine Water/Non-Water Forest holes')
# Create Natural TCWetland Holes Polygon by selecting forest holes with a majority of Natural LU/TC in AG
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Natural Forest Holes Polygon (20 second)' ) 
Natural_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\Natural_TCWetland_Holes"
# Natural_TCWetland_Holes_Selection = arcpy.SelectLayerByAttribute_management(MD_TCWetland_Holes_Singlepart_Polygon, "NEW_SELECTION", "MAJORITY = 1")
# arcpy.CopyFeatures_management(Natural_TCWetland_Holes_Selection, Natural_TCWetland_Holes_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Natural TCWetland Holes Polygon')
#Merge MD TCWetland Polygon and Natural TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge TCWetland Polygons (1 minute)')
Merged_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\Merged_TCWetland"
# arcpy.management.Merge([MD_TCWetland_Polygon,Natural_TCWetland_Holes_Polygon], Merged_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
# Create Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Merged TCWetland Single Part Polygon (1 minutes)')
Merged_TCWetland_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\Merged_TCWetland_Singlepart"
# arcpy.MultipartToSinglepart_management(Merged_TCWetland_Polygon, Merged_TCWetland_Singlepart_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Merged TCWetland Single Part Polygon')
#Create Filled TCWetland Polygon by dissolving Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Filled TCWetland Polygon (10 minutes)')
Filled_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD.gdb\Filled_TCWetland"
# arcpy.PairwiseDissolve_analysis(Merged_TCWetland_Singlepart_Polygon, Filled_TCWetland_Polygon, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled TCWetland Polygon')
#Clip StreamRivers to Filled TC Wetland
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create MD StreamRivers Clipped (10 minutes)')
MD_StreamRivers_Clipped = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Clipped.shp"
# arcpy.PairwiseClip_analysis(StreamRivers,Filled_TCWetland_Polygon,MD_StreamRivers_Clipped)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD StreamRivers Clipped (10 minutes)')
# Create MD StreamRivers Clipped Singlepart Line
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create  MD StreamRivers Clipped Singlepart (1 minutes)')
MD_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Clipped_Singlepart.shp"
# arcpy.MultipartToSinglepart_management(MD_StreamRivers_Clipped, MD_StreamRiver_Clipped_Singlepart)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD StreamRivers Clipped Singlepart')
#Buffer StreamRivers by 100 Feet
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffering MD StreamRivers Clipped Singlepart by 100 feet ( seconds)')
MD_StreamRiver_Buffer_PreClip = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Buffer_PreClip.shp"
# arcpy.analysis.PairwiseBuffer(MD_StreamRiver_Clipped_Singlepart, MD_StreamRiver_Buffer_PreClip, "100 Feet")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffered MD StreamRivers Clipped Singlepart by 100 feet')
# Create MD StreamRivers Buffers
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create  MD StreamRivers Clipped Singlepart (1 minutes)')
MD_StreamRiver_Buffer = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Buffer.shp"
# arcpy.PairwiseClip_analysis(StreamRiver_Buffer,Filled_TCWetland_Polygon,MD_StreamRiver_Buffer)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD StreamRivers Clipped Singlepart')
# Create MD StreamRivers Buffer Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create  MD StreamRivers Buffer Singlepart (1 minutes)')
MD_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Buffer_Singlepart.shp"
# arcpy.MultipartToSinglepart_management(MD_StreamRiver_Buffer, MD_StreamRiver_Buffer_Singlepart)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD StreamRivers Buffer Singlepart')
# Summarize Within MD Priority Parcels for Streams
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for Streams (1 minutes)')
MD_Parcels_SW_Streams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_Parcels_SW_Streams.shp"
# arcpy.gapro.SummarizeWithin(StreamRivers, MD_Parcels_SW_Streams, "POLYGON", '', None, MD_Priority_Parcels, "ADD_SUMMARY", "MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for Buffered Stream Area (1 minutes)')
# Summarize Within MD Priority Parcels for Buffered Streams
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for Buffered Streams (1 minutes)')
MD_Parcels_SW_BuffStreams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_Parcels_SW_BuffStreams.shp"
# arcpy.gapro.SummarizeWithin(MD_StreamRiver_Buffer_Singlepart, MD_Parcels_SW_BuffStreams, "POLYGON", '', None, MD_Priority_Parcels, "ADD_SUMMARY", "SQUARE_MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for Streams (1 minutes)')
#Join Stream Mile and Buffered Stream Area field back to MD Priority Parcels and Create Stream Buffer Ratio
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Stream Mile and Buffered Stream Area field back to MD Priority Parcels (1 minutes)')
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Parcels_SW_Streams, "UID",["sum_length"])
# arcpy.AddField_management(MD_Priority_Parcels, "Stream_M", "FLOAT")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Stream_M", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Stream_M", "!sum_length!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["sum_length"])
# arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Parcels_SW_BuffStreams, "UID",["sum_area_s"])
# arcpy.AddField_management(MD_Priority_Parcels, "BuffS_Area", "FLOAT")
# arcpy.CalculateField_management(MD_Priority_Parcels, "BuffS_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "BuffS_Area", "!sum_area_s!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["sum_area_s"])
# arcpy.AddField_management(MD_Priority_Parcels, "SB_Ratio", "FLOAT")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB_Ratio", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB_Ratio", "(!BuffS_Area! * !Stream_M!) / 0.038", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Stream Mile and Buffered Stream Area field back to MD Priority Parcels')
#Create SB attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Stream Buffer attribute (1 minutes)')
# arcpy.AddField_management(MD_Priority_Parcels, "SB1", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB1", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB1", "!SB_Ratio! >= 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "SB2", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB2", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB2", "!SB_Ratio! > 0.010495", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "SB3", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB3", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB3", "!SB_Ratio! > 0.048996", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "SB4", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB4", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB4", "!SB_Ratio! > 0.127791", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "SB5", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB5", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB5", "!SB_Ratio! > 0.347993", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "SB", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "SB", "!SB1! + !SB2! + !SB3! + !SB4! + !SB5!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["SB1"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["SB2"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["SB3"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["SB4"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["SB5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Stream Buffer attribute')
#Create Parcel Size attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Parcel Size attribute (1 minutes)')
# arcpy.AddField_management(MD_Priority_Parcels, "PS1", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS1", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS1", "!Acreage! >= 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "PS2", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS2", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS2", "!Acreage! >= 75", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "PS3", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS3", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS3", "!Acreage! >= 100", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "PS4", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS4", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS4", "!Acreage! >= 125", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "PS5", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS5", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS5", "!Acreage! > 150", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "PS", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "PS", "!PS1! + !PS2! + !PS3! + !PS4! + !PS5!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PS1"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PS2"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PS3"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PS4"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["PS5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Parcel Size attribute (1 minutes)')
# Summarize Within MD Priority Parcels for Forest Hubs (No Wetland Hubs in MD study area could be different in VA)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within MD Priority Parcels for Hubs (1 minutes)')
MD_Forest_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\Forest_Hubs.shp"
MD_Parcels_SW_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\MD_Parcels_SW_Hubs.shp"
# arcpy.gapro.SummarizeWithin(MD_Forest_Hubs, MD_Parcels_SW_Hubs, "POLYGON", '', None, MD_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within MD Priority Parcels for Hubs')
#Join Stream Mile and Buffered Stream Area field back to MD Priority Parcels and Create Stream Buffer Ratio
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Hub Area field back to MD Priority Parcels (1 minutes)')
# # arcpy.JoinField_management(MD_Priority_Parcels, "UID", MD_Parcels_SW_Hubs, "UID",["sum_area_a"])
# arcpy.AddField_management(MD_Priority_Parcels, "Hub_Area", "FLOAT")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub_Area", "!sum_area_a!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["sum_area_a"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Hub Area field back to MD Priority Parcels')
#Create Hub attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Hub attribute (1 minutes)')
# arcpy.AddField_management(MD_Priority_Parcels, "Hub1", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub1", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub1", "!Hub_Area! >= 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "Hub2", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub2", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub2", "!Hub_Area! > 0", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "Hub3", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub3", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub3", "!Hub_Area! > 10", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "Hub4", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub4", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub4", "!Hub_Area! > 30", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "Hub5", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub5", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub5", "!Hub_Area! > 50", "PYTHON3")
# arcpy.AddField_management(MD_Priority_Parcels, "Hub", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub", "0", "PYTHON3")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Hub", "!Hub1! + !Hub2! + !Hub3! + !Hub4! + !Hub5!", "PYTHON3")
# arcpy.DeleteField_management(MD_Priority_Parcels, ["Hub1"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["Hub2"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["Hub3"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["Hub4"])
# arcpy.DeleteField_management(MD_Priority_Parcels, ["Hub5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Hub attribute')
#Create Priority Attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Priority attribute (1 minutes)')
# arcpy.AddField_management(MD_Priority_Parcels, "Score", "LONG")
# arcpy.CalculateField_management(MD_Priority_Parcels, "Score", "(!TNC! * 5) + !Hub! + !CBP_WQP! + !ICPRB_WQ! + !DevV! + !SB! + !Adj_PL! + !Adj_T! + (!Historic! * 5) + !PS! + !SVI_US!", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Priority attribute (1 minutes)')




#VIRGINIA/WEST VIRGINIA FOREST HUBS
vawv_cflist = [
    'augu_51015',
    'clar_51043',
    'fred_51069',
    'high_51091',
    'loud_51107',
    'page_51139',
    'rock_51165',
    'shen_51171',
    'warr_51187',
    'berk_54003',
    'gran_54023',
    'hamp_54027',
    'hard_54031',
    'jeff_54037',
    'mine_54057',
    'morg_54065',
    'pend_54071',
    ]
#Create List of MD LU rasters
VA_LU_Raster_List = []
WV_LU_Raster_List = []
for cf in vawv_cflist:
    print('############################')
    print('####### {} #########'.format(cf))
    print('############################')
    statenum = cf[5]+cf[6]
    state_cf_dict = {
            '36' :'NY',
            '42' : 'PA',
            '11' : 'DC',
            '10' : 'DE',
            '24' : 'MD',
            '54' : 'WV',
            '51' : 'VA',
            '20' : 'PA'
            }
    state = state_cf_dict[statenum]
    if state == 'NY':
        oldyear = '2013'
        newyear = '2017'
    if state == 'PA':
        oldyear = '2013'
        newyear = '2017'
    if state == 'DC':
        oldyear = '2013'
        newyear = '2017'
    if state == 'DE':
        oldyear = '2013'
        newyear = '2018'
    if state == 'MD':
        oldyear = '2013'
        newyear = '2018'
    if state == 'WV':
        oldyear = '2014'
        newyear = '2018'
        cf_LU_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LU\{}_lu_2017_2018.tif".format(cf)
        WV_LU_Raster_List.append(cf_LU_Raster)
    if state == 'VA':
        oldyear = '2014'
        newyear = '2018'
        cf_LU_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LU\{}_lu_2017_2018.tif".format(cf)
        VA_LU_Raster_List.append(cf_LU_Raster)
#Mosaic LU Rasters
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC LU Raster (1 Hour 52 minutes)')
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU", "VAWV_PC_LU.gdb")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb","VA_PC_LU_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\VA_PC_LU_mosaic","Raster Dataset",VA_LU_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\VA_PC_LU_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VA_PC_LU.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb","WV_PC_LU_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\WV_PC_LU_mosaic","Raster Dataset",WV_LU_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\WV_PC_LU_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\WV_PC_LU.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb","VAWV_PC_LU_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\VAWV_PC_LU_mosaic","Raster Dataset",[r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VA_PC_LU.tif",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\WV_PC_LU.tif"],"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.gdb\VAWV_PC_LU_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LU\VAWV_PC_LU.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC LU Raster')
#Create List of VAWV LC rasters
VA_LC_Raster_List = []
WV_LC_Raster_List = []
for cf in vawv_cflist:
    print('############################')
    print('####### {} #########'.format(cf))
    print('############################')
    statenum = cf[5]+cf[6]
    state_cf_dict = {
            '36' :'NY',
            '42' : 'PA',
            '11' : 'DC',
            '10' : 'DE',
            '24' : 'MD',
            '54' : 'WV',
            '51' : 'VA',
            '20' : 'PA'
            }
    state = state_cf_dict[statenum]
    if state == 'NY':
        oldyear = '2013'
        newyear = '2017'
    if state == 'PA':
        oldyear = '2013'
        newyear = '2017'
    if state == 'DC':
        oldyear = '2013'
        newyear = '2017'
    if state == 'DE':
        oldyear = '2013'
        newyear = '2018'
    if state == 'MD':
        oldyear = '2013'
        newyear = '2018'
    if state == 'WV':
        oldyear = '2014'
        newyear = '2018'
        cf_LC_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LC\{}_landcover_2018_June2021.tif".format(cf)
        WV_LC_Raster_List.append(cf_LC_Raster)
    if state == 'VA':
        oldyear = '2014'
        newyear = '2018'
        cf_LC_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LC\{}_landcover_2018_June2021.tif".format(cf)
        VA_LC_Raster_List.append(cf_LC_Raster)
#Mosaic LC Rasters
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC LC Raster (12 minutes)')
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC", "VAWV_PC_LC.gdb")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb","VA_PC_LC_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "8_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\VA_PC_LC_mosaic","Raster Dataset",VA_LC_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\VA_PC_LC_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_PC_LC.tif","",255,255,"NONE","NONE","8_BIT_UNSIGNED")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb","WV_PC_LC_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "8_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\WV_PC_LC_mosaic","Raster Dataset",WV_LC_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\WV_PC_LC_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_PC_LC.tif","",255,255,"NONE","NONE","8_BIT_UNSIGNED")
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb","VAWV_PC_LC_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "8_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\VAWV_PC_LC_mosaic","Raster Dataset",[r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_PC_LC.tif",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_PC_LC.tif"],"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.gdb\VAWV_PC_LC_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif","",255,255,"NONE","NONE","8_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC LC Raster')
#Create VAWV Tree Canopy Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC TC Raster (7 minutes)')
VAWV_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif"
VAWV_PC_TC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_TC.tif"
# TC_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, 0,"VALUE = 3")
# TC_Con.save(VAWV_PC_TC_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC TC Raster')
#Create VAWV Wetland Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC Wet Raster (6 minutes)')
VAWV_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif"
VAWV_PC_Wet_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_Wet.tif"
# Wet_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, 0,"VALUE = 2")
# Wet_Con.save(VAWV_PC_Wet_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC Wet Raster')
#Create VAWV Scrub\Shrub Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC SS Raster (7 minutes)')
VAWV_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif"
VAWV_PC_SS_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_SS.tif"
# SS_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, 0,"VALUE = 4")
# SS_Con.save(VAWV_PC_SS_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC SS Raster')
#Create VAWV Low Vegetation Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC LV Raster (7 minutes)')
VAWV_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif"
VAWV_PC_LV_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LV.tif"
# LV_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, 0,"VALUE = 5")
# LV_Con.save(VAWV_PC_LV_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC LV Raster')
#Create VAWV Water Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV PC Wat Raster (7 minutes)')
VAWV_PC_LC_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_LC.tif"
VAWV_PC_Wat_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VAWV_PC_Wat.tif"
# Wat_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, 0,"VALUE = 1")
# Wat_Con.save(VAWV_PC_Wat_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV PC Wat Raster')
#INTERIOR FOREST
Forest_Polygon_List = []
Forest_Raster_List = []
Nat_LU_TCAg_Polygon_List = []
for cf in vawv_cflist:
    # print('############################')
    # print('####### {} #########'.format(cf))
    # print('############################')
    # Reclass LU to Forest (1) and Non-Forest (0) (2 Hrs 34 minutes for all counties)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Reclassifying LU to Forest and Non-Forest')
    cf_LU_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LU\{}_lu_2017_2018.tif".format(cf)
    cf_Forest_NonForest_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_Forest_NF.tif".format(cf)
    # whereClause = "VALUE = 3 OR VALUE= 3100 OR VALUE = 5104 OR VALUE = 5105 OR VALUE = 5204 OR VALUE= 5205 OR VALUE = 5304 OR VALUE= 5305"
    # Forest_NonForest_Con = arcpy.sa.Con(cf_LU_Raster,1,0,whereClause)
    # Forest_NonForest_Con.save(cf_Forest_NonForest_Raster)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Reclassifying LU to Forest and Non-Forest')
    #Convert Forest/Non-Forest Rasters to Polygons
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Forest/Non-Forest Polygon')
    cf_Forest_NonForest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_Forest_NonForest.shp".format(cf)
    # arcpy.RasterToPolygon_conversion(cf_Forest_NonForest_Raster, cf_Forest_NonForest_Polygon, "NO_SIMPLIFY","VALUE")
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Forest/Non-Forest Polygon')
    #Select Forest and save it
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Forest Polygon')
    # cf_Forest_Selection = arcpy.SelectLayerByAttribute_management(cf_Forest_NonForest_Polygon, "NEW_SELECTION", "gridcode = 1")
    cf_Forest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_Forest.shp".format(cf)
    # arcpy.CopyFeatures_management(cf_Forest_Selection, cf_Forest_Polygon)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Forest Polygon')
    Forest_Polygon_List.append(cf_Forest_Polygon)
    #Create Forest Raster
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Forest Raster ( minutes)')
    cf_Forest_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_F.tif".format(cf)
    # arcpy.PolygonToRaster_conversion(cf_Forest_Polygon, "gridcode", cf_Forest_Raster, "CELL_CENTER", "", 1)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Forest Raster')
    Forest_Raster_List.append(cf_Forest_Raster)
    # Reclass LU to Natural LU and TC in Ag (1) and Non-Natural (2)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Create Natural LU TC in Ag Raster')
    cf_LU_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LU\{}_lu_2017_2018.tif".format(cf)
    cf_Nat_LU_TCAg_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_NatLUTCAg.tif".format(cf)
    # whereClause = "VALUE = 2 OR VALUE = 5000 OR VALUE = 5101 OR VALUE = 5102 OR VALUE = 5103 OR VALUE = 5201 OR VALUE = 5202 OR VALUE = 5203 OR VALUE = 5301 OR VALUE = 5302 OR VALUE= 5303 OR VALUE = 5104 OR VALUE = 5105 OR VALUE = 5204 OR VALUE = 5205 OR VALUE = 5304 OR VALUE = 5305 OR VALUE = 1 OR VALUE = 1000 OR VALUE = 1120 OR VALUE = 3 OR VALUE= 3100 OR VALUE = 4 OR VALUE = 5 OR VALUE = 6 OR VALUE = 3410 OR VALUE = 3420 OR VALUE = 3430 OR VALUE = 5400 OR VALUE = 3200"
    # cf_Natural_LU_TCAg_Con = arcpy.sa.Con(cf_LU_Raster,1,2,whereClause)
    # cf_Natural_LU_TCAg_Con.save(cf_Nat_LU_TCAg_Raster)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Natural LU TC in Ag Raster')
    #Convert Natural LU TC in Ag Raster to Polygon
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Natural LU TC in Ag Polygon')
    cf_Nat_LU_TCAg_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_NatLUTCAg.shp".format(cf)
    # arcpy.RasterToPolygon_conversion(cf_Nat_LU_TCAg_Raster, cf_Nat_LU_TCAg_Polygon, "NO_SIMPLIFY","VALUE")
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Natural LU TC in Ag Polygon')
    Nat_LU_TCAg_Polygon_List.append(cf_Nat_LU_TCAg_Polygon)
#Merge Forest Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge Forest Polygons (1 minute)')
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest", "IntFor.gdb")
No_Dissolve_Forest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\No_Dissolve_Forest"
# arcpy.management.Merge(Forest_Polygon_List, No_Dissolve_Forest_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
#Create VAWV Forest Polygon by dissolving  No Dissolve Forest Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VAWV Forest Polygon (11 minutes)')
VAWV_Forest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\VAWV_Forest"
# arcpy.PairwiseDissolve_analysis(No_Dissolve_Forest_Polygon, VAWV_Forest_Polygon, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV Forest Polygon')
#Merge Natural LU TC in Ag Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge Natural LU TC in Ag Polygons (2 minute)')
VAWV_Nat_LU_TCAg_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\VAWV_Nat_LU_TCAg"
# arcpy.management.Merge(Nat_LU_TCAg_Polygon_List, VAWV_Nat_LU_TCAg_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Natural LU TC in Ag Polygons')
# Convert Natural LU TC in Ag Polygon to Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating VAWV Natural LU TC in Ag Raster (3 Hours 42 minutes)')
VAWV_Nat_LU_TCAg_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\VAWV_NatLUTCAg.tif"
# arcpy.PolygonToRaster_conversion(VAWV_Nat_LU_TCAg_Polygon, "gridcode", VAWV_Nat_LU_TCAg_Raster, "CELL_CENTER", "", 1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV Natural LU TC in Ag Raster')
# Eliminate totally included areas on VAWV Forest Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminate totally included areas on VAWV Forest Polygons (1 minute)')
VAWV_Forest_Eliminated_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\VAWV_Forest_Eliminated"
# arcpy.EliminatePolygonPart_management(VAWV_Forest_Polygon, VAWV_Forest_Eliminated_Polygon, "AREA", 100000, "", "CONTAINED_ONLY")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminated totally included areas on VAWV Forest Polygons')
# Create Forest Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Forest Holes Polygon (15 minutes)')
VAWV_Forest_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\VAWV_Forest_Holes"
# arcpy.SymDiff_analysis(VAWV_Forest_Eliminated_Polygon, VAWV_Forest_Polygon, VAWV_Forest_Holes_Polygon, "ALL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Forest Holes Polygon')
# Create Forest Holes Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Forest Holes Singlepart Polygon (1 minutes)')
VAWV_Forest_Holes_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\VAWV_Forest_Holes_Singlepart"
# arcpy.MultipartToSinglepart_management(VAWV_Forest_Holes_Polygon, VAWV_Forest_Holes_Singlepart_Polygon)
# arcpy.AddField_management(VAWV_Forest_Holes_Singlepart_Polygon, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(VAWV_Forest_Holes_Singlepart_Polygon, ["OBJECTID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Forest Holes Singlepart Polygon')
# Zonal Statistics as Table on VAWV Natural LU TC in Ag Raster using Forest Holes Singlepart Polygon as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to determine Natural/Non-Natural Forest holes (1 hr 33 minutes)')
Forest_Hole_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Forest_Hole_ZS.dbf"
# ForestHoleZSaT = arcpy.sa.ZonalStatisticsAsTable(VAWV_Forest_Holes_Singlepart_Polygon, "UID", VAWV_Nat_LU_TCAg_Raster, Forest_Hole_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(VAWV_Forest_Holes_Singlepart_Polygon, "UID", Forest_Hole_ZS_Table, "UID",["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to determine Natural/Non-Natural holes')
# Create Natural Forest Holes Polygon by selecting forest holes with a majority of Natural LU/TC in AG
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Natural Forest Holes Polygon (20 second)' ) 
Natural_Forest_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Natural_Forest_Holes"
# Natural_Forest_Holes_Selection = arcpy.SelectLayerByAttribute_management(VAWV_Forest_Holes_Singlepart_Polygon, "NEW_SELECTION", "MAJORITY = 1")
# arcpy.CopyFeatures_management(Natural_Forest_Holes_Selection, Natural_Forest_Holes_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Natural Forest Holes Polygon')
#Merge VAWV Forest Polygon and Natural Forest Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge Forest Polygons (1 minute)')
Merged_Forest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Merged_Forest"
# arcpy.management.Merge([VAWV_Forest_Polygon,Natural_Forest_Holes_Polygon], Merged_Forest_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
# Create Merged Forest Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Merged Forest Single Part Polygon (1 minutes)')
Merged_Forest_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Merged_Forest_Singlepart"
# arcpy.MultipartToSinglepart_management(Merged_Forest_Polygon, Merged_Forest_Singlepart_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Merged Forest Single Part Polygon')
#Create Filled Forest Polygon by dissolving Merged Forest Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Filled Forest Polygon (10 minutes)')
Filled_Forest_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest"
# arcpy.PairwiseDissolve_analysis(Merged_Forest_Singlepart_Polygon, Filled_Forest_Polygon, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled Forest Polygon')
#Create line of Filled Forest
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Filled Forest Line (33 minutes)')
Filled_Forest_Line = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_Line"
# arcpy.FeatureToLine_management(Filled_Forest_Polygon, Filled_Forest_Line)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled Forest Line')
#Buffer Filled Forest 100 meters 
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffering Filled Forest Line by 100 meters (8 minutes)')
Filled_Forest_Buffer = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_Buffer"
# arcpy.analysis.PairwiseBuffer(Filled_Forest_Line, Filled_Forest_Buffer, "100 Meters")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffered Forest by 100 Meters')
# Convert VAWV Filled Forest Buffer to Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating VAWV Forest Buffer Raster (29 minutes)')
VAWV_Forest_Buffer_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\VAWV_ForBuff.tif"
# arcpy.AddField_management(Filled_Forest_Buffer, "Uni_Value", "LONG")
# arcpy.CalculateField_management(Filled_Forest_Buffer, "Uni_Value", "7", "PYTHON3")
# arcpy.PolygonToRaster_conversion(Filled_Forest_Buffer, "Uni_Value", VAWV_Forest_Buffer_Raster, "CELL_CENTER", "", 1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VAWV Forest Buffer Raster')
# Convert Filled Forest Polygon to Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Filled Forest Raster (17 minutes)')
Filled_Forest_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\FilledForest.tif"
# arcpy.AddField_management(Filled_Forest_Polygon, "Uni_Value", "LONG")
# arcpy.CalculateField_management(Filled_Forest_Polygon, "Uni_Value", "1", "PYTHON3")
# arcpy.PolygonToRaster_conversion(Filled_Forest_Polygon, "Uni_Value", Filled_Forest_Raster, "CELL_CENTER", "", 1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled Forest Raster')
for cf in vawv_cflist:
    # print('############################')
    # print('####### {} #########'.format(cf))
    # print('############################')
    #Create "Blank" Rasters for each county (52 minutes)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Blank County Raster')
    cf_LC_Raster = r"C:\Users\kwalker\Desktop\V1_VAWV_LC\{}_landcover_2018_June2021.tif".format(cf)
    # cf_Blank_Con = arcpy.sa.Con(cf_LC_Raster,0,cf_LC_Raster,"VALUE > 0")
    cf_Blank_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Blank.tif".format(cf)
    # cf_Blank_Con.save(cf_Blank_Raster)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Blank County Raster')
    #Create Filled Forest Raster for each county (35 minutes for all)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Create Filled Forest County Raster')
    cf_Blank_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Blank.tif".format(cf)
    # cf_FF_Calc = arcpy.sa.Raster(Filled_Forest_Raster) + arcpy.sa.Raster(cf_Blank_Raster)
    cf_Filled_Forest_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\{}_FF.tif".format(cf)
    # cf_FF_Calc.save(cf_Filled_Forest_Raster)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Filled Forest County Raster')
#Mosaic Filled Forest Raster and Blank Rasters
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Filled Forest/Non-Forest Raster (2 hr 56 minutes)')
# Forest_Raster_List_1 = [r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\augu_51015_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\clar_51043_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\fred_51069_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\high_51091_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\loud_51107_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\page_51139_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\rock_51165_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\shen_51171_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\warr_51187_FF.tif",
#     ]
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","Filled_Forest_mosaic_1", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_mosaic_1","Raster Dataset",Forest_Raster_List_1,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_mosaic_1",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Filled_Forest_1.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# Forest_Raster_List_2 = [r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\berk_54003_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\gran_54023_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\hamp_54027_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\hard_54031_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\jeff_54037_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\mine_54057_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\morg_54065_FF.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\pend_54071_FF.tif",
#     ]
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","Filled_Forest_mosaic_2", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_mosaic_2","Raster Dataset",Forest_Raster_List_2,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Filled_Forest_mosaic_2",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Filled_Forest_2.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# Blank_Raster_List_1 = [r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\augu_51015_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\clar_51043_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\fred_51069_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\high_51091_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\loud_51107_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\page_51139_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\rock_51165_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\shen_51171_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\warr_51187_Blank.tif",
#     ]
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","Blank_mosaic_1", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Blank_mosaic_1","Raster Dataset",Blank_Raster_List_1,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Blank_mosaic_1",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Blank1.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# Blank_Raster_List_2 = [r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\berk_54003_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\gran_54023_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\hamp_54027_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\hard_54031_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\jeff_54037_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\mine_54057_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\morg_54065_Blank.tif",
#                       r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\pend_54071_Blank.tif",
#     ]
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","Blank_mosaic_2", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Blank_mosaic_2","Raster Dataset",Blank_Raster_List_2,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Blank_mosaic_2",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Blank2.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# Filled_Forest_NF_Raster_List = [r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Filled_Forest_2.tif",
#                                 r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Filled_Forest_1.tif",
#                                 r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Blank2.tif",
#                                 r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Blank1.tif",
                                
#     ]
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","FF_NF_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\FF_NF_mosaic","Raster Dataset",Filled_Forest_NF_Raster_List,"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.SetMosaicDatasetProperties_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\FF_NF_mosaic",allowed_mosaic_methods="None",default_mosaic_method="None")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\FF_NF_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\FillFor_NF.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled Forest/Non-Forest Raster')
#Multiply Filled Forest/Non-Forest Raster with MD Forest Buffer Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Interior Forest Buffer Raster (38 minutes)')
Filled_Forest_NF_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\FillFor_NF.tif"
# Interior_Forest_Buffer_Raster_Calc = arcpy.sa.Raster(Filled_Forest_NF_Raster) *  arcpy.sa.Raster(VAWV_Forest_Buffer_Raster)
Interior_Forest_Buffer_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Interior_Forest_Buffer.tif"
# Interior_Forest_Buffer_Raster_Calc.save(Interior_Forest_Buffer_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Interior Forest Buffer Raster')
#Combine Interior Forest Buffer Raster and Forest/Non-Forest Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Combine Interior Forest Buffer Raster and Filled Forest/Non-Forest Raster (1 Hr 14 minutes)')
Interior_Forest_Buffer_No_Reclass_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Interior_Forest_NoRC.tif"
# arcpy.CreateMosaicDataset_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb","Interior_Forest_NoRC_mosaic", 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "1", "16_BIT_UNSIGNED")
# arcpy.management.AddRastersToMosaicDataset(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Interior_Forest_NoRC_mosaic","Raster Dataset",[Interior_Forest_Buffer_Raster,Filled_Forest_NF_Raster],"UPDATE_CELL_SIZES","UPDATE_BOUNDARY","UPDATE_OVERVIEWS","","","","","","","","BUILD_PYRAMIDS","CALCULATE_STATISTICS","BUILD_THUMBNAILS")
# arcpy.management.CopyRaster(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\IntFor.gdb\Interior_Forest_NoRC_mosaic",r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Interior_Forest_NoRC.tif","",255,255,"NONE","NONE","16_BIT_UNSIGNED")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Combined Interior Forest Buffer Raster and Filled Forest/Non-Forest Raster')
#Create Interior Forest Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Interior Forest Raster (26 minutes)')
Interior_Forest_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Interior_Forest\Interior_Forest.tif"
# Interior_Forest_Raster_Con = arcpy.sa.Con(Interior_Forest_Buffer_No_Reclass_Raster,13, 0,"VALUE = 1")
# Interior_Forest_Raster_Con.save(Interior_Forest_Raster)
# arcpy.management.BuildPyramids(Interior_Forest_Raster,-1,"","","","","")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Interior Forest Raster')
#HUBS
#FOREST
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Region Group Interior Forest (2 hrs 11 minutes)')
# InteriorForestRegionGrp = arcpy.sa.RegionGroup(Interior_Forest_Raster, "FOUR", "WITHIN", "NO_LINK",0)
VAWV_Interior_Forest_RG_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\VAWV_Interior_Forest_RG.tif"
# InteriorForestRegionGrp.save(VAWV_Interior_Forest_RG_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Region Grouped Interior Forest')
#Remove Interior Forest that is less than 10 Acres
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Interior Forest > 10 Acre Raster (46 minutes)')
# InteriorForest_10_Con = arcpy.sa.Con(VAWV_Interior_Forest_RG_Raster, VAWV_Interior_Forest_RG_Raster, 0, "COUNT > 40468")
VAWV_Interior_Forest_10_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\VAWV_IntFor_10.tif"
# InteriorForest_10_Con.save(VAWV_Interior_Forest_10_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Interior Forest > 10 Acre Raster')
#Make Interior Forest > 10 Acre Raster have Uniform Value
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Interior Forest > 10 Acre Uniform Value Raster (21 minutes)')
# InteriorForest_Uni_Con = arcpy.sa.Con(VAWV_Interior_Forest_10_Raster, 1, "", "VALUE > 0")
VAWV_Interior_Forest_10_Uni_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\MD_IntFor_10_Uni.tif"
# InteriorForest_Uni_Con.save(VAWV_Interior_Forest_10_Uni_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Interior Forest > 10 Acre Uniform Value Raster')
#Region Group Filled Forest Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating VAWV Forest Region Group Raster (2 Hr 16 minutes)')
# ForestRegionGrp = arcpy.sa.RegionGroup(Filled_Forest_Raster, "FOUR", "WITHIN", "NO_LINK",0)
VAWV_Forest_RG_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\VAWV_Forest_RG.tif"
# ForestRegionGrp.save(VAWV_Forest_RG_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created MD Forest Region Group Raster')
#Remove Forest that is less than 50 Acres
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Forest Patches > 50 Acre Raster (46 minutes)')
# Forest_50_Con = arcpy.sa.Con(VAWV_Forest_RG_Raster, VAWV_Forest_RG_Raster, "", "COUNT > 202342")
VAWV_Forest_Patch_50_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\VAWV_Forest_Patch_50.tif"
# Forest_50_Con.save(VAWV_Forest_Patch_50_Raster)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Forest Patches > 50 Acre Raster')
#Create Forest Patch Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Forest Patch Polygon (23 minutes)' ) 
Forest_Patch_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Patch.shp"
# arcpy.RasterToPolygon_conversion(VAWV_Forest_Patch_50_Raster, Forest_Patch_Polygon, "NO_SIMPLIFY","VALUE")
# arcpy.CalculateGeometryAttributes_management(Forest_Patch_Polygon,[["Acreage","AREA"]],"","ACRES")  
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Forest Patch Polygon' )
#Create UID for MD Forest Patch Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Create UID (1 second)')
# arcpy.AddField_management(Forest_Patch_Polygon, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(Forest_Patch_Polygon, ["FID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Created UID')
# Zonal Statistics as Table on VAWV Interior Forest Raster using VAWV Forest Patch as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Interior Forest within Forest Patch (44 minutes)')
Forest_Patch_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Patch_ZS.dbf"
# ForestPatchIntForestZSaT = arcpy.sa.ZonalStatisticsAsTable(Forest_Patch_Polygon, "UID", VAWV_Interior_Forest_10_Uni_Raster, Forest_Patch_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(Forest_Patch_Polygon, "UID", Forest_Patch_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(Forest_Patch_Polygon, "Int_Acre", "LONG")
# arcpy.CalculateField_management(Forest_Patch_Polygon, "Int_Acre", "0", "PYTHON3")
# arcpy.CalculateField_management(Forest_Patch_Polygon, "Int_Acre", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(Forest_Patch_Polygon, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Interior Forest within Forest Patch')
# Create Forest Hubs Polygon by selecting Forest Patches with 10 Acres or more of Contguous Interior Forest
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Forest Hubs Polygon (1 minutes)' ) 
Forest_Hub_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Hubs.shp"
# Forest_Hub_Selection = arcpy.SelectLayerByAttribute_management(Forest_Patch_Polygon, "NEW_SELECTION", "Int_Acre >= 10")
# arcpy.CopyFeatures_management(Forest_Hub_Selection, Forest_Hub_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Forest Hubs Polygon')


#VIRGINIA
#Project VA Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project VA Parcels (14 seconds)')
VA_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\VA\Virginia_Parcels\Virginia_Parcel_Dataset_2021Q3.gdb\VA_Parcels"
VA_Parcels_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\VA\Virginia_Parcels\Virginia_Parcel_Dataset_2021Q3.gdb\VA_Parcels_Projected"
# sr = arcpy.SpatialReference("USA Contiguous Albers Equal Area Conic USGS")
# arcpy.Project_management(VA_Parcels, VA_Parcels_Projected,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA Parcels')
#Select VA Parcels in desired counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Parcels in desired counties')
VA_Parcels_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\VA\VA_Parcels_Desired_Counties.shp"
VA_Parcels_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(VA_Parcels_Projected, "NEW_SELECTION", "LOCALITY = 'Augusta County' Or LOCALITY = 'Clarke County' Or LOCALITY = 'Frederick County' Or LOCALITY = 'Highland County' Or LOCALITY = 'Loudoun County' Or LOCALITY = 'Page County' Or LOCALITY = 'Rockingham County' Or LOCALITY = 'Shenandoah County' Or LOCALITY = 'Warren County'")
# arcpy.CopyFeatures_management(VA_Parcels_Projected, VA_Parcels_Desired_Counties)
# arcpy.CopyFeatures_management(VA_Parcels_Desired_Counties_Selection, VA_Parcels_Desired_Counties)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected VA Parcels in desired counties')
#Calculate VA Parcels in Desired Counties Acreage
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculating VA Parcels in Desired Counties Acreage ( minute)')
# arcpy.CalculateGeometryAttributes_management(VA_Parcels_Desired_Counties,[["Acreage","AREA"]],"","ACRES")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculated VA Parcels in Desired Counties Acreage')
#Select VA Parcels in Desired Counties >= 50 Acres
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Parcels in desired counties')
VA_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\VA\VA_Priority_Parcels.shp"
VA_Priority_Parcels_Selection = arcpy.management.SelectLayerByAttribute(VA_Parcels_Desired_Counties, "NEW_SELECTION", "Acreage >= 50")
# arcpy.CopyFeatures_management(VA_Priority_Parcels_Selection, VA_Priority_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected VA Parcels in desired counties')
#Select US SVI in Desired VA Counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA SVI in desired counties')
US_SVI_VA_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_VA_Desired_Counties.shp"
US_SVI_VA_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(US_SVI_Projected, "NEW_SELECTION", "STCNTY = '51015' Or STCNTY = '51043' Or STCNTY = '51069' Or STCNTY = '51091' Or STCNTY = '51107' Or STCNTY = '51139' Or STCNTY = '51165' Or STCNTY = '51171' Or STCNTY = '51187'")
# arcpy.CopyFeatures_management(US_SVI_VA_Desired_Counties_Selection, US_SVI_VA_Desired_Counties)
# arcpy.CalculateField_management(US_SVI_VA_Desired_Counties, "Value", "0", "PYTHON3")
# with arcpy.da.UpdateCursor(US_SVI_VA_Desired_Counties, ['RPL_THEMES', 'Value']) as cursor:
#     for row in cursor:
#         RPL = row[0]
#         if RPL <= 0:
#             row[1] = 1
#             cursor.updateRow(row)
#         if 0 < RPL <= 0.25:
#             row[1] = 2
#             cursor.updateRow(row)
#         if 0.25 < RPL <= 0.5:
#             row[1] = 3
#             cursor.updateRow(row)
#         if 0.5 < RPL <= 0.75:
#             row[1] = 4
#             cursor.updateRow(row)
#         if RPL > 0.75:
#             row[1] = 5
#             cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected VA SVI in desired counties')
#Create US_SVI_VA Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating US_SVI_VA Raster (9 minutes)')
US_SVI_VA_Desired_Counties_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_VA.tif"
# arcpy.PolygonToRaster_conversion(US_SVI_VA_Desired_Counties, "Value", US_SVI_VA_Desired_Counties_Raster, "CELL_CENTER","",1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created US_SVI_VA Raster')
#Project Virginia Development Vulnerability 2025 Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Virginia Development Vulnerability 2025 Raster (14 seconds)')
VA_DevV_2025_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\CIC_PotomacConservancy\va_cz_2021_dev_vulnerability_2025.tif"
VA_DevV_2025_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\VA_DevV_2025.tif"
# arcpy.management.ProjectRaster(VA_DevV_2025_Raster, VA_DevV_2025_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "30 30", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Virginia Development Vulnerability 2025 Raster')
#Create UID for VA Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Create UID (11 seconds)') 
# arcpy.AddField_management(VA_Priority_Parcels, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(VA_Priority_Parcels, ["FID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Created UID')
# Zonal Statistics as Table on VA Tree Canopy Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Tree Canopy within Priority Parcels (6 minutes)')
VA_TC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_TC_ZS.dbf"
# VA_TC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VAWV_PC_TC_Raster, VA_TC_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_TC_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(VA_Priority_Parcels, "LC_TC", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_TC", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_TC", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Tree Canopy within Priority Parcels')
# Zonal Statistics as Table on VA Wetland Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Wetland within Priority Parcels (7 minutes)')
VA_Wet_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_Wet_ZS.dbf"
# VA_Wet_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VAWV_PC_Wet_Raster, VA_Wet_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Wet_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(VA_Priority_Parcels, "LC_Wet", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_Wet", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_Wet", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Wetland within Priority Parcels')
# Zonal Statistics as Table on VA Scrub\Shrub Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Scrub\Shrub within Priority Parcels (6 minutes)')
VA_SS_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_SS_ZS.dbf"
# VA_SS_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VAWV_PC_SS_Raster, VA_SS_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_SS_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(VA_Priority_Parcels, "LC_SS", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_SS", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_SS", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Scrub\Shrub within Priority Parcels')
# Zonal Statistics as Table on VA Low Vegetation Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Low Vegetation within Priority Parcels (7 minutes)')
VA_LV_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_LV_ZS.dbf"
# VA_LV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VAWV_PC_LV_Raster, VA_LV_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_LV_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(VA_Priority_Parcels, "LC_LV", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_LV", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_LV", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Low Vegetation within Priority Parcels')
# Zonal Statistics as Table on VA Water Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Water within Priority Parcels (7 minutes)')
VA_Wat_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\VA_Wat_ZS.dbf"
# VA_Wat_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VAWV_PC_Wat_Raster, VA_Wat_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Wat_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(VA_Priority_Parcels, "LC_Wat", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_Wat", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "LC_Wat", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Water within Priority Parcels')
#Select Priority Parcels that have National Historic Landmarks
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Historic Landmarks (1 second)')
# National_Historic_Landmark_selection = arcpy.SelectLayerByLocation_management(VA_Priority_Parcels, 'INTERSECT', National_Historic_Landmarks_Projected)
VA_NHL_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\VA_NHL_Parcels.shp"
# arcpy.CopyFeatures_management(National_Historic_Landmark_selection, VA_NHL_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Historic Landmarks')
#Create NHL Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NHL Field ( second)')
# NHL_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_NHL_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NHL_Parcels_selection, "NHL", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NHL Field')
#Select Priority Parcels that have National Register of Historic Sites and Places (NRHP)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Register of Historic Sites and Places (NRHP) (1 second)')
# NRHP_selection = arcpy.SelectLayerByLocation_management(VA_Priority_Parcels, 'INTERSECT', NRHP_Projected)
VA_NRHP_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\VA_NRHP_Parcels.shp"
# arcpy.CopyFeatures_management(NRHP_selection, VA_NRHP_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Register of Historic Sites and Places')
#Create NRHP Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NRHP Field ( second)')
# NRHP_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_NRHP_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NRHP_Parcels_selection, "NRHP", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NRHP Field')
#Create Historic Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Historic Field ( second)')
# arcpy.management.CalculateField(VA_Priority_Parcels, "H_SUM", "!NHL! + !NRHP!", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(VA_Priority_Parcels, "Historic", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Historic", "!H_SUM! > 0", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["H_SUM"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["NHL"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["NRHP"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Historic Field ( second)')
# Zonal Statistics as Table on CBP WQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of CBP WQ within Priority Parcels ( minutes)')
VA_WQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\VA_WQ_ZS.dbf"
# VA_WQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", WQ_Raster_Projected, VA_WQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_WQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(VA_Priority_Parcels, "WQP_Val", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP_Val", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(VA_Priority_Parcels, "WQP1", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP1", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP1", "!WQP_Val! >= 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQP2", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP2", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP2", "!WQP_Val! > 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQP3", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP3", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP3", "!WQP_Val! > 30", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQP4", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP4", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP4", "!WQP_Val! > 38", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQP5", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP5", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQP5", "!WQP_Val! > 48", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "CBP_WQP", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "CBP_WQP", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "CBP_WQP", "!WQP1! + !WQP2! + !WQP3! + !WQP4! + !WQP5!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQP1"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQP2"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQP3"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQP4"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQP5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of CBP WQ within Priority Parcels')
# Zonal Statistics as Table on TNC Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of TNC within Priority Parcels ( minutes)')
VA_TNC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\VA_TNC_ZS.dbf"
# VA_TNC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", TNC_Raster_Projected, VA_TNC_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_TNC_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(VA_Priority_Parcels, "TNC", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "TNC", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "TNC", "!MAJORITY! > 0", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of TNC within Priority Parcels')
# Zonal Statistics as Table on DWQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of DWQ within Priority Parcels ( minutes)')
VA_DWQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\VA_DWQ_ZS.dbf"
# VA_DWQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", DWQ_Raster_Projected, VA_DWQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_DWQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(VA_Priority_Parcels, "ICPRB_Val", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "ICPRB_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "ICPRB_Val", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(VA_Priority_Parcels, "WQ_30", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_30", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_30", "!ICPRB_Val! > 30", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQ_45", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_45", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_45", "!ICPRB_Val! > 45", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQ_60", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_60", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_60", "!ICPRB_Val! > 60", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQ_75", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_75", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_75", "!ICPRB_Val! > 75", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "WQ_Sum", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_Sum", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "WQ_Sum", "!WQ_30! + !WQ_45! + !WQ_60! + !WQ_75!", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "ICPRB_WQ", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "ICPRB_WQ", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "ICPRB_WQ", "!WQ_Sum! + 1", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQ_30"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQ_45"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQ_60"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQ_75"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["WQ_Sum"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of DWQ within Priority Parcels')
# Zonal Statistics as Table on VA Develompment Vulnerabilty Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority value of VA Develompment Vulnerabilty within Priority Parcels ( minutes)')
VA_DevV_2025_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\VA_DevV_2025_ZS.dbf"
# VA_DevV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_Priority_Parcels, "UID", VA_DevV_2025_Raster_Projected, VA_DevV_2025_ZS_Table, "DATA", "MAXIMUM")
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_DevV_2025_ZS_Table, "UID",["MAX"])
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_Val", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_Val", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_Val", "!MAX!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["MAX"])
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_1", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_1", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_1", "!DevV_Val! > -1", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_2", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_2", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_2", "!DevV_Val! > 1", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_3", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_3", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_3", "!DevV_Val! > 2", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_4", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_4", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_4", "!DevV_Val! > 3", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "DevV_5", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_5", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV_5", "!DevV_Val! > 5", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "DevV", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "DevV", "!DevV_1! + !DevV_2! + !DevV_3! + !DevV_4! + !DevV_5!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["DevV_1"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["DevV_2"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["DevV_3"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["DevV_4"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["DevV_5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority value of VA Develompment Vulnerabilty within Priority Parcels')
#Select VA Priority Parcels Intersecting Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels Intersecting Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
VA_Parcels_Int_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\VA_Parcels_Int_PADUS.shp"
# VA_Parcels_Int_PADUS_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "INTERSECT", PADUS_Bay, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_Int_PADUS_Selection, VA_Parcels_Int_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels Intersecting Protected Areas')
#Select VA Priority Parcels .25 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels .25 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
VA_Parcels_QM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\VA_Parcels_QM_PADUS.shp"
# VA_Parcels_QM_PADUS_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_QM_PADUS_Selection, VA_Parcels_QM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels .25 mile from Protected Areas')
#Select VA Priority Parcels .5 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels .5 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
VA_Parcels_HM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\VA_Parcels_HM_PADUS.shp"
# VA_Parcels_HM_PADUS_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_HM_PADUS_Selection, VA_Parcels_HM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels .5 mile from Protected Areas')
#Select VA Priority Parcels 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
VA_Parcels_1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\VA_Parcels_1M_PADUS.shp"
# VA_Parcels_1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_1M_PADUS_Selection, VA_Parcels_1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels 1 mile from Protected Areas')
#Select VA Priority Parcels Greater than 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels Greater Than 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
VA_Parcels_GreaterThan1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\VA_Parcels_GreaterThan1M_PADUS.shp"
# VA_Parcels_GreaterThan1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_GreaterThan1M_PADUS_Selection, VA_Parcels_GreaterThan1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels Greater Than 1 mile from Protected Areas')
#Create Adjacency to federal/state protected lands (Adj_PL) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Adjacency to federal/state protected lands (Adj_PL) Field ( second)')
# VA_Int_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_Int_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_Int_PADUS_Parcels_selection, "PL_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_QM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_QM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_QM_PADUS_Parcels_selection, "PL_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_HM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_HM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_HM_PADUS_Parcels_selection, "PL_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_1M_PADUS_Parcels_selection, "PL_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_GreaterThan1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_GreaterThan1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_GreaterThan1M_PADUS_Parcels_selection, "PL_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(VA_Priority_Parcels, "Adj_PL", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Adj_PL", "max([!PL_Int!, !PL_QM!, !PL_HM!,!PL_1M!,!PL_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PL_Int"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PL_QM"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PL_HM"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PL_1M"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PL_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Adjacency to federal/state protected lands (Adj_PL) Field')
#Select VA Priority Parcels Intersecting Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels Intersecting Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
VA_Parcels_Int_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\VA_Parcels_Int_Trails.shp"
# VA_Parcels_Int_Trails_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "INTERSECT", Baywide_Trails_Projected, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_Int_Trails_Selection, VA_Parcels_Int_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels Intersecting Trails')
#Select VA Priority Parcels .25 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels .25 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
VA_Parcels_QM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\VA_Parcels_QM_Trails.shp"
# VA_Parcels_QM_Trails_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_QM_Trails_Selection, VA_Parcels_QM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels .25 mile from Trails')
#Select VA Priority Parcels .5 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels .5 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
VA_Parcels_HM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\VA_Parcels_HM_Trails.shp"
# VA_Parcels_HM_Trails_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_HM_Trails_Selection, VA_Parcels_HM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels .5 mile from Trails')
# Select VA Priority Parcels 1 Miles from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
VA_Parcels_1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\VA_Parcels_1M_Trails.shp"
# VA_Parcels_1M_Trails_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_1M_Trails_Selection, VA_Parcels_1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels 1 mile from Trails')
#Select VA Priority Parcels Greater than 1 Mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select VA Priority Parcels Greater Than 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
VA_Parcels_GreaterThan1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\VA_Parcels_GreaterThan1M_Trails.shp"
# VA_Parcels_GreaterThan1M_Trails_Selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(VA_Parcels_GreaterThan1M_Trails_Selection, VA_Parcels_GreaterThan1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting VA Priority Parcels Greater Than 1 mile from Trails')
#Create Trail network expansion (Trail_exp) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Trail network expansion (Trail_exp) Field ( second)')
# VA_Int_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_Int_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_Int_Trails_Parcels_selection, "T_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_QM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_QM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_QM_Trails_Parcels_selection, "T_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_HM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_HM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_HM_Trails_Parcels_selection, "T_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_1M_Trails_Parcels_selection, "T_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# VA_GreaterThan1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(VA_Priority_Parcels, "ARE_IDENTICAL_TO", VA_Parcels_GreaterThan1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(VA_GreaterThan1M_Trails_Parcels_selection, "T_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(VA_Priority_Parcels, "Adj_T", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Adj_T", "max([!T_Int!, !T_QM!, !T_HM!,!T_1M!,!T_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["T_Int"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["T_QM"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["T_HM"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["T_1M"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["T_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Trail network expansion (Trail_exp) Field ')
# Summarize Within on US_SVI_VA_Desired_Counties Polygon using Priority Parcels as Zones CANT FIGURE OUT WHY IT BREAKS
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for US_SVI and create SVI_US and SVI_Val field (1 minutes)')
VA_Parcels_SW_SVI = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\VA_Parcels_SW_SVI.shp"
VA_Parcels_SW_SVI_Maj_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\VA_Parcels_SW_SVI_Maj.dbf"
# arcpy.gapro.SummarizeWithin(US_SVI_VA_Desired_Counties, VA_Parcels_SW_SVI, "POLYGON", '', None, VA_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, "Value", "ADD_MIN_MAJ", "NO_PERCENT", VA_Parcels_SW_SVI_Maj_Table)
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Parcels_SW_SVI, "UID",["MAJORITY_V"])
# arcpy.AddField_management(VA_Priority_Parcels, "SVI_US", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SVI_US", "!MAJORITY_V!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["MAJORITY_V"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within VA Priority Parcels for US_SVI and created SVI_US field')
#Create TCWetland Raster and Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Raster and Polygon (15 minutes)' ) 
VA_TCWetland_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_TCWetland.tif"
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams", "VA.gdb")
VA_TCWetland_NonTCWet_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\VA_TCWetland_NonTCWet"
# TCWtland_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, "","VALUE = 3 OR VALUE = 2")
# TCWtland_Con.save(VA_TCWetland_Raster)
# arcpy.RasterToPolygon_conversion(VA_TCWetland_Raster, VA_TCWetland_NonTCWet_Polygon, "NO_SIMPLIFY","VALUE") 
# VA_TCWetland_Selection = arcpy.management.SelectLayerByAttribute(VA_TCWetland_NonTCWet_Polygon, "NEW_SELECTION", "gridcode = 1")
VA_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\VA_TCWetland"
# arcpy.CopyFeatures_management(VA_TCWetland_Selection, VA_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Raster and Polygon' )
# Eliminate totally included areas on TCWetland Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminate totally included areas on VA TCWetland Polygons (1 minute)')
VA_TCWetland_Eliminated_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\VA_TCWetland_Eliminated"
# arcpy.EliminatePolygonPart_management(VA_TCWetland_Polygon, VA_TCWetland_Eliminated_Polygon, "AREA", 100000, "", "CONTAINED_ONLY")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminated totally included areas on VA TCWetland Polygons')
# Create TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Polygon (15 minutes)')
VA_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\VA_TCWetland_Holes"
# arcpy.SymDiff_analysis(VA_TCWetland_Eliminated_Polygon, VA_TCWetland_Polygon, VA_TCWetland_Holes_Polygon, "ALL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Polygon')
# Create TCWetland Holes Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Singlepart Polygon (1 minutes)')
VA_TCWetland_Holes_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\VA_TCWetland_Holes_Singlepart"
# arcpy.MultipartToSinglepart_management(VA_TCWetland_Holes_Polygon, VA_TCWetland_Holes_Singlepart_Polygon)
# arcpy.AddField_management(VA_TCWetland_Holes_Singlepart_Polygon, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(VA_TCWetland_Holes_Singlepart_Polygon, ["OBJECTID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Singlepart Polygon')
# Zonal Statistics as Table on VA Water LC Raster using TCWetland Holes Singlepart Polygon as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to determine Water/Non-Water Forest holes (1 hr 33 minutes)')
TCWetland_Hole_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\TCWetland_Hole_ZS.dbf"
# TCWetlandHoleZSaT = arcpy.sa.ZonalStatisticsAsTable(VA_TCWetland_Holes_Singlepart_Polygon, "UID", VAWV_PC_Wat_Raster, TCWetland_Hole_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(VA_TCWetland_Holes_Singlepart_Polygon, "UID", TCWetland_Hole_ZS_Table, "UID",["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to determine Water/Non-Water Forest holes')
# Create Natural TCWetland Holes Polygon by selecting forest holes with a majority of Natural LU/TC in AG
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Natural Forest Holes Polygon (20 second)' ) 
Natural_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\Natural_TCWetland_Holes"
# Natural_TCWetland_Holes_Selection = arcpy.SelectLayerByAttribute_management(VA_TCWetland_Holes_Singlepart_Polygon, "NEW_SELECTION", "MAJORITY = 1")
# arcpy.CopyFeatures_management(Natural_TCWetland_Holes_Selection, Natural_TCWetland_Holes_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Natural TCWetland Holes Polygon')
#Merge VA TCWetland Polygon and Natural TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge TCWetland Polygons (1 minute)')
Merged_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\Merged_TCWetland"
# arcpy.management.Merge([VA_TCWetland_Polygon,Natural_TCWetland_Holes_Polygon], Merged_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
# Create Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Merged TCWetland Single Part Polygon (1 minutes)')
Merged_TCWetland_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\Merged_TCWetland_Singlepart"
# arcpy.MultipartToSinglepart_management(Merged_TCWetland_Polygon, Merged_TCWetland_Singlepart_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Merged TCWetland Single Part Polygon')
#Create Filled TCWetland Polygon by dissolving Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Filled TCWetland Polygon (10 minutes)')
Filled_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\Filled_TCWetland"
# arcpy.PairwiseDissolve_analysis(Merged_TCWetland_Singlepart_Polygon, Filled_TCWetland_Polygon, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled TCWetland Polygon')
#Clip StreamRivers to Filled TC Wetland
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VA StreamRivers Clipped (10 minutes)')
VA_StreamRivers_Clipped = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Clipped.shp"
# arcpy.PairwiseClip_analysis(StreamRivers,Filled_TCWetland_Polygon,VA_StreamRivers_Clipped)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VA StreamRivers Clipped (10 minutes)')
# Create VA StreamRivers Clipped Singlepart Line
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create  VA StreamRivers Clipped Singlepart (1 minutes)')
VA_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Clipped_Singlepart.shp"
# arcpy.MultipartToSinglepart_management(VA_StreamRivers_Clipped, VA_StreamRiver_Clipped_Singlepart)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VA StreamRivers Clipped Singlepart')
#Buffer StreamRivers by 100 Feet
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffering VA StreamRivers Clipped Singlepart by 100 feet ( seconds)')
VA_StreamRiver_Buffer_PreClip = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Buffer_PreClip.shp"
# arcpy.analysis.PairwiseBuffer(VA_StreamRiver_Clipped_Singlepart, VA_StreamRiver_Buffer_PreClip, "100 Feet")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffered VA StreamRivers Clipped Singlepart by 100 feet')
va_cflist = [
    'augu_51015',
    'clar_51043',
    'fred_51069',
    'high_51091',
    'loud_51107',
    'page_51139',
    'rock_51165',
    'shen_51171',
    'warr_51187',
    
    ]
va_StreamRiver_Buffer_list = []
for cf in va_cflist:
    # print('############################')
    # print('####### {} #########'.format(cf))
    # print('############################')
    #Create Blank County Polygons
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Blank County Polygons')
    cf_Blank_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Blank.tif".format(cf)
    cf_Blank_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Polygon.shp".format(cf)
    # arcpy.RasterToPolygon_conversion(cf_Blank_Raster, cf_Blank_Polygon, "NO_SIMPLIFY","VALUE") 
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Blank County Polygons')
    # Create County StreamRivers Buffers #REDO
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Create  VA StreamRivers Clipped (1 minutes)')
    cf_StreamRiver_Buffer_PreClip = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\{}_StreamRiver_Buffer_PreClip.shp".format(cf)
    # arcpy.PairwiseClip_analysis(StreamRiver_Buffer,cf_Blank_Polygon,cf_StreamRiver_Buffer_PreClip)
    cf_StreamRiver_Buffer = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\{}_StreamRiver_Buffer.shp".format(cf)
    # arcpy.PairwiseClip_analysis(cf_StreamRiver_Buffer_PreClip,Filled_TCWetland_Polygon,cf_StreamRiver_Buffer)
    va_StreamRiver_Buffer_list.append(cf_StreamRiver_Buffer)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created VA StreamRivers Clipped Singlepart')
#Merge County Stream Buffer Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge County Stream Buffer Polygons (1 minute)')
Merged_VA_StreamBuffer_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA.gdb\Merged_VA_StreamBuffer"
# arcpy.management.Merge(va_StreamRiver_Buffer_list, Merged_VA_StreamBuffer_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
#Create VA Stream Buffer Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create VA StreamRivers Buffer Singlepart (10 minutes)')
VA_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Buffer_Singlepart.shp"
# arcpy.PairwiseDissolve_analysis(Merged_VA_StreamBuffer_Polygon, VA_StreamRiver_Buffer_Singlepart, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created VA StreamRivers Buffer Singlepart')
# Summarize Within VA Priority Parcels for Streams
t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for Streams (1 minutes)')
VA_Parcels_SW_Streams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_Parcels_SW_Streams.shp"
# arcpy.gapro.SummarizeWithin(StreamRivers, VA_Parcels_SW_Streams, "POLYGON", '', None, VA_Priority_Parcels, "ADD_SUMMARY", "MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for Buffered Stream Area (1 minutes)')
# Summarize Within VA Priority Parcels for Buffered Streams
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for Buffered Streams (1 minutes)')
VA_Parcels_SW_BuffStreams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_Parcels_SW_BuffStreams.shp"
# arcpy.gapro.SummarizeWithin(VA_StreamRiver_Buffer_Singlepart, VA_Parcels_SW_BuffStreams, "POLYGON", '', None, VA_Priority_Parcels, "ADD_SUMMARY", "SQUARE_MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for Streams (1 minutes)')
#Join Stream Mile and Buffered Stream Area field back to VA Priority Parcels and Create Stream Buffer Ratio
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Stream Mile and Buffered Stream Area field back to VA Priority Parcels (1 minutes)')
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Parcels_SW_Streams, "UID",["sum_length"])
# arcpy.AddField_management(VA_Priority_Parcels, "Stream_M", "FLOAT")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Stream_M", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Stream_M", "!sum_length!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["sum_length"])
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Parcels_SW_BuffStreams, "UID",["sum_area_s"])
# arcpy.AddField_management(VA_Priority_Parcels, "BuffS_Area", "FLOAT")
# arcpy.CalculateField_management(VA_Priority_Parcels, "BuffS_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "BuffS_Area", "!sum_area_s!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["sum_area_s"])
# arcpy.AddField_management(VA_Priority_Parcels, "SB_Ratio", "FLOAT")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB_Ratio", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB_Ratio", "(!BuffS_Area! * !Stream_M!) / 0.038", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Stream Mile and Buffered Stream Area field back to VA Priority Parcels')
#Create SB attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Stream Buffer attribute (1 minutes)')
# arcpy.AddField_management(VA_Priority_Parcels, "SB1", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB1", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB1", "!SB_Ratio! >= 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "SB2", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB2", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB2", "!SB_Ratio! > 0.010495", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "SB3", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB3", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB3", "!SB_Ratio! > 0.048996", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "SB4", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB4", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB4", "!SB_Ratio! > 0.127791", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "SB5", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB5", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB5", "!SB_Ratio! > 0.347993", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "SB", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "SB", "!SB1! + !SB2! + !SB3! + !SB4! + !SB5!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["SB1"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["SB2"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["SB3"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["SB4"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["SB5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Stream Buffer attribute')
#Create Parcel Size attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Parcel Size attribute (1 minutes)')
# arcpy.AddField_management(VA_Priority_Parcels, "PS1", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS1", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS1", "!Acreage! >= 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "PS2", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS2", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS2", "!Acreage! >= 75", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "PS3", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS3", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS3", "!Acreage! >= 100", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "PS4", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS4", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS4", "!Acreage! >= 125", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "PS5", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS5", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS5", "!Acreage! > 150", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "PS", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "PS", "!PS1! + !PS2! + !PS3! + !PS4! + !PS5!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PS1"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PS2"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PS3"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PS4"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["PS5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Parcel Size attribute (1 minutes)')
# Summarize Within VA Priority Parcels for Forest Hubs (No Wetland Hubs in VA study area could be different in VA)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within VA Priority Parcels for Hubs (1 minutes)')
VAWV_Forest_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Hubs.shp"
VA_Parcels_SW_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VA_Parcels_SW_Hubs.shp"
# arcpy.gapro.SummarizeWithin(VAWV_Forest_Hubs, VA_Parcels_SW_Hubs, "POLYGON", '', None, VA_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within VA Priority Parcels for Hubs')
#Join Hub Area field back to VA Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Hub Area field back to VA Priority Parcels (1 minutes)')
# arcpy.JoinField_management(VA_Priority_Parcels, "UID", VA_Parcels_SW_Hubs, "UID",["sum_area_a"])
# arcpy.AddField_management(VA_Priority_Parcels, "Hub_Area", "FLOAT")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub_Area", "!sum_area_a!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["sum_area_a"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Hub Area field back to VA Priority Parcels')
# Create Hub attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Hub attribute (1 minutes)')
# arcpy.AddField_management(VA_Priority_Parcels, "Hub1", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub1", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub1", "!Hub_Area! >= 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "Hub2", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub2", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub2", "!Hub_Area! > 0", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "Hub3", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub3", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub3", "!Hub_Area! > 10", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "Hub4", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub4", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub4", "!Hub_Area! > 30", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "Hub5", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub5", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub5", "!Hub_Area! > 50", "PYTHON3")
# arcpy.AddField_management(VA_Priority_Parcels, "Hub", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub", "0", "PYTHON3")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Hub", "!Hub1! + !Hub2! + !Hub3! + !Hub4! + !Hub5!", "PYTHON3")
# arcpy.DeleteField_management(VA_Priority_Parcels, ["Hub1"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["Hub2"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["Hub3"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["Hub4"])
# arcpy.DeleteField_management(VA_Priority_Parcels, ["Hub5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Hub attribute')
#Create Priority Attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Priority attribute (1 minutes)')
# arcpy.AddField_management(VA_Priority_Parcels, "Score", "LONG")
# arcpy.CalculateField_management(VA_Priority_Parcels, "Score", "(!TNC! * 5) + !Hub! + !CBP_WQP! + !ICPRB_WQ! + !DevV! + !SB! + !Adj_PL! + !Adj_T! + (!Historic! * 5) + !PS! + !SVI_US!", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Priority attribute (1 minutes)')






#WEST VIRGINIA
#Merge WV Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge WV Parcels (1 minute)')
WV_Parcel_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\WV_Parcels.shp"
WV_Parcel_List = [
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\berk_54003\Berkeley - WV Property Tax Division\Berkeley_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\gran_54023\Grant- WV Property Tax Division\Grant_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\hard_54031\Hardy - WV Property Tax Division\Hardy_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\hamp_54027\Hampshire - WV Property Tax Division\Hampshire_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\jeff_54037\Jefferson- WV Property Tax Division\Jefferson_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\mine_54057\Mineral- WV Property Tax Division\Mineral_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\morg_54065\Morgan- WV Property Tax Division\Morgan_projected.shp",
    r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\pend_54071\Pendleton- WV Property Tax Division\Pendleton_projected.shp"
    ]
# arcpy.management.Merge(WV_Parcel_List, WV_Parcel_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged WV Parcels')
#Calculate WV Parcels in Desired Counties Acreage
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculating WV Parcels in Desired Counties Acreage ( minute)')
# arcpy.CalculateGeometryAttributes_management(WV_Parcel_Polygon,[["Acreage","AREA"]],"","ACRES")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Calculated WV Parcels in Desired Counties Acreage')
#Select WV Parcels in Desired Counties >= 50 Acres
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Parcels in desired counties')
WV_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\WV_Priority_Parcels.shp"
# WV_Priority_Parcels_Selection = arcpy.management.SelectLayerByAttribute(WV_Parcel_Polygon, "NEW_SELECTION", "Acreage >= 50")
# arcpy.CopyFeatures_management(WV_Priority_Parcels_Selection, WV_Priority_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected WV Parcels in desired counties')
#Select US SVI in Desired WV Counties
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV SVI in desired counties')
US_SVI_WV_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_WV_Desired_Counties.shp"
# US_SVI_WV_Desired_Counties_Selection = arcpy.management.SelectLayerByAttribute(US_SVI_Projected, "NEW_SELECTION", "STCNTY = '54003' Or STCNTY = '54023' Or STCNTY = '54027' Or STCNTY = '54031' Or STCNTY = '54037' Or STCNTY = '54057' Or STCNTY = '54065' Or STCNTY = '54071'")
# arcpy.CopyFeatures_management(US_SVI_WV_Desired_Counties_Selection, US_SVI_WV_Desired_Counties)
# arcpy.CalculateField_management(US_SVI_WV_Desired_Counties, "Value", "0", "PYTHON3")
# with arcpy.da.UpdateCursor(US_SVI_WV_Desired_Counties, ['RPL_THEMES', 'Value']) as cursor:
#     for row in cursor:
#         RPL = row[0]
#         if RPL <= 0:
#             row[1] = 1
#             cursor.updateRow(row)
#         if 0 < RPL <= 0.25:
#             row[1] = 2
#             cursor.updateRow(row)
#         if 0.25 < RPL <= 0.5:
#             row[1] = 3
#             cursor.updateRow(row)
#         if 0.5 < RPL <= 0.75:
#             row[1] = 4
#             cursor.updateRow(row)
#         if RPL > 0.75:
#             row[1] = 5
#             cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected WV SVI in desired counties')
#Create US_SVI_WV Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating US_SVI_WV Raster (9 minutes)')
US_SVI_WV_Desired_Counties_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_WV.tif"
# arcpy.PolygonToRaster_conversion(US_SVI_WV_Desired_Counties, "Value", US_SVI_WV_Desired_Counties_Raster, "CELL_CENTER","",1)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created US_SVI_WV Raster')
#Project West Virginia Development Vulnerability 2025 Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project West Virginia Development Vulnerability 2025 Raster (14 seconds)')
WV_DevV_2025_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\CIC_PotomacConservancy\WV_cz_2021_dev_vulnerability_2025.tif"
WV_DevV_2025_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\WV_DevV_2025.tif"
# arcpy.management.ProjectRaster(WV_DevV_2025_Raster, WV_DevV_2025_Raster_Projected, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NEAREST", "30 30", None, None, 'PROJCS["NAD_1983_UTM_Zone_18N",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-75.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected West Virginia Development Vulnerability 2025 Raster')
#Create UID for WV Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Create UID (11 seconds)') 
# arcpy.AddField_management(WV_Priority_Parcels, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(WV_Priority_Parcels, ["FID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,'Created UID')
# Zonal Statistics as Table on WV Tree Canopy Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Tree Canopy within Priority Parcels (6 minutes)')
WV_TC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_TC_ZS.dbf"
# WV_TC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", VAWV_PC_TC_Raster, WV_TC_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_TC_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(WV_Priority_Parcels, "LC_TC", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_TC", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_TC", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Tree Canopy within Priority Parcels')
# Zonal Statistics as Table on WV Wetland Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Wetland within Priority Parcels (7 minutes)')
WV_Wet_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_Wet_ZS.dbf"
# WV_Wet_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", VAWV_PC_Wet_Raster, WV_Wet_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Wet_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(WV_Priority_Parcels, "LC_Wet", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_Wet", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_Wet", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Wetland within Priority Parcels')
# Zonal Statistics as Table on WV Scrub\Shrub Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Scrub\Shrub within Priority Parcels (6 minutes)')
WV_SS_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_SS_ZS.dbf"
# WV_SS_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", VAWV_PC_SS_Raster, WV_SS_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_SS_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(WV_Priority_Parcels, "LC_SS", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_SS", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_SS", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Scrub\Shrub within Priority Parcels')
# Zonal Statistics as Table on WV Low Vegetation Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Low Vegetation within Priority Parcels (7 minutes)')
WV_LV_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_LV_ZS.dbf"
# WV_LV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", VAWV_PC_LV_Raster, WV_LV_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_LV_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(WV_Priority_Parcels, "LC_LV", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_LV", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_LV", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Low Vegetation within Priority Parcels')
# Zonal Statistics as Table on WV Water Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of Water within Priority Parcels (7 minutes)')
WV_Wat_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\LC\WV_Wat_ZS.dbf"
# WV_Wat_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", VAWV_PC_Wat_Raster, WV_Wat_ZS_Table, "DATA", "SUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Wat_ZS_Table, "UID",["COUNT"])
# arcpy.AddField_management(WV_Priority_Parcels, "LC_Wat", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_Wat", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "LC_Wat", "!COUNT! / 4046.86", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["COUNT"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of Water within Priority Parcels')
#Select Priority Parcels that have National Historic Landmarks
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Historic Landmarks (1 second)')
# National_Historic_Landmark_selection = arcpy.SelectLayerByLocation_management(WV_Priority_Parcels, 'INTERSECT', National_Historic_Landmarks_Projected)
WV_NHL_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\WV_NHL_Parcels.shp"
# arcpy.CopyFeatures_management(National_Historic_Landmark_selection, WV_NHL_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Historic Landmarks')
# #Create NHL Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NHL Field ( second)')
# NHL_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_NHL_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NHL_Parcels_selection, "NHL", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NHL Field')
#Select Priority Parcels that have National Register of Historic Sites and Places (NRHP)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting Priority Parcels that have National Register of Historic Sites and Places (NRHP) (1 second)')
# NRHP_selection = arcpy.SelectLayerByLocation_management(WV_Priority_Parcels, 'INTERSECT', NRHP_Projected)
WV_NRHP_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\WV_NRHP_Parcels.shp"
# arcpy.CopyFeatures_management(NRHP_selection, WV_NRHP_Parcels)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selected Priority Parcels that have National Register of Historic Sites and Places')
#Create NRHP Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating NRHP Field ( second)')
# NRHP_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_NRHP_Parcels, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(NRHP_Parcels_selection, "NRHP", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created NRHP Field')
#Create Historic Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Historic Field ( second)')
# arcpy.management.CalculateField(WV_Priority_Parcels, "H_SUM", "!NHL! + !NRHP!", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(WV_Priority_Parcels, "Historic", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Historic", "!H_SUM! > 0", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["H_SUM"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["NHL"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["NRHP"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Historic Field ( second)')
# Zonal Statistics as Table on CBP WQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find amount of CBP WQ within Priority Parcels ( minutes)')
WV_WQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\WV_WQ_ZS.dbf"
# WV_WQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", WQ_Raster_Projected, WV_WQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_WQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(WV_Priority_Parcels, "WQP_WVl", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP_WVl", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP_WVl", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(WV_Priority_Parcels, "WQP1", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP1", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP1", "!WQP_WVl! >= 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQP2", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP2", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP2", "!WQP_WVl! > 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQP3", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP3", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP3", "!WQP_WVl! > 30", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQP4", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP4", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP4", "!WQP_WVl! > 38", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQP5", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP5", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQP5", "!WQP_WVl! > 48", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "CBP_WQP", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "CBP_WQP", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "CBP_WQP", "!WQP1! + !WQP2! + !WQP3! + !WQP4! + !WQP5!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQP1"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQP2"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQP3"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQP4"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQP5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find amount of CBP WQ within Priority Parcels')
# Zonal Statistics as Table on TNC Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority Value of TNC within Priority Parcels ( minutes)')
WV_TNC_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\WV_TNC_ZS.dbf"
# WV_TNC_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", TNC_Raster_Projected, WV_TNC_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_TNC_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(WV_Priority_Parcels, "TNC", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "TNC", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "TNC", "!MAJORITY! > 0", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority Value of TNC within Priority Parcels')
# Zonal Statistics as Table on DWQ Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority Value of DWQ within Priority Parcels ( minutes)')
WV_DWQ_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\WV_DWQ_ZS.dbf"
# WV_DWQ_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", DWQ_Raster_Projected, WV_DWQ_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_DWQ_ZS_Table, "UID",["MAJORITY"])
# arcpy.AddField_management(WV_Priority_Parcels, "ICPRB_WVl", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "ICPRB_WVl", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "ICPRB_WVl", "!MAJORITY!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["MAJORITY"])
# arcpy.AddField_management(WV_Priority_Parcels, "WQ_30", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_30", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_30", "!ICPRB_WVl! > 30", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQ_45", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_45", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_45", "!ICPRB_WVl! > 45", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQ_60", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_60", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_60", "!ICPRB_WVl! > 60", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQ_75", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_75", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_75", "!ICPRB_WVl! > 75", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "WQ_Sum", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_Sum", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "WQ_Sum", "!WQ_30! + !WQ_45! + !WQ_60! + !WQ_75!", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "ICPRB_WQ", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "ICPRB_WQ", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "ICPRB_WQ", "!WQ_Sum! + 1", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQ_30"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQ_45"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQ_60"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQ_75"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["WQ_Sum"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority Value of DWQ within Priority Parcels')
# Zonal Statistics as Table on WV Develompment Vulnerabilty Raster using Priority Parcels as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to find majority Value of WV Develompment Vulnerabilty within Priority Parcels ( minutes)')
WV_DevV_2025_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Development_Vulnerability\WV_DevV_2025_ZS.dbf"
# WV_DevV_ZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_Priority_Parcels, "UID", WV_DevV_2025_Raster_Projected, WV_DevV_2025_ZS_Table, "DATA", "MAXIMUM")
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_DevV_2025_ZS_Table, "UID",["MAX"])
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_WVl", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_WVl", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_WVl", "!MAX!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["MAX"])
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_1", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_1", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_1", "!DevV_WVl! > -1", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_2", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_2", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_2", "!DevV_WVl! > 1", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_3", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_3", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_3", "!DevV_WVl! > 2", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_4", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_4", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_4", "!DevV_WVl! > 3", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "DevV_5", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_5", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV_5", "!DevV_WVl! > 5", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "DevV", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "DevV", "!DevV_1! + !DevV_2! + !DevV_3! + !DevV_4! + !DevV_5!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["DevV_1"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["DevV_2"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["DevV_3"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["DevV_4"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["DevV_5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to find majority Value of WV Develompment Vulnerabilty within Priority Parcels')
#Select WV Priority Parcels Intersecting Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels Intersecting Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
WV_Parcels_Int_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\WV_Parcels_Int_PADUS.shp"
# WV_Parcels_Int_PADUS_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "INTERSECT", PADUS_Bay, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_Int_PADUS_Selection, WV_Parcels_Int_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels Intersecting Protected Areas')
#Select WV Priority Parcels .25 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels .25 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
WV_Parcels_QM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\WV_Parcels_QM_PADUS.shp"
# WV_Parcels_QM_PADUS_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_QM_PADUS_Selection, WV_Parcels_QM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels .25 mile from Protected Areas')
#Select WV Priority Parcels .5 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels .5 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
WV_Parcels_HM_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\WV_Parcels_HM_PADUS.shp"
# WV_Parcels_HM_PADUS_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_HM_PADUS_Selection, WV_Parcels_HM_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels .5 mile from Protected Areas')
#Select WV Priority Parcels 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
WV_Parcels_1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\WV_Parcels_1M_PADUS.shp"
# WV_Parcels_1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_1M_PADUS_Selection, WV_Parcels_1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels 1 mile from Protected Areas')
#Select WV Priority Parcels Greater than 1 mile from Protected Areas
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels Greater Than 1 mile from Protected Areas')
PADUS_Bay = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\PADUS_Bay\PADUS_Bay.shp"
WV_Parcels_GreaterThan1M_PADUS = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Protected_Lands\WV_Parcels_GreaterThan1M_PADUS.shp"
# WV_Parcels_GreaterThan1M_PADUS_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", PADUS_Bay, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_GreaterThan1M_PADUS_Selection, WV_Parcels_GreaterThan1M_PADUS)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels Greater Than 1 mile from Protected Areas')
#Create Adjacency to federal/state protected lands (Adj_PL) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Adjacency to federal/state protected lands (Adj_PL) Field ( second)')
# WV_Int_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_Int_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_Int_PADUS_Parcels_selection, "PL_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_QM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_QM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_QM_PADUS_Parcels_selection, "PL_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_HM_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_HM_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_HM_PADUS_Parcels_selection, "PL_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_1M_PADUS_Parcels_selection, "PL_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_GreaterThan1M_PADUS_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_GreaterThan1M_PADUS, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_GreaterThan1M_PADUS_Parcels_selection, "PL_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(WV_Priority_Parcels, "Adj_PL", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Adj_PL", "max([!PL_Int!, !PL_QM!, !PL_HM!,!PL_1M!,!PL_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PL_Int"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PL_QM"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PL_HM"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PL_1M"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PL_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Adjacency to federal/state protected lands (Adj_PL) Field')
#Select WV Priority Parcels Intersecting Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels Intersecting Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
WV_Parcels_Int_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\WV_Parcels_Int_Trails.shp"
# WV_Parcels_Int_Trails_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "INTERSECT", Baywide_Trails_Projected, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_Int_Trails_Selection, WV_Parcels_Int_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels Intersecting Trails')
#Select WV Priority Parcels .25 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels .25 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
WV_Parcels_QM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\WV_Parcels_QM_Trails.shp"
# WV_Parcels_QM_Trails_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.25 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_QM_Trails_Selection, WV_Parcels_QM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels .25 mile from Trails')
#Select WV Priority Parcels .5 mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels .5 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
WV_Parcels_HM_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\WV_Parcels_HM_Trails.shp"
# WV_Parcels_HM_Trails_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "0.5 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_HM_Trails_Selection, WV_Parcels_HM_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels .5 mile from Trails')
#Select WV Priority Parcels 1 Miles from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
WV_Parcels_1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\WV_Parcels_1M_Trails.shp"
# WV_Parcels_1M_Trails_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "NOT_INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_1M_Trails_Selection, WV_Parcels_1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels 1 mile from Trails')
#Select WV Priority Parcels Greater than 1 Mile from Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Select WV Priority Parcels Greater Than 1 mile from Trails')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
WV_Parcels_GreaterThan1M_Trails = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\WV_Parcels_GreaterThan1M_Trails.shp"
# WV_Parcels_GreaterThan1M_Trails_Selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "WITHIN_A_DISTANCE", Baywide_Trails_Projected, "1 Miles", "NEW_SELECTION", "INVERT")
# arcpy.CopyFeatures_management(WV_Parcels_GreaterThan1M_Trails_Selection, WV_Parcels_GreaterThan1M_Trails)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Selecting WV Priority Parcels Greater Than 1 mile from Trails')
#Create Trail network expansion (Trail_exp) Field
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Creating Trail network expansion (Trail_exp) Field ( second)')
# WV_Int_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_Int_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_Int_Trails_Parcels_selection, "T_Int", "5", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_QM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_QM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_QM_Trails_Parcels_selection, "T_QM", "4", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_HM_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_HM_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_HM_Trails_Parcels_selection, "T_HM", "3", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_1M_Trails_Parcels_selection, "T_1M", "2", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# WV_GreaterThan1M_Trails_Parcels_selection = arcpy.management.SelectLayerByLocation(WV_Priority_Parcels, "ARE_IDENTICAL_TO", WV_Parcels_GreaterThan1M_Trails, None, "NEW_SELECTION", "NOT_INVERT")
# arcpy.management.CalculateField(WV_GreaterThan1M_Trails_Parcels_selection, "T_G1M", "1", "PYTHON3", '', "LONG", "NO_ENFORCE_DOMAINS")
# arcpy.AddField_management(WV_Priority_Parcels, "Adj_T", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Adj_T", "max([!T_Int!, !T_QM!, !T_HM!,!T_1M!,!T_G1M!])", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["T_Int"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["T_QM"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["T_HM"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["T_1M"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["T_G1M"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Trail network expansion (Trail_exp) Field ')
# Summarize Within on US_SVI_WV_Desired_Counties Polygon using Priority Parcels as Zones CANT FIGURE OUT WHY IT BREAKS
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for US_SVI and create SVI_US and SVI_WVl field (1 minutes)')
WV_Parcels_SW_SVI = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\WV_Parcels_SW_SVI.shp"
WV_Parcels_SW_SVI_Maj_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\WV_Parcels_SW_SVI_Maj.dbf"
# arcpy.gapro.SummarizeWithin(US_SVI_WV_Desired_Counties, WV_Parcels_SW_SVI, "POLYGON", '', None, WV_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, "Value", "ADD_MIN_MAJ", "NO_PERCENT", WV_Parcels_SW_SVI_Maj_Table)
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Parcels_SW_SVI, "UID",["MAJORITY_V"])
# arcpy.AddField_management(WV_Priority_Parcels, "SVI_US", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SVI_US", "!MAJORITY_V!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["MAJORITY_V"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within WV Priority Parcels for US_SVI and created SVI_US field')
#Create TCWetland Raster and Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Raster and Polygon (15 minutes)' ) 
WV_TCWetland_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_TCWetland.tif"
# arcpy.CreateFileGDB_management(r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams", "WV.gdb")
WV_TCWetland_NonTCWet_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\WV_TCWetland_NonTCWet"
# TCWtland_Con = arcpy.sa.Con(VAWV_PC_LC_Raster, 1, "","VALUE = 3 OR VALUE = 2")
# TCWtland_Con.save(WV_TCWetland_Raster)
# arcpy.RasterToPolygon_conversion(WV_TCWetland_Raster, WV_TCWetland_NonTCWet_Polygon, "NO_SIMPLIFY","VALUE") 
# WV_TCWetland_Selection = arcpy.management.SelectLayerByAttribute(WV_TCWetland_NonTCWet_Polygon, "NEW_SELECTION", "gridcode = 1")
WV_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\WV_TCWetland"
# arcpy.CopyFeatures_management(WV_TCWetland_Selection, WV_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Raster and Polygon' )
# Eliminate totally included areas on TCWetland Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminate totally included areas on WV TCWetland Polygons (1 minute)')
WV_TCWetland_Eliminated_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\WV_TCWetland_Eliminated"
# arcpy.EliminatePolygonPart_management(WV_TCWetland_Polygon, WV_TCWetland_Eliminated_Polygon, "AREA", 100000, "", "CONTAINED_ONLY")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Eliminated totally included areas on WV TCWetland Polygons')
# Create TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Polygon (15 minutes)')
WV_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\WV_TCWetland_Holes"
# arcpy.SymDiff_analysis(WV_TCWetland_Eliminated_Polygon, WV_TCWetland_Polygon, WV_TCWetland_Holes_Polygon, "ALL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Polygon')
# Create TCWetland Holes Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create TCWetland Holes Singlepart Polygon (1 minutes)')
WV_TCWetland_Holes_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\WV_TCWetland_Holes_Singlepart"
# arcpy.MultipartToSinglepart_management(WV_TCWetland_Holes_Polygon, WV_TCWetland_Holes_Singlepart_Polygon)
# arcpy.AddField_management(WV_TCWetland_Holes_Singlepart_Polygon, "UID", "LONG")
# total=0
# with arcpy.da.UpdateCursor(WV_TCWetland_Holes_Singlepart_Polygon, ["OBJECTID", "UID"]) as cursor:
#     for row in cursor:
#         total += 1
#         row[1]= total
#         cursor.updateRow(row)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created TCWetland Holes Singlepart Polygon')
# Zonal Statistics as Table on WV Water LC Raster using TCWetland Holes Singlepart Polygon as Zones
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Run Zonal Stats to determine Water/Non-Water Forest holes (1 hr 33 minutes)')
TCWetland_Hole_ZS_Table = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\TCWetland_Hole_ZS.dbf"
# TCWetlandHoleZSaT = arcpy.sa.ZonalStatisticsAsTable(WV_TCWetland_Holes_Singlepart_Polygon, "UID", VAWV_PC_Wat_Raster, TCWetland_Hole_ZS_Table, "DATA", "MAJORITY")
# arcpy.JoinField_management(WV_TCWetland_Holes_Singlepart_Polygon, "UID", TCWetland_Hole_ZS_Table, "UID",["MAJORITY"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Ran Zonal Stats to determine Water/Non-Water Forest holes')
# Create Natural TCWetland Holes Polygon by selecting forest holes with a majority of Natural LU/TC in AG
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Natural Forest Holes Polygon (20 second)' ) 
Natural_TCWetland_Holes_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\Natural_TCWetland_Holes"
# Natural_TCWetland_Holes_Selection = arcpy.SelectLayerByAttribute_management(WV_TCWetland_Holes_Singlepart_Polygon, "NEW_SELECTION", "MAJORITY = 1")
# arcpy.CopyFeatures_management(Natural_TCWetland_Holes_Selection, Natural_TCWetland_Holes_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Natural TCWetland Holes Polygon')
#Merge WV TCWetland Polygon and Natural TCWetland Holes Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge TCWetland Polygons (1 minute)')
Merged_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\Merged_TCWetland"
# arcpy.management.Merge([WV_TCWetland_Polygon,Natural_TCWetland_Holes_Polygon], Merged_TCWetland_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
# Create Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Merged TCWetland Single Part Polygon (1 minutes)')
Merged_TCWetland_Singlepart_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\Merged_TCWetland_Singlepart"
# arcpy.MultipartToSinglepart_management(Merged_TCWetland_Polygon, Merged_TCWetland_Singlepart_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Merged TCWetland Single Part Polygon')
#Create Filled TCWetland Polygon by dissolving Merged TCWetland Single Part Polygon
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Filled TCWetland Polygon (10 minutes)')
Filled_TCWetland_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\Filled_TCWetland"
# arcpy.PairwiseDissolve_analysis(Merged_TCWetland_Singlepart_Polygon, Filled_TCWetland_Polygon, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Filled TCWetland Polygon')
#Clip StreamRivers to Filled TC Wetland
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create WV StreamRivers Clipped (10 minutes)')
WV_StreamRivers_Clipped = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Clipped.shp"
# arcpy.PairwiseClip_analysis(StreamRivers,Filled_TCWetland_Polygon,WV_StreamRivers_Clipped)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created WV StreamRivers Clipped (10 minutes)')
# Create WV StreamRivers Clipped Singlepart Line
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create  WV StreamRivers Clipped Singlepart (1 minutes)')
WV_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Clipped_Singlepart.shp"
# arcpy.MultipartToSinglepart_management(WV_StreamRivers_Clipped, WV_StreamRiver_Clipped_Singlepart)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created WV StreamRivers Clipped Singlepart')
#Buffer StreamRivers by 100 Feet
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffering WV StreamRivers Clipped Singlepart by 100 feet ( seconds)')
WV_StreamRiver_Buffer_PreClip = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Buffer_PreClip.shp"
# arcpy.analysis.PairwiseBuffer(WV_StreamRiver_Clipped_Singlepart, WV_StreamRiver_Buffer_PreClip, "100 Feet")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Buffered WV StreamRivers Clipped Singlepart by 100 feet')
wv_cflist = [
    'berk_54003',
    'gran_54023',
    'hamp_54027',
    'hard_54031',
    'jeff_54037',
    'mine_54057',
    'morg_54065',
    'pend_54071',
    
    ]
wv_StreamRiver_Buffer_list = []
for cf in wv_cflist:
    # print('############################')
    # print('####### {} #########'.format(cf))
    # print('############################')
    #Create Blank County Polygons
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Creating Blank County Polygons')
    cf_Blank_Raster = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Blank.tif".format(cf)
    cf_Blank_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Blank\{}_Polygon.shp".format(cf)
    # arcpy.RasterToPolygon_conversion(cf_Blank_Raster, cf_Blank_Polygon, "NO_SIMPLIFY","VALUE") 
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created Blank County Polygons')
    # Create County StreamRivers Buffers #REDO
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Create  WV StreamRivers Clipped (1 minutes)')
    cf_StreamRiver_Buffer_PreClip = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\{}_StreamRiver_Buffer_PreClip.shp".format(cf)
    # arcpy.PairwiseClip_analysis(StreamRiver_Buffer,cf_Blank_Polygon,cf_StreamRiver_Buffer_PreClip)
    cf_StreamRiver_Buffer = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\{}_StreamRiver_Buffer.shp".format(cf)
    # arcpy.PairwiseClip_analysis(cf_StreamRiver_Buffer_PreClip,Filled_TCWetland_Polygon,cf_StreamRiver_Buffer)
    wv_StreamRiver_Buffer_list.append(cf_StreamRiver_Buffer)
    # t = time.localtime()
    # current_time = time.strftime("%H:%M:%S",t)
    # print(current_time,' Created VA StreamRivers Clipped Singlepart')
#Merge County Stream Buffer Polygons
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merge County Stream Buffer Polygons (1 minute)')
Merged_WV_StreamBuffer_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV.gdb\Merged_WV_StreamBuffer"
# arcpy.management.Merge(wv_StreamRiver_Buffer_list, Merged_WV_StreamBuffer_Polygon)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Merged Forest Polygons')
#Create WV Stream Buffer Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create WV StreamRivers Buffer Singlepart (10 minutes)')
WV_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Buffer_Singlepart.shp"
# arcpy.PairwiseDissolve_analysis(Merged_WV_StreamBuffer_Polygon, WV_StreamRiver_Buffer_Singlepart, "", "", "SINGLE_PART")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created WV StreamRivers Buffer Singlepart')
# Summarize Within WV Priority Parcels for Streams
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for Streams (1 minutes)')
WV_Parcels_SW_Streams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_Parcels_SW_Streams.shp"
# arcpy.gapro.SummarizeWithin(StreamRivers, WV_Parcels_SW_Streams, "POLYGON", '', None, WV_Priority_Parcels, "ADD_SUMMARY", "MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for Buffered Stream Area (1 minutes)')
# Summarize Within WV Priority Parcels for Buffered Streams
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for Buffered Streams (1 minutes)')
WV_Parcels_SW_BuffStreams = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_Parcels_SW_BuffStreams.shp"
# arcpy.gapro.SummarizeWithin(WV_StreamRiver_Buffer_Singlepart, WV_Parcels_SW_BuffStreams, "POLYGON", '', None, WV_Priority_Parcels, "ADD_SUMMARY", "SQUARE_MILES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for Streams (1 minutes)')
#Join Stream Mile and Buffered Stream Area field back to WV Priority Parcels and Create Stream Buffer Ratio
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Stream Mile and Buffered Stream Area field back to WV Priority Parcels (1 minutes)')
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Parcels_SW_Streams, "UID",["sum_length"])
# arcpy.AddField_management(WV_Priority_Parcels, "Stream_M", "FLOAT")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Stream_M", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Stream_M", "!sum_length!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["sum_length"])
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Parcels_SW_BuffStreams, "UID",["sum_area_s"])
# arcpy.AddField_management(WV_Priority_Parcels, "BuffS_Area", "FLOAT")
# arcpy.CalculateField_management(WV_Priority_Parcels, "BuffS_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "BuffS_Area", "!sum_area_s!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["sum_area_s"])
# arcpy.AddField_management(WV_Priority_Parcels, "SB_Ratio", "FLOAT")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB_Ratio", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB_Ratio", "(!BuffS_Area! * !Stream_M!) / 0.038", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Stream Mile and Buffered Stream Area field back to WV Priority Parcels')
#Create SB attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Stream Buffer attribute (1 minutes)')
# arcpy.AddField_management(WV_Priority_Parcels, "SB1", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB1", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB1", "!SB_Ratio! >= 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "SB2", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB2", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB2", "!SB_Ratio! > 0.010495", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "SB3", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB3", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB3", "!SB_Ratio! > 0.048996", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "SB4", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB4", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB4", "!SB_Ratio! > 0.127791", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "SB5", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB5", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB5", "!SB_Ratio! > 0.347993", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "SB", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "SB", "!SB1! + !SB2! + !SB3! + !SB4! + !SB5!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["SB1"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["SB2"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["SB3"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["SB4"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["SB5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Stream Buffer attribute')
#Create Parcel Size attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Parcel Size attribute (1 minutes)')
# arcpy.AddField_management(WV_Priority_Parcels, "PS1", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS1", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS1", "!Acreage! >= 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "PS2", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS2", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS2", "!Acreage! >= 75", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "PS3", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS3", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS3", "!Acreage! >= 100", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "PS4", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS4", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS4", "!Acreage! >= 125", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "PS5", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS5", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS5", "!Acreage! > 150", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "PS", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "PS", "!PS1! + !PS2! + !PS3! + !PS4! + !PS5!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PS1"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PS2"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PS3"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PS4"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["PS5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Parcel Size attribute (1 minutes)')
# Summarize Within WV Priority Parcels for Forest Hubs (No Wetland Hubs in WV study area could be different in WV)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarize Within WV Priority Parcels for Hubs (1 minutes)')
VAWV_Forest_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Hubs.shp"
WV_Parcels_SW_Hubs = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\WV_Parcels_SW_Hubs.shp"
# arcpy.gapro.SummarizeWithin(VAWV_Forest_Hubs, WV_Parcels_SW_Hubs, "POLYGON", '', None, WV_Priority_Parcels, "ADD_SUMMARY", "ACRES", None, None, None, "NO_MIN_MAJ", None, None)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Summarized Within WV Priority Parcels for Hubs')
#Join Hub Area field back to WV Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Join Hub Area field back to WV Priority Parcels (1 minutes)')
# arcpy.JoinField_management(WV_Priority_Parcels, "UID", WV_Parcels_SW_Hubs, "UID",["sum_area_a"])
# arcpy.AddField_management(WV_Priority_Parcels, "Hub_Area", "FLOAT")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub_Area", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub_Area", "!sum_area_a!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["sum_area_a"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Joined Hub Area field back to WV Priority Parcels')
#Create Hub attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Hub attribute (1 minutes)')
# arcpy.AddField_management(WV_Priority_Parcels, "Hub1", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub1", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub1", "!Hub_Area! >= 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "Hub2", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub2", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub2", "!Hub_Area! > 0", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "Hub3", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub3", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub3", "!Hub_Area! > 10", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "Hub4", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub4", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub4", "!Hub_Area! > 30", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "Hub5", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub5", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub5", "!Hub_Area! > 50", "PYTHON3")
# arcpy.AddField_management(WV_Priority_Parcels, "Hub", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub", "0", "PYTHON3")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Hub", "!Hub1! + !Hub2! + !Hub3! + !Hub4! + !Hub5!", "PYTHON3")
# arcpy.DeleteField_management(WV_Priority_Parcels, ["Hub1"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["Hub2"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["Hub3"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["Hub4"])
# arcpy.DeleteField_management(WV_Priority_Parcels, ["Hub5"])
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Hub attribute')
#Create Priority Attribute
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Create Priority attribute (1 minutes)')
# arcpy.AddField_management(WV_Priority_Parcels, "Score", "LONG")
# arcpy.CalculateField_management(WV_Priority_Parcels, "Score", "(!TNC! * 5) + !Hub! + !CBP_WQP! + !ICPRB_WQ! + !DevV! + !SB! + !Adj_PL! + !Adj_T! + (!Historic! * 5) + !PS! + !SVI_US!", "PYTHON3")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Created Priority attribute (1 minutes)')




#WEB PUBLISHING
#Project MD Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD Priority Parcels (14 seconds)')
MD_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\MD\MD_Priority_Parcels.shp"
MD_Priority_Parcels_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\MD_Priority_Parcels"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(MD_Priority_Parcels, MD_Priority_Parcels_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD Priority Parcels')
#Project US SVI MD
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project US SVI MD Desired Counties (14 seconds)')
US_SVI_MD_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_MD_Desired_Counties.shp"
US_SVI_MD_Desired_Counties_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\US_SVI_MD_Desired_Counties"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(US_SVI_MD_Desired_Counties, US_SVI_MD_Desired_Counties_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD SVI Desired Counties')
#Project National Historic Landmarks
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project National Historic Landmarks (14 seconds)')
National_Historic_Landmarks_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\National_Historic_Landmarks_Projected.shp"
National_Historic_Landmark_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\National_Historic_Landmarks"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(National_Historic_Landmarks_Projected, National_Historic_Landmark_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected National Historic Landmarks')
#Project National Register of Historic Sites and Places (NRHP)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project National Historic Landmarks (14 seconds)')
NRHP_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Historic_Landmarks_and_Sites\NRHP_Projected.shp"
NRHP_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\NRHP"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(NRHP_Projected, NRHP_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected National Historic Landmarks')
#Project Baywide Trails
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Baywide Trails (14 seconds)')
Baywide_Trails_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Baywide Trails\Baywide_Trails_Proj.shp"
Baywide_Trails_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\Baywide_Trails"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(Baywide_Trails_Projected, Baywide_Trails_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Baywide Trails')
#Project StreamRivers
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project StreamRivers (14 seconds)')
StreamRivers = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\StreamRiver.shp"
StreamRivers_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\Streams_Rivers"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(StreamRivers, StreamRivers_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected StreamRivers')
#Project MD_StreamRiver_Buffer_Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD_StreamRiver_Buffer_Singlepart (14 seconds)')
MD_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Buffer_Singlepart.shp"
MD_StreamRiver_Buffer_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\MD_Buffered_Streams"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(MD_StreamRiver_Buffer_Singlepart, MD_StreamRiver_Buffer_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD_StreamRiver_Buffer_Singlepart')
#Project Water Quality Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project CBP Water Quality Raster (14 seconds)')
WQ_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\CBP_Water_Quality_Model_Data_2021.08.23\Water_Quality\wq_proj.tif"
WQ_Raster_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\CBP_WQP.tif"
# arcpy.management.ProjectRaster(WQ_Raster_Projected, WQ_Raster_Web, 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', "NEAREST", "36.73 36.73", "WGS_1984_(ITRF00)_To_NAD_1983", None, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Water Quality Raster')
#Project TNC Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project TNC Raster (14 seconds)')
TNC_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\TNC\TNC.tif"
TNC_Raster_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\TNC.tif"
# arcpy.management.ProjectRaster(TNC_Raster_Projected, TNC_Raster_Web, 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', "NEAREST", "36.73 36.73", "WGS_1984_(ITRF00)_To_NAD_1983", None, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected TNC Raster')
#Project Drinking Water Quality Raster
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project Drinking Water Quality Raster (14 seconds)')
DWQ_Raster_Projected = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\ICPRB_LandPrioritization_GIS_Package_received2021.11.09\DWQ.tif"
DWQ_Raster_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\ICPRB_DWQ.tif"
# arcpy.management.ProjectRaster(DWQ_Raster_Projected, DWQ_Raster_Web, 'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]', "NEAREST", "36.73 36.73", "WGS_1984_(ITRF00)_To_NAD_1983", None, 'PROJCS["USA_Contiguous_Albers_Equal_Area_Conic_USGS_version",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Albers"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-96.0],PARAMETER["Standard_Parallel_1",29.5],PARAMETER["Standard_Parallel_2",45.5],PARAMETER["Latitude_Of_Origin",23.0],UNIT["Meter",1.0]]', "NO_VERTICAL")
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected Drinking Water Quality Raster')
#Project MD_StreamRiver_Clipped_Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD_StreamRiver_Clipped_Singlepart (14 seconds)')
MD_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\MD_StreamRiver_Clipped_Singlepart.shp"
MD_StreamRiver_Clipped_Singlepart_Web = r"\\ccsvr01\d\GIS\_Web_Services\PotomacConservancy\WebData.gdb\Streams_Rivers_MD"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(MD_StreamRiver_Clipped_Singlepart, MD_StreamRiver_Clipped_Singlepart_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected MD_StreamRiver_Clipped_Singlepart')
#Project MD Forest Hubs
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project MD_Forest_Hub_Polygon (14 seconds)')
MD_Forest_Hub_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\Forest_Hubs.shp"
MD_Forest_Hub_Polygon_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\MD_Forest_Hubs"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(MD_Forest_Hub_Polygon, MD_Forest_Hub_Polygon_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA_StreamRiver_Clipped_Singlepart')
#Project VA Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project VA Priority Parcels (14 seconds)')
VA_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\VA\VA_Priority_Parcels.shp"
VA_Priority_Parcels_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\VA_Priority_Parcels"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(VA_Priority_Parcels, VA_Priority_Parcels_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA Priority Parcels')
#Project US SVI VA
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project US SVI VA Desired Counties (14 seconds)')
US_SVI_VA_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_VA_Desired_Counties.shp"
US_SVI_VA_Desired_Counties_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\US_SVI_VA_Desired_Counties"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(US_SVI_VA_Desired_Counties, US_SVI_VA_Desired_Counties_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA SVI Desired Counties')
#Project VA_StreamRiver_Clipped_Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project VA_StreamRiver_Clipped_Singlepart (14 seconds)')
VA_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Clipped_Singlepart.shp"
VA_StreamRiver_Clipped_Singlepart_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\Streams_Rivers_VA"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(VA_StreamRiver_Clipped_Singlepart, VA_StreamRiver_Clipped_Singlepart_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA_StreamRiver_Clipped_Singlepart')
#Project VA StreamRiver Buffer Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project VA StreamRiver Buffer Singlepart (14 seconds)')
VA_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\VA_StreamRiver_Buffer_Singlepart.shp"
VA_StreamRiver_Buffer_Singlepart_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\VA_StreamRiver_Buffer_Singlepart"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(VA_StreamRiver_Buffer_Singlepart, VA_StreamRiver_Buffer_Singlepart_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA StreamRiver Buffer Singlepart')
#Project VAWV Forest Hubs
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project VAWV_Forest_Hub_Polygon (14 seconds)')
VAWV_Forest_Hub_Polygon = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Hubs\VAWV\Forest_Hubs.shp"
VAWV_Forest_Hub_Polygon_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\VAWV_Forest_Hubs"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(VAWV_Forest_Hub_Polygon, VAWV_Forest_Hub_Polygon_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected VA_StreamRiver_Clipped_Singlepart')
#Project WV Priority Parcels
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project WV Priority Parcels (14 seconds)')
WV_Priority_Parcels = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Parcels\WV\WV_Priority_Parcels.shp"
WV_Priority_Parcels_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\WV_Priority_Parcels"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(WV_Priority_Parcels, WV_Priority_Parcels_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected WV Priority Parcels')
#Project US SVI WV
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project US SVI WV Desired Counties (14 seconds)')
US_SVI_WV_Desired_Counties = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\Equity_and_Inclusion\US_SVI_WV_Desired_Counties.shp"
US_SVI_WV_Desired_Counties_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\US_SVI_WV_Desired_Counties"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(US_SVI_WV_Desired_Counties, US_SVI_WV_Desired_Counties_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected WV SVI Desired Counties')
#Project WV_StreamRiver_Clipped_Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project WV_StreamRiver_Clipped_Singlepart (14 seconds)')
WV_StreamRiver_Clipped_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Clipped_Singlepart.shp"
WV_StreamRiver_Clipped_Singlepart_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\Streams_Rivers_WV"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(WV_StreamRiver_Clipped_Singlepart, WV_StreamRiver_Clipped_Singlepart_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected WV_StreamRiver_Clipped_Singlepart')
#Project WV StreamRiver Buffer Singlepart
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Project WV StreamRiver Buffer Singlepart (14 seconds)')
WV_StreamRiver_Buffer_Singlepart = r"C:\Users\kwalker\Desktop\Potomac_Conservancy\BufferedStreams\WV_StreamRiver_Buffer_Singlepart.shp"
WV_StreamRiver_Buffer_Singlepart_Web = r"Z:\GIS\_Web_Services\PotomacConservancy\WebData.gdb\WV_StreamRiver_Buffer_Singlepart"
# sr = arcpy.SpatialReference(text='PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Mercator_Auxiliary_Sphere"],PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')
# arcpy.Project_management(WV_StreamRiver_Buffer_Singlepart, WV_StreamRiver_Buffer_Singlepart_Web,sr)
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S",t)
# print(current_time,' Projected WV StreamRiver Buffer Singlepart')