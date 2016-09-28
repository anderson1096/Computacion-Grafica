import libreria
import math
import pygame

#Definicion dimensiones de la pantalla a mostrar
ANCHO = 600
ALTO = 600
#definicion de los colores en la escala RGB
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,102,255)
CENTRO = (300,300)

def angulo_ciclo():
    l = []
    for i in range(360):
        l.append(i)
    return l

def polar_function(angulo,a):
    r = 2*math.sin(3*angulo)
    return a*r,angulo

def list_polares(polares):
    cartesianas = []
    for polar in polares:
        aux = libreria.polares_cartesianas(polar[0], polar[1])
        cartesianas.append(aux)
    return cartesianas

def escalar(puntos, escala):
    l = []
    for i in puntos:
        aux = (i[0] * escala, i[1] * escala)
        l.append(aux)
    return l

def draw(puntos):
    for i in puntos:
        screen.set_at(i,VERDE)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    libreria.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    grados = angulo_ciclo()
    polares = []
    for i in grados:
        aux = polar_function(i,100)
        polares.append(aux)
    cartesianas = list_polares(polares)
    cartesianasT = libreria.trans_points(cartesianas,CENTRO)
    n = len(cartesianasT)
    for i in cartesianasT:
        #libreria.cartesiano(screen, CENTRO, i, VERDE)
        #pygame.draw.line(screen,VERDE, cartesianasT[i-1],cartesianasT[i])
        pygame.draw.circle(screen,VERDE,i,2)
        #screen.set_at(i,NEGRO)
    #pygame.draw.polygon(screen, VERDE, cartesianasET, 1)"""
    #pygame.draw.polygon(screen, VERDE, cartesianasT)
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
