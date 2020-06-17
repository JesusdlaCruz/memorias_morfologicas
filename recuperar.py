import os
import json
from imagenes import arreglo_a_imagen
from imagenes import imagen_como_arreglo
from memorias import memoria_max
from memorias import memoria_min

ruta_raiz = os.path.dirname(os.path.realpath(__file__))
carpeta_max = os.path.join(ruta_raiz, 'salida_max')
carpeta_min = os.path.join(ruta_raiz, 'salida_min')
carpeta_entradas = os.path.join(ruta_raiz, 'img_recuperacion')
json_memmax = os.path.join(ruta_raiz,'memmax.json')
json_memmin = os.path.join(ruta_raiz,'memmin.json')
lista_entradas = os.listdir(carpeta_entradas)

memmax = memoria_max()
memmin = memoria_min()

memmax.cargar_matriz(json_memmax)
memmin.cargar_matriz(json_memmin)

for im in lista_entradas:
    print(os.path.join(carpeta_entradas,im))
    #Abre imagen como arreglo
    X = imagen_como_arreglo(os.path.join(carpeta_entradas,im))

    #Obtiene salida de las memorias
    Ymax = memmax.recuperar(X)
    Ymin = memmin.recuperar(X)

    # Guarda las imagenes de salida en la carpeta correspondiente para cada memoria
    arreglo_a_imagen(Ymax, os.path.join(carpeta_max,im))
    arreglo_a_imagen(Ymin, os.path.join(carpeta_min,im))