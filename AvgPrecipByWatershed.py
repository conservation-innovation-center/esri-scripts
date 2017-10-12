"""
Average precipitation in watershed zones
Colin
October 12, 2017

This script loops through a directory of precipitation rasters, calculates zonal statistics (mean)
of watersheds in a shapefile, then appends that information to the shapefile.

Important note: This is meant to be used within an ArcGIS Toolbox, with appropriate parameters setup:

1. Precipitation Raster Folder (Type: Folder)
2. Effective watersheds (Type: Feature Layer) <-- Using 'Feature Layer' allows us to drag and drop from table of contents
3. Zone field (Type: Field) <-- If you setup the 'Obtained from' property to be the 'Effective watersheds', it can pre-populate this as a drop down
4. Raster for snapping (Type: Raster Layer) <-- ditto #2

"""
## Start timer
import os, sys, timeit
start = timeit.default_timer()

## This def main() thing looks weird, but it's totally normal and very helpful.
##
## It allows you to define helper functions below the main script, getting things out of the way.
##   In Python, if you reach a line in the script the calls a helper function that has not
##   been defined yet, it throws an error -- order matters. But that sucks, because I want my important
##   things up top, and my extra stuff down below. To solve this, we can structure our script in the following way:
## 
## def main():
##    Important tasks to complete!
##   
## def helperFunctionOne():
##    Extra stuff
##
## def helperFunctionTwo():
##    More extra stuff
##
## if __name__ == '__main__':
##     main()
##

## As a side note, there are lots of reasons to use this structure (more important than the above) but not too relevant for us
## https://stackoverflow.com/questions/4041238/why-use-def-main

def main():
    ## Packages
    ## Find out mor about try/except blocks here: https://stackoverflow.com/questions/730764/try-except-in-python-how-do-you-properly-ignore-exceptions
    try:
        import arcpy
        import pandas
        arcpy.AddMessage('Libraries imported')

    except:
        arcpy.AddMessage('Could not import necessary libraries')
        sys.exit()

    ## Extensions
    arcpy.CheckOutExtension("spatial")

    ## Parameters
    ## Find out more here: http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/accessing-parameters-in-a-script-tool.htm
    precipRasterDirectory = arcpy.GetParameterAsText(0)
    watersheds = arcpy.GetParameterAsText(1)
    zoneField = arcpy.GetParameterAsText(2)
    snapRaster = arcpy.GetParameterAsText(3)

    ## Environments
    arcpy.env.cellSize = snapRaster
    arcpy.env.snapRaster = snapRaster
    arcpy.env.outputCoordinateSystem =snapRaster
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = precipRasterDirectory

    ## Add square meters area field to effective watersheds
    arcpy.AddMessage('Adding geometry fields')
    arcpy.AddGeometryAttributes_management(watersheds, "AREA", "", "SQUARE_METERS")

    ## Grab list of fields for later on
    watershedFields = arcpy.ListFields(watersheds)

    ## Get list of rasters and loop through them
    precipRasters = arcpy.ListRasters('*', 'TIF')
    for raster in precipRasters:

        ## Get 3 character capitalized month abbreviation
        month = getMonth(raster)
        arcpy.AddMessage('Starting: {0}'.format(month)) ## Weird format, but very handy. Find out more here: https://pyformat.info/

        ## Zonal statistics (mean) on watersheds; output is an in_memory table
        ## Find out more about in_memory here: https://gis.stackexchange.com/questions/35468/what-is-the-proper-syntax-and-usage-for-arcgis-in-memory-workspace
        arcpy.AddMessage('Calculating zonal statistics')
        precipTable = arcpy.sa.ZonalStatisticsAsTable(watersheds, zoneField, raster, 'in_memory/myNewTable', 'DATA', 'MEAN')

        ## Change field name within output table to the current month
        arcpy.AddMessage('Renaming field')
        arcpy.AlterField_management(precipTable, 'MEAN', month)

        ## Check if field already exists... delete it if it does
        arcpy.AddMessage('Checking if field already exists')
        for field in watershedFields:
            if field.name == month:
                arcpy.AddMessage('Deleting existing field')
                arcpy.DeleteField_management(watersheds, [month])

        ## Permanently join the mean field from precip table on to the watersheds 
        arcpy.AddMessage('Joining field to watershed table')
        arcpy.JoinField_management(watersheds, zoneField, precipTable, zoneField, month)

        ## Multiply the new field by area
        arcpy.AddMessage('Getting total precip of watershed based on mean')
        arcpy.CalculateField_management(watersheds, month, '!POLY_AREA!*!{0}!'.format(month), "PYTHON_9.3")

        arcpy.Delete_management("in_memory")

    arcpy.CheckInExtension("spatial")
    arcpy.AddMessage(getFinalTime())

def getMonth(name):
    if 'm01' in name:
        return 'JAN'
    elif 'm02' in name:
        return 'FEB'
    elif 'm03' in name:
        return 'MAR'
    elif 'm04' in name:
        return 'APR'
    elif 'm05' in name:
        return 'MAY'
    elif 'm06' in name:
        return 'JUN'
    elif 'm07' in name:
        return 'JUL'
    elif 'm08' in name:
        return 'AUG'
    elif 'm09' in name:
        return 'SEP'
    elif 'm10' in name:
        return 'OCT'
    elif 'm11' in name:
        return 'NOV'
    elif 'm12' in name:
        return 'DEC'

def getFinalTime():
    stop = timeit.default_timer()
    total_time = stop - start
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    return 'Total running time: {0} hours, {1} minutes, {2} seconds'.format(hours, mins, round(secs, 2))

if __name__ == '__main__':
    main()