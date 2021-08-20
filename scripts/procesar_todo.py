## COME-COORDENATAS EÓLICAS v0.1
## Script que procesa coordenadas en formato UTM e produce un ficheiro
## KML preparado para importar en mapas de google-maps

## INPUT: ficheiro de texto CSV:
## Valores separados por ;
## campos: nome;coord X;coord Y   (coordenadas UTM)
## as coordenadas teñen a parte enteira e decimal separada por ,

## OUTPUT: ficheiro KMZ no directorio ./output

import os
import sys
import csv
import re
import itertools
import simplekml
from pyproj import CRS, Transformer
from zipfile import ZipFile

#Introducir manualmente rango de filas para cada cosa. A la primera fila del
#rango hay que restarle una unidad. (seguro?)
#Rango Aerogeneradores
ai = 0
aj = 0
#Rango LAAT
li = 0
lj = 0
#Rango Poligonal parque
pi = 0
pj = 0
#Rango Poligonal subestacion
si = 0
sj = 0
#Rango Torres metereológicas
ti = 0
tj = 0

if (len(sys.argv)!=2):
    print("Tes que indicar o nome do ficheiro CSV ou non vai funcionar!")
    exit(1)

nome_ficheiro = sys.argv[1]
ficheiro_temporal = "temp_"+nome_ficheiro
novo_ficheiro = nome_ficheiro[0:-3]+"kmz"

# Utilízase un ficheiro temporal onde se substitúen algúns caracteres
with open(nome_ficheiro, "r") as sources:
    lines = sources.readlines()
with open(ficheiro_temporal, "w") as sources:
    for line in lines:
        sources.write(re.sub(r',', '.', line))

with open(ficheiro_temporal, "r") as sources:
    lines = sources.readlines()
with open(ficheiro_temporal, "w") as sources:
    for line in lines:
        sources.write(re.sub(r';', ',', line))


inputfile = list(csv.reader(open(ficheiro_temporal,'r')))

kml=simplekml.Kml()

#establécense orixe e destino da transformación
trans = Transformer.from_crs("EPSG:25829","EPSG:4326",always_xy=True)

# POLIGONAL PARQUE
if(pi!=0):
    coordList1 = []
    for row in itertools.islice(inputfile, pi-1, pj):
            coordsSet1= trans.transform(row[1],row[2])
            coordList1.append(coordsSet1)
    coordList1.append(coordList1[0])
    #print(coordList1)

    pol = kml.newpolygon(name="Poligonal Parque")
    pol.outerboundaryis = coordList1
    pol.style.linestyle.color = simplekml.Color.rgb(255,82,82)
    pol.style.linestyle.width = 5
    pol.style.polystyle.color = simplekml.Color.changealphaint(50, simplekml.Color.rgb(255,82,82))

# POLIGONAL SUBESTACIÓN
if(si!=0):
    coordList2 = []
    for row in itertools.islice(inputfile, si-1, sj):
            coordsSet2= trans.transform(row[1],row[2])
            coordList2.append(coordsSet2)
    coordList2.append(coordList2[0])
    # print(coordList2)

    pol2 = kml.newpolygon(name="Poligonal Subestación")
    pol2.outerboundaryis = coordList2
    pol2.style.linestyle.color = simplekml.Color.rgb(255,234,0)
    pol2.style.linestyle.width = 2
    pol2.style.polystyle.color = simplekml.Color.changealphaint(100, simplekml.Color.rgb(255,234,0))

# AEROXENERADORES MODELO 3D
if(ai!=0):
    for row in itertools.islice(inputfile, ai-1, aj):
        modelLink = simplekml.Link(href = "untitled.dae")
        coordsSet= trans.transform(row[1],row[2])
        coords = simplekml.Location(longitude=coordsSet[0], latitude=coordsSet[1], altitude=0)
        model = kml.newmodel(name=row[0],description='aeroxenerador',altitudemode='relativeToGround', location=coords, link=modelLink)
        model.style.iconstyle.icon.href = "molino.png" # icono para gmaps

# TORRE METEOROLÓGICA
if(ti!=0):
    for row in itertools.islice(inputfile, ti-1, tj):
        pnt = kml.newpoint(name=row[0], coords=[trans.transform(row[1],row[2])])
        pnt.style.iconstyle.scale = 0.8  # Icon thrice as big
        pnt.style.iconstyle.icon.href = "torremet.png"

# LINEA LAAT
if(li!=0):
    coordListLAAT = []
    for row in itertools.islice(inputfile, li-1, lj):
        coordsSetLAAT= trans.transform(row[1],row[2])
        coordListLAAT.append(coordsSetLAAT)
        #Puntos
        laatpnt = kml.newpoint(name=row[0])
        laatpnt.coords = [coordsSetLAAT]
        laatpnt.style.iconstyle.scale = 0.7
        laatpnt.style.iconstyle.icon.href = "laat.png"

    #Línea
    lin = kml.newlinestring(name="LAAT", description="Linea Aerea Alta Tensión", coords=coordListLAAT)
    lin.style.linestyle.color = simplekml.Color.rgb(2,136,209)
    lin.style.linestyle.width= 5  # 5 pixels

#garda o ficheiro
kml.save('doc.kml')

# create a ZipFile object
zipObj = ZipFile('output/'+novo_ficheiro, 'w')
# Add multiple files to the zip
zipObj.write('doc.kml')
zipObj.write('molino.png')
zipObj.write('torremet.png')
zipObj.write('laat.png')
zipObj.write('untitled.dae')
# close the Zip File
zipObj.close()

#elimina ficheiros temporais
os.remove('doc.kml')
os.remove(ficheiro_temporal)
