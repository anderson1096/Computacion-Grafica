import random



#Funcion para generar una matriz aleatoria dado su tamano
def matriz_aleatoria(tamf, tamc):
    cont = 0
    m = []
    for i in range(tamf):
        f = []
        valor = random.randrange(5)
        f.append(valor)
        m.append(f)
        for j in range(tamc-1):
            valor2 = random.randrange(5)
            m[i].append(valor2)
    return m

#Funcion para sumar dos matrices
def suma_matrices(matriz1, matriz2):
    aux = len(matriz1)
    res = matriz_aleatoria(len(matriz1),len(matriz1))
    for i in range(aux):
        for j in range(aux):
            res[i][j] = matriz1[i][j] + matriz2[i][j]
    return res

#Funcion para construir una lista de tamano n (vector)
def vector(n):
    vec = []
    for i in range(n):
        vec.append(0)
    return vec

#Funcion que suma las filas de una matriz
def suma_filas(matriz1):
    res = vector(len(matriz1[0]))
    aux = len(matriz1)
    for i in matriz1:
        for j in range(len(res)):
            res[j] += i[j]

    return res

#Funcion que calcula la transpuesta de una matriz
def transpuesta(matriz):
    res = matriz_aleatoria(len(matriz[0]),len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            res[j][i] = matriz[i][j]
    return res

#Funcion que calcula la opuesta de una matriz
def opuesta(matriz):
    aux = len(matriz)
    for i in range(aux):
        for j in range(aux):
            matriz[i][j] = matriz[i][j] * (-1)
    return matriz

#Funcion para imprimir una matriz
def imprimir(matriz):
    for fila in matriz:
        print fila

m1 = [[1,0,3],[21,5,6],[7,34,9]]
m2 = [[1,2,3],[0,5,6],[7,0,9]]

print "Matriz 1: "
imprimir(m1)
print "Matriz 2: "
imprimir(m2)
print "Resultado: "
imprimir(suma_filas(m1))
