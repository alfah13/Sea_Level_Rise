Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import arcpy

#imp-geoprocessing
from arcpy import env

#imp-spatial analyst
from arcpy.sa import *

#checkifextension is ON
print("your spatial package is" + ' ... ' +  arcpy.CheckOutExtension("Spatial"))


#setup wd
env.workspace = "C:\Users\MTA78\Desktop\GIS"

# Set input raster
inRaster = Raster("Water_Depth_Raster.tif")

#make dictionary of depth of water increase
DepthIncrease = {'2022':0.2,'2027':0.5,'2032':0.9, '2037':1.4, '2042':2.0, 
'2047':2.7, '2052':3.5, '2057':4.4, '2062':5.4, '2067':6.5}

#output Raster for each year 
WaterDepth2022 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2022"]
WaterDepth2027 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2027"]
WaterDepth2032 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2032"]
WaterDepth2037 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2037"]
WaterDepth2042 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2042"]
WaterDepth2047 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2047"]
WaterDepth2052 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2052"]
WaterDepth2057 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2057"]
WaterDepth2062 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2062"]
WaterDepth2067 = Raster("Water_Depth_Raster.tif")+DepthIncrease["2067"]

WaterDepth2022.save('2022')
WaterDepth2027.save('2027')
WaterDepth2032.save('2032')
WaterDepth2037.save('2037')
WaterDepth2042.save('2042')
WaterDepth2047.save('2047')
WaterDepth2052.save('2052')
WaterDepth2057.save('2057')
WaterDepth2062.save('2062')
WaterDepth2067.save('2067')
