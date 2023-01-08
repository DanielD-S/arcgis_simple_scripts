#Importar multiples kmz desde una misma carpeta a un archivo mxd
#Generar un archivo de salida .shp.gdb
#Considerar poligonos Z como archivo de salida

#importar librerias
import arcpy
import os

#Establecer ruta de trabajo (Carpeta donde estan nuestros archivos KMZ)

arcpy.env.workspace = r'D:\test\...'

#Listado archivos kmz

kmz_archivos = arcpy.ListFiles("*.kmz")

#Ruta de salida de archivos

out_workspace = r'D:\test\...'

#Ejecucion de iteracion 

for kmz in kmz_archivos:
    shp = os.path.splitext(kmz)[0]+".shp"
    #Transformacion archivos .kmz a .shp salida
    arcpy.KMLToLayer_conversion(kmz,out_workspace,shp)