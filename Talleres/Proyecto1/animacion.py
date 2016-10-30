import random
import pygame
import os, sys

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
    print img_ancho, ' ', img_alto
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
    #fondo = pygame.image.load('Sprites/terrenogen.png').convert_alpha()
    fondo = cargar_fondo('Sprites/terrenogen.png', 32, 32)
    screen.blit(fondo[8][9],(0,0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
