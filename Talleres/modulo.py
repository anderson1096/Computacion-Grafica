import math
#import draw_vectors
import pygame

#Funcion que determina un vector dados dos puntos
def vector(point1,point2):
    vec = (point2[0] - point1[0],point2[1]-point1[1])
    return vec
#Funcion que determina la norma de un vector
def norma(vec):
    n = math.sqrt(vec[0]**2 + vec[1]**2)
    return n
#Funcion que determina la distancia entre dos puntos
def distancia(point1,point2):
    a = point2[0]-point1[0]
    b = point2[1]-point1[1]
    dis = math.sqrt(a**2 + b**2)
    return dis
#Funcion para retornar el producto punto entre dos vectores
def punto(vec1,vec2):
    res = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return res

#Funcion para sacar el angulo entre vectores
def angulo(vector1,vector2):
    a = math.fabs(punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    print b
    t = math.acos(a/b)
    return math.degrees(t)

"""
#Solicitando los datos de los puntos
str1 = raw_input("Ingrese el primer punto: ").split(" ")
Ax = int(str1[0])
Ay = int(str1[1])
A = (Ax,Ay)
str2 = raw_input("Ingrese el primer punto: ").split(" ")
Bx = int(str2[0])
By = int(str2[1])
B = (Bx,By)

#Iniciando pygame, para dibujar el resultado en pantalla
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
draw_vectors.Dibujarejes(screen, (250,250), 500, 500)
draw_vectors.cartesiano(screen,(250,250),vector(A,B),(0,0,255))
pygame.display.flip()

#Mostrando resultados
print "El vector resultado es: ", vector(A,B)
print "La norma es: ", norma(vector(A,B))
print "La distancia es: ", distancia(A,B)

while 1:
    tecla = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

print angulo(A,B)
"""
