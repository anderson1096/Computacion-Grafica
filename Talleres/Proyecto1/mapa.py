import random
import pygame
import os, sys
import ConfigParser

ANCHO = 1024
ALTO = 384
CENTRO = (300,300)
BLANCO = (255,255,255)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)

def cargar_fondo(archivo, ancho_corte, alto_corte):
    imagen = pygame.image.load('Sprites/terrenogen.png').convert_alpha()
    img_ancho, img_alto = imagen.get_size()
    matriz_fondo = []
    for fila in range(img_ancho/ancho_corte):
        linea = []
        for columna in range(img_alto/alto_corte):
            cuadro = (fila*ancho_corte, columna*alto_corte, ancho_corte, alto_corte)
            linea.append(imagen.subsurface(cuadro))
        matriz_fondo.append(linea)
    return matriz_fondo




if __name__ == '__main__':
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    lector = ConfigParser.ConfigParser()
    lector.read("Mapas/mapa1.map")
    print lector.sections()
    origen = lector.get("nivel1", "origen")
    ial_or = int(lector.get("nivel1", "alto"))
    ian_or = int(lector.get("nivel1", "ancho"))
    mapa = lector.get("nivel1", "mapa").split("\n")

    fondo = cargar_fondo('Sprites/terrenogen.png', 32, 32)
    print 'filas', len(mapa)
    yact = 0
    for fila in mapa:
        xact = 0
        for x in range(len(fila)):
            xp = int(lector.get(fila[x], 'x'))
            yp = int(lector.get(fila[x], 'y'))
            xact = (ian_or * x)
            screen.blit(fondo[xp][yp], (xact, yact))
        yact += ial_or


    #fondo = pygame.image.load('Sprites/terrenogen.png').convert_alpha()

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
