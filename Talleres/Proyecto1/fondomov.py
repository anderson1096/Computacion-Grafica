import random
import pygame
import os, sys

ANCHO = 800
ALTO = 600
CENTRO = (300,300)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)


class Jugador(pygame.sprite.Sprite):
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.rect = self.image.get_rect()
        self.image.fill(BLANCO)
        self.rect.x = px
        self.rect.y = py
        self.var_x = 0
        self.var_y = 0
        self.salto = False

    def gravedad(self):
        if self.var_y == 0:
            self.var_y = 1
        else:
            self.var_y += 0.35

    def update(self):
        self.gravedad()
        self.rect.x += self.var_x
        self.rect.y += self.var_y

        if self.rect.y >= ALTO - 180:
            self.rect.y = ALTO - 180
            self.var_y = 0




if __name__ == '__main__':
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load("background.jpg")
    mov_x = 0
    pos_x = 0
    pos_y = 800
    marco = fondo.subsurface(pos_x,pos_y, ANCHO, ALTO)
    screen.blit(marco, [0,0])
    todos = pygame.sprite.Group()
    jp = Jugador(10,400)
    todos.add(jp)
    pygame.display.flip()
    reloj = pygame.time.Clock()
    #bandera que determina el movimiento derecha o izquierda
    flag = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #pos_x = -5
                    jp.var_x = -5
                    flag = 1


                if event.key == pygame.K_RIGHT:
                    #pos_x = 5
                    jp.var_x = 5
                    flag = 2

                if event.key == pygame.K_UP:
                    jp.var_y = -10

        #Condicion para que se reinicie el mapa
        if pos_x == fondo.get_rect()[2] - ANCHO:
            pos_x = 0

        #Condicion para el limite 1
        if jp.rect.x < 10:
            jp.rect.x = 10


        #Condicion del limite 2 movimiento derecha e izquierda
        if jp.rect.x == 700 and flag == 2:
            mov_x = 5
            jp.var_x = 0
        elif flag == 1:
            mov_x = -5
            if pos_x == 10:
                mov_x = 0
        #Condicion para que solo se mueva el cuadro y no el fondo
        elif jp.rect.x >= 10 and jp.rect.x < 700 and flag == 2:
            mov_x = 0

        pos_x += mov_x
        marco = fondo.subsurface(pos_x,pos_y, ANCHO, ALTO)
        screen.blit(marco, [0,0])
        todos.update()
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)
