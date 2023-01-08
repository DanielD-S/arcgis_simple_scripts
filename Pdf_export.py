#NOTA: Script para exportar multiples archivos PDF desde diferentes
#archivos mxd que esten en la misma carpeta.
#

###########################################3
#importar librerias
import arcpy
import os

#Configuracion ruta de trabajo (donde se encuentran los archivos mxd)
arcpy.env.workspace = r'D:\test\...'

#Lista archivos mxd

list_mxd = arcpy.ListFiles('*.mxd')

#Iteracion de proceso archivo mxd

for mxd_archivo in list_mxd:
    mxd = arcpy.mapping.MapDocument(mxd_archivo)
    #Nombre archivo pdf salida
    pdf_file = mxd_archivo[:-4]+'.pdf'
    #Eliminacion de duplicados archivos PDF
    if os.path.exists(pdf_file):
        os.remove(pdf_file)

     #Exportar a PDF
     arcpy.mapping.ExportToPDF(mxd,pdf_file)
     del mxd