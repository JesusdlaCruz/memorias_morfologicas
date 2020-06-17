import statistics
from PIL import Image

def arreglo_a_imagen(lista, ruta): # Guarda una lista de valores binarios como una imagen

    listaRGB = [0 for i in range(len(lista))] # Lista que almacenará los valores rgb de la imagen como tuplas
    for i in range(len(lista)): # Llena el arreglo bidimensional con los valores binarios de la imagen
        if lista[i][0] <= 0:
            listaRGB[i] = (0,0,0)
        else:
            listaRGB[i] = (255,255,255)
        #print(listaRGB)

    img = Image.new("RGB", (20,20), "white") # Crea objeto imagen de 10x10 pixeles en blanco
    img.putdata(listaRGB) # Asigna los valores de la lista
    img.save(ruta)

def imagen_como_arreglo(ruta):
    im = Image.open(ruta)
    a = list(im.getdata()) # imagen a arrego unidimensional
    b =  [[0 for x in range(1)] for y in range(len(a))] # Crea un arreglo bidimensional

    for i in range(len(a)): # Llena el arreglo bidimensional con los valores binarios de la imagen
        if statistics.mean(a[i]) == 0:
            b[i][0]=0
        else:
            b[i][0]=1
    return b