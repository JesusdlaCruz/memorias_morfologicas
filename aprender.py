import os
import json
from imagenes import imagen_como_arreglo
from memorias import memoria_max
from memorias import memoria_min

# Crea objetos para las memorias morfologicas de tipo max y min
memmax = memoria_max()
memmin = memoria_min()

ruta_raiz = os.path.dirname(os.path.realpath(__file__))
carpeta_entradas = os.path.join(ruta_raiz, 'img') # Nombre de la carpeta que contiene las imagenes que aprenderán las memorias
json_memmax = os.path.join(ruta_raiz,'memmax.json')
json_memmin = os.path.join(ruta_raiz,'memmin.json')

lista_imagenes = os.listdir(carpeta_entradas)

for im in lista_imagenes:  # Aprende todas las imagenes en la carpeta indicada
    x = imagen_como_arreglo(os.path.join(carpeta_entradas,im))
    memmax.aprender(x)
    memmin.aprender(x)

# Guarda las matrices de memoria en un archivo
with open(json_memmax,'w') as mmax:
    json.dump(memmax.M, mmax)

with open(json_memmin,'w') as mmin:
    json.dump(memmin.W, mmin)

