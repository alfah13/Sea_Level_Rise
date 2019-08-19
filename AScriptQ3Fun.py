import arcpy

#imp-geoprocessing
from arcpy import env

#imp-spatial analyst
from arcpy.sa import *

#checkifextension is ON then tell user
print("your spatial package is" + ' ... ' +  arcpy.CheckOutExtension("Spatial"))


#setup wd [***NEED TO BE EDITED BY USER***]
env.workspace = "C:\Users\MTA78\Desktop\GIS"

# Set input raster [***NEED TO BE EDITED BY USER***]
inRaster = Raster("Water_Depth_Raster.tif")

#this works but output is not labeled by year
#and the output is temp saved in default gtb 
#List HAS TO BE IN ORDER
#Iterations will happen in order of input values

List = [0.2,0.5,0.9,1.4,2.0,2.7,3.5,4.4,5.4,6.5]

WaterDepth = [Raster("Water_Depth_Raster.tif") + (i) for i in List]

WaterDepth[1].save('2022')
WaterDepth[2].save('2027')
WaterDepth[3].save('2032')
WaterDepth[4].save('2037')
WaterDepth[5].save('2042')
WaterDepth[6].save('2047')
WaterDepth[7].save('2052')
WaterDepth[8].save('2057')
WaterDepth[9].save('2062')
WaterDepth[10].save('2067')

