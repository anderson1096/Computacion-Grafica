import os, sys
import pygame
import mapa
import enemigo
import random

ANCHO = 800
ALTO = 480
ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,255,0)
BLANCO = (255,255,255)



def gen(num):
    if num == 1:
        aux = [[1,1,1,1,1], 40, 5]
    elif num == 2:
        aux = [[1,2,1,2,2], 40, 5]
    elif num == 3:
        aux = [[3,2,2,2,1], 40, 5]

    return aux

def gen_oleada(l_tipo, tempo, cant_ene, todos, enemigos):
    aux = olear(l_tipo, tempo, cant_ene, todos, enemigos)
    return aux

def olear(l_tipo, tempo, cant_ene, todos, enemigos):
    if tempo == 0 and cant_ene > 0:
        enemigo.crear_enemigo(l_tipo[cant_ene-1], todos, enemigos)
        tempo = 40
        cant_ene -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    tempo -= 1
    if tempo < 0:
        tempo = 40
    return l_tipo, tempo, cant_ene



if __name__ ==  "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    todos = pygame.sprite.Group()

    enemigos = pygame.sprite.Group()


    reloj = pygame.time.Clock()

    aux = gen(3)
    while 1:

        aux = gen_oleada(aux[0], aux[1], aux[2], todos, enemigos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pantalla.fill(NEGRO)
        todos.update(pantalla)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(18)
