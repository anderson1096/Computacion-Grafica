import random
import pygame
import os, sys

ANCHO = 600
ALTO = 480
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

        if self.rect.y >= ALTO - self.rect.height:
            self.rect.y = ALTO - self.rect.height
            self.var_y = 0


if __name__ == '__main__':
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    todos = pygame.sprite.Group()
    jp = Jugador(0,0)


    todos.add(jp)

    reloj = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x = -5

                if event.key == pygame.K_RIGHT:
                    jp.var_x = 5

                if event.key == pygame.K_UP:
                    jp.var_y = -10

        screen.fill(NEGRO)
        todos.update()
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)
