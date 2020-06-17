import json

def producto_maximo(X,Y):
    actual = 0
    if len(X[0]) != len(Y):
        print("Los tamaños no coinciden {}x{} y {}x{}".format(len(X),len(X[0]),len(Y),len(Y[0])))
        return
    
    R = [[0 for x in range(len(Y[0]))] for y in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            actual = -99999
            for k in range(len(Y)):
                aux = X[i][k] + Y[k][j]
                if(actual < aux):
                    actual = aux
                #print(X[i][k] , Y[k][j] , aux)
            R[i][j] = actual
    return R

def producto_minimo(X,Y):
    actual = 0
    if len(X[0]) != len(Y):
        print("Los tamaños no coinciden {}x{} y {}x{}".format(len(X),len(X[0]),len(Y),len(Y[0])))
        return
    
    R = [[0 for x in range(len(Y[0]))] for y in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            actual = 99999
            for k in range(len(Y)):
                aux = X[i][k] + Y[k][j]
                if(actual > aux):
                    actual = aux
                #print(str(X[i][k]) + "+" + str(Y[k][j]) + "=" + str(aux) + "  " + str(R[i][j]))
            R[i][j] = actual
    return R

def transpuesta(X):
    T = [[0 for x in range(len(X))] for y in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            T[j][i] = X[i][j]
    return T

def negativo(X):
    N = [[0 for x in range(len(X[0]))] for y in range(len(X))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            N[i][j] = -X[i][j]
    return N

def minimo(M, X):
    if len(X) != len(M) or len(X[0]) != len(M[0]):
        print("Los tamaños no coinciden")
        return M
    for i in range(len(X)):
        for j in range(len(X[0])):
            M[i][j] = min(M[i][j],X[i][j])

def maximo(M, X):
    if len(X) != len(M) or len(X[0]) != len(M[0]):
        print("Los tamaños no coinciden")
        return M
    for i in range(len(X)):
        for j in range(len(X[0])):
            M[i][j] = max(M[i][j],X[i][j])

class memoria_max():
    def __init__(self):
        self.M = None

    def aprender(self,X):
        if self.M is None: # si es el primer patrón...
            self.M = producto_minimo(X,negativo(transpuesta(X)))
        else: # Si ya existe una matriz
            maximo(self.M,producto_minimo(X,negativo(transpuesta(X))))
        print("Patrón agregado a la memoria")
    
    def recuperar(self,X):
        return producto_minimo(self.M,X)
    
    def cargar_matriz(self,ruta):
        with open(ruta) as m:
            self.M = json.load(m)

class memoria_min():
    def __init__(self):
        self.W = None

    def aprender(self,X):
        if self.W is None: # si es el primer patrón...
            self.W = producto_maximo(X,negativo(transpuesta(X)))
        else: # Si ya existe una matriz
            minimo(self.W,producto_maximo(X,negativo(transpuesta(X))))
        print("Patrón agregado a la memoria")
    
    def recuperar(self,X):
        return producto_maximo(self.W,X)

    def cargar_matriz(self,ruta):
        with open(ruta) as m:
            self.W = json.load(m)