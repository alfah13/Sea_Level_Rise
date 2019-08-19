import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.env.overwriteOutput = True

#PLEASE DEFINE WORKSPACE
#[***NEED TO BE EDITED BY USER***]
env.workspace = "C:\Users\MTA78\Desktop\GIS"

#PLEASE DEFINE SHP VECTOR FOR PROPERTY EXTENTS
#[***NEED TO BE EDITED BY USER***]
Vector = "south_florida_properties_samp.shp"

#NO NEED TO EDIT
Zonefield = "LOT"

#PLEASE DEFINE Q1Z name and make sure it is located in defaul
#workspace (this is the output of question 1)
#[***NEED TO BE EDITED BY USER***]
Q1z = "ZonalSt_shp2"

arcpy.env.overwriteOutput = True

#getting zonal stats of all rasters, this creates "ot = output tables".
ZST17 = ZonalStatisticsAsTable(Vector,Zonefield,"Water_Depth_Raster.tif","ot17","NODATA","MAXIMUM")
ZST22 = ZonalStatisticsAsTable(Vector,Zonefield,"2022","ot22","NODATA","MAXIMUM")
ZST27 = ZonalStatisticsAsTable(Vector,Zonefield,"2027","ot27","NODATA","MAXIMUM")
ZST32 = ZonalStatisticsAsTable(Vector,Zonefield,"2032","ot32","NODATA","MAXIMUM")
ZST37 = ZonalStatisticsAsTable(Vector,Zonefield,"2037","ot37","NODATA","MAXIMUM")
ZST42 = ZonalStatisticsAsTable(Vector,Zonefield,"2037","ot42","NODATA","MAXIMUM")
ZST47 = ZonalStatisticsAsTable(Vector,Zonefield,"2047","ot47","NODATA","MAXIMUM")
ZST52 = ZonalStatisticsAsTable(Vector,Zonefield,"2052","ot52","NODATA","MAXIMUM")
ZST57 = ZonalStatisticsAsTable(Vector,Zonefield,"2057","ot57","NODATA","MAXIMUM")
ZST62 = ZonalStatisticsAsTable(Vector,Zonefield,"2062","ot62","NODATA","MAXIMUM")
ZST67 = ZonalStatisticsAsTable(Vector,Zonefield,"2067","ot67","NODATA","MAXIMUM")

#joining all the tables into ot17
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot22", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot27", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot32", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot37", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot42", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot47", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot52", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot57", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot62", join_field="LOT", fields="MAX")
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table="ot67", join_field="LOT", fields="MAX")

#joining the zonalstats from q1
arcpy.JoinField_management(in_data="ot17", in_field="LOT", 
join_table=Q1z, join_field="LOT", fields="MAX")

#adding field for Max elev data
arcpy.AddField_management("ot17","DEPT2017","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2022","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2027","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2032","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2037","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2042","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2047","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2052","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2057","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2062","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPT2067","DOUBLE","10","5","5")
arcpy.AddField_management("ot17","DEPTZERO","DOUBLE","10","5","5")

#moving the data from obscurely named columns to columns by year
arcpy.CalculateField_management(in_table="ot17", field="DEPT2017", expression="[MAX]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2022", expression="[MAX_1]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2027", expression="[MAX_12]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2032", expression="[MAX_12_13]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2037", expression="[MAX_12_13_14]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2042", expression="[MAX_12_13_14_15]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2047", expression="[MAX_12_13_14__16]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2052", expression="[MAX_12_13_14__17]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2057", expression="[MAX_12_13_14__18]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2062", expression="[MAX_12_13_14__19]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPT2067", expression="[MAX_12_13_14__20]", expression_type="VB", code_block="")
arcpy.CalculateField_management(in_table="ot17", field="DEPTZERO", expression="[MAX_12_13_14__21]", expression_type="VB", code_block="")

arcpy.TableToTable_conversion("ot17",env.workspace, "mastertable.dbf")
arcpy.TableToExcel_conversion("mastertable","master.xls")
