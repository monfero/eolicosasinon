## COME-COORDENATAS EÓLICAS v0.1
## Script que procesa coordenadas en formato UTM e produce un ficheiro
## KML preparado para importar en mapas de google-maps

## INPUT: ficheiro de texto CSV:
## Valores separados por ;
## campos: nome;coord X;coord Y   (coordenadas UTM)
## as coordenadas teñen a parte enteira e decimal separada por ,

## OUTPUT: ficheiro KML

import sys
import csv
import re
import simplekml
from pyproj import CRS, Transformer

if (len(sys.argv)!=2):
    print("Tes que indicar o nome do ficheiro CSV ou non vai funcionar!")
    exit(1)

nome_ficheiro = sys.argv[1]
novo_ficheiro = nome_ficheiro[0:-3]+"kml"

# a quite strange way to modify the CSV source
# cambianse as comas por puntos
# despois cambianse os punto-e-coma por comas
with open(nome_ficheiro, "r") as sources:
    lines = sources.readlines()
with open(nome_ficheiro, "w") as sources:
    for line in lines:
        sources.write(re.sub(r',', '.', line))

with open(nome_ficheiro, "r") as sources:
    lines = sources.readlines()
with open(nome_ficheiro, "w") as sources:
    for line in lines:
        sources.write(re.sub(r';', ',', line))


inputfile = csv.reader(open(nome_ficheiro,'r'))
kml=simplekml.Kml()

#establécese orixe e destino da transformación
trans = Transformer.from_crs("EPSG:25829","EPSG:4326",always_xy=True)

#para cada liña de datos do ficheiro crea un novo punto
for row in inputfile:
    kml.newpoint(name=row[0], coords=[trans.transform(row[1],row[2])])

#garda o ficheiro
kml.save(novo_ficheiro)
