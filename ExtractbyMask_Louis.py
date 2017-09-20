#This script performs extract by mask tool for a number of files, matching mask files in one folder with image files in another folder.  
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

arcpy.env.overwriteOutput = True

#Set local variables for mask folder and raster folder
water_ws = "H:/VEE_data/Analysis/HUC10_Water_network"
mask_ws = "H:/VEE_data/Analysis/HUC10_filled"

#for loop to loop through all file pairs
for i in range (0, 46):
    #set input rasters
    water_raster = "H:/VEE_data/Analysis/HUC10_Water_network/Water_network_%s_fill.tif" %(i)
    mask_raster = "H:/VEE_data/Analysis/HUC10_filled/%s_fill.tif" %(i)

    # Execute ExtractByMask
    outExtractByMask = arcpy.sa.ExtractByMask(water_raster, mask_raster)

    # Save the output
    outExtractByMask.save("H:/VEE_data/Analysis/HUC10_Water_network/ExtractbyMask/Clip_WaterNetwork_%s.tif") %(i)

    print(water_raster)
print ('Done processing')