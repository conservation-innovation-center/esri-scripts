#### Clip Raster By Rows Of Vector
#### Colin Stief
#### 9/20/17
#### Loops through the rows of a vector file, creates a temporary feature of the current shape,
####   clips the raster dataset, and stores the output in a new folder, named after the row
####   Used in favor of 'Split' (http://desktop.arcgis.com/en/arcmap/10.3/tools/analysis-toolbox/split.htm)
####   because I wanted more control over the output name and location

import arcpy
import os

## Define raster
landcover = r'\\CCSVR01\NorthWalk\LandCover\BaywideDataset_12Classes\BaywideData12Classes.gdb\BaywideLandCover'

## Can't select from a file you're looping through (I think, I can't really remember though... either way, this works too)
## So define the file to loop through, then create a distinct layer to select from
huc12_looper = r'\\Ccsvr01\d\GIS\Envision_the_Susquehanna_NFWF\_Data\Susquehanna_HUC12.shp'
huc12_selection = arcpy.MakeFeatureLayer_management(huc12_looper, "huc12_selection")

## Grab the actual layer object so we can get the extent to limit the processing
## I tried to use .getSelectedExtent() on the huc12_selection variable I created, 
## but it's a Result object, not a Layer ovject, so it doesn't have that method
mxd = arcpy.mapping.MapDocument(r'\\Ccsvr01\d\GIS\Envision_the_Susquehanna_NFWF\Analysis\Chop_LC_Flowpaths\ChopLC.mxd')
df = arcpy.mapping.ListDataFrames(mxd)[0]
for layer in arcpy.mapping.ListLayers(mxd, '', df):
    if layer.name == 'huc12_selection':
        hucs = layer

## Set environments
arcpy.env.cellSize = 1
arcpy.env.snapRaster = landcover
arcpy.env.compression = 'LZ77'

## Loop through HUC12s
with arcpy.da.SearchCursor(huc12_looper, ['HUC12']) as cursor:
    for row in cursor:

        ## Check for HUC12 directory, and create it if it doesn't exist
        directory = os.path.join(r'C:\Users\CStief\Desktop\SusHucs', 'HUC_' + row[0])
        if not os.path.isdir(directory):
            os.makedirs(directory)

        ## Select a single HUC12
        sql = '"HUC12" = ' + "'" + row[0] + "'"
        print("Starting: ", sql)
        arcpy.SelectLayerByAttribute_management(huc12_selection, 'NEW_SELECTION', sql)

        ## Create feature in_memory to use for the clip
        memoryFeature = "in_memory" + "\\" + "huc_" + row[0]
        arcpy.CopyFeatures_management(huc12_selection, memoryFeature)

        ## Define output name and path
        name = 'LC_' + row[0] + '.tif'
        outputPath = os.path.join(directory, name)

        ## Clip with selected layer
        arcpy.Clip_management(landcover, '#', outputPath, memoryFeature, 'NoData', 'ClippingGeometry')

        ## Clean up in_memory
        arcpy.Delete_management("in_memory")
