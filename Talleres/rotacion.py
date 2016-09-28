import pygame
import draw_vectors
import modulo
import math

#Definicion dimensiones de la pantalla a mostrar
ANCHO = 600
ALTO = 600
#definicion de los colores en la escala RGB
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,102,255)
CENTRO = (300,300)

#Funcion para transladar un punto
def transladar(c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    return px,py

#Funcion para transladar una lista de puntos
def trans_points(puntos,c):
    trans = []
    for p in puntos:
        px = c[0] + p[0]
        py = c[1] - p[1]
        trans.append([px,py])
    return trans

#Funcion para rotar un punto
def rotar_punto(punto,angulo):
    rad = math.radians(angulo)
    xr = punto[0] * math.cos(rad) - punto[1] * math.sin(rad)
    yr = punto[0] * math.sin(rad) + punto[1] * math.cos(rad)
    return int(xr),int(yr)

#Funcion para rotar una lista de puntos
def rotar_lpuntos(puntos, angulo):
    rot = []
    rad = math.radians(angulo)
    for punto in puntos:
        xr = punto[0] * math.cos(rad) - punto[1] * math.sin(rad)
        yr = punto[0] * math.sin(rad) + punto[1] * math.cos(rad)
        rot.append((int(xr),int(yr)))
    return rot


if __name__== "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    draw_vectors.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    pygame.display.flip()
    points = [(100,100), (0,200), (100,300), (200,300), (300,200), (200,100)]
    pointsT = trans_points(points,CENTRO)
    #cont = 0
    reloj = pygame.time.Clock()
    while 1:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            pointsR = rotar_lpuntos(points, 45)
            pointRT = trans_points(pointsR, CENTRO)
            pygame.draw.polygon(screen, AZUL,pointsT)
            pygame.draw.polygon(screen, AZUL, pointRT)
            points = pointsR
            pygame.display.flip()
            #cont += 45
            #if(cont == 360):
            #    cont = 0
        reloj.tick(60)
