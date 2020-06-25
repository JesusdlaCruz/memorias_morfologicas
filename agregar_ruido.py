import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import os
def agregar_ruido(ruta):
    imagen = cv2.imread(ruta)

    rows, columns, chanel = imagen.shape
    p = 0.2
    output = np.zeros(imagen.shape, np.uint8)

    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2:
                output[i][j] = [0,0,0]
            elif r < p:
                output[i][j] = [0,0,0]
            else:
                output[i][j] = imagen[i][j]

    plt.imshow(output)
    plt.title("Imagen distorcionada")
    plt.show()
    return output


def modificar_imagenes():
    ruta_raiz = os.path.dirname(os.path.realpath(__file__))
    carpeta_entradas = os.path.join(ruta_raiz, 'img')
    carpeta_guardar = os.path.join(ruta_raiz, 'img_ruido')
    lista_imagenes = os.listdir(carpeta_entradas)
    for i in lista_imagenes:
        x = agregar_ruido(os.path.join(carpeta_entradas,i))
        cv2.imwrite(os.path.join(carpeta_guardar,i), x)
        #memmax.aprender(x)
        #memmin.aprender(x)

modificar_imagenes()
