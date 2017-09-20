## This script is an example from the change detection project.
##It loops through a list of paired binary change rasters for a range of years
##and calculates overlap between rasters from an algorithm result (LandTrendr here) and
##rasters from a reference dataset (Impervious surface gain here). It does a straight overlap
##and a fuzzy overlap: +/- 1 year = good enough to call accurate.

##Emily Mills 9/20/17


##throughout this script you'll see one or more "%s" followed by "% ()"
#this is a nice shortcut for string formatting.
# see further documentation at the link below, which includes all kinds of good python formatting tips
# not limited to strings:
#https://pyformat.info/

## Import modules
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

##Set environment setting to overwrite existing outputs
arcpy.env.overwriteOutput = True


##Set workspaces.
#in_ws is where the algorithm binary change rasters are located
in_ws = "X:/GIS/CBP_Change_Detection/_Data/LandTrendr/OvlpGFCKeep"
#set out_ws to where you want overlap rasters to be saved
out_ws = "X:/GIS/CBP_Change_Detection/_Data/LandTrendr/OvlpImp"
#set fuzzy_ws to where you want fuzzy overlap rasters to be saved
fuzzy_ws = "X:/GIS/CBP_Change_Detection/_Data/LandTrendr/OvlpImp/fuzzy"
#set imp_ws to where the reference data set binary change rasters are located
imp_ws = "X:/GIS/CBP_Change_Detection/_Data/Impervious/ImpFiltered"


##overlap (not fuzzy)
#for loop that matches impervious raster (labeled 2-25) with LandTrendr raster (labeled 1985-2008),
#adds them together and saves the output in regular overlap workspace (out_ws)
for yr in range(2, 26):
    in_raster = "%s/PGimpgain%s.tif" % (imp_ws, yr)
    lyr = yr + 1983
    ldtr_raster = "%s/%sbin.tif" % (in_ws, lyr)

    ovlp_raster = (Raster(in_raster) + Raster(ldtr_raster))
    ovlp_name = "%s/ldtr_imp_ovlp%s.tif" % (out_ws, lyr)
    ovlp_raster.save(ovlp_name)


##ovlp fuzzy
#for loop that takes each raster layer (besides first and last) and combines with rasters from
#+/- 1yr to create a fuzzy composite layer.
for n in range(1986, 2008):
    yr= n
    pyr= n+1
    myr= n-1

    in_raster = "%s/%sbin.tif" %(in_ws, yr)
    p_one = "%s/%sbin.tif" %(in_ws, pyr)
    m_one = "%s/%sbin.tif" %(in_ws, myr)

    out_raster = Con(Raster(in_raster)+ Raster(p_one) + Raster(m_one) >= 1, 1, 0)
    out_raster_name = "%s/%s.tif" %(fuzzy_ws, yr)
    out_raster.save(out_raster_name)

##do beginning yr separately
#beginning yr will just be combined with the +1 yr raster
beginyr = 1985
pyr = 1986

in_raster = "%s/%sbin.tif" %(in_ws, beginyr) 
p_one = "%s/%sbin.tif" %(in_ws, pyr)

out_raster = Con(Raster(in_raster)+ Raster(p_one) >= 1, 1, 0)
out_raster.save("%s/%s.tif" %(fuzzy_ws, beginyr))

##do end yr separately
#end yr will just be combined with the -1 yr raster

endyr = 2008
myr = 2007

in_raster = "%s/%sbin.tif" %(in_ws, endyr) 
m_one = "%s/%sbin.tif" %(in_ws, myr)

out_raster = Con(Raster(in_raster)+ Raster(m_one) >= 1, 1, 0)
out_raster.save("%s/%s.tif" %(fuzzy_ws, endyr))


##fuzzy overlap
#for loop that matches impervious raster (labeled 2-25) with fuzzy binary change (+/- 1yr)LandTrendr raster
#(labeled 1985-2008), adds them together and saves the output in the fuzzy workspace
for n in range(1985, 2009):
    term = n-1983
    in_imp = "%s/PGimpgain%s.tif" %(imp_ws, term)
    in_LD = "%s/%s.tif" %(fuzzy_ws, n)

    out_raster = Raster(in_imp) + Raster(in_LD)
    out_raster_name = "%s/%s_fuzzyovlp.tif" % (fuzzy_ws, n)
    out_raster.save(out_raster_name)

