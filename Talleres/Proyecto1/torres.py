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

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.image.fill(VERDE)
        self.var_x = 0
        self.var_y = 0
        self.id = 0
        self.enviado = 0

    def update(self):
        self.rect.x += self.var_x


class Torres(pygame.sprite.Sprite):
    def __init__(self, px, py):
        le = []
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.rect = self.image.get_rect()
        self.image.fill(BLANCO)
        self.rect.x = px
        self.rect.y = py
        self.radar = auxTorres(px,py,100,30,30)

    def update(self):
        colision = pygame.sprite.spritecollide(self.radar, self.le, False)
        for en_d in colision:
            print "el primero: {0}".format(en_d.id)
            print "disparo"
            print "en radar: {0}".format(len(colision))



class auxTorres(pygame.sprite.Sprite):
    def __init__(self, px, py, radio, xd, yd):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radio,radio])
        self.rect = self.image.get_rect()
        self.image.fill(NEGRO)
        self.rect.x = px
        self.rect.y = py
        self.cx = radio / 2;
        self.cy = radio / 2;
        nx = self.cx - (xd/2)
        ny = self.cy - (yd/2)
        self.rect.x = px - nx
        self.rect.y = py - ny






if __name__ == '__main__':
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    enemigos = pygame.sprite.Group()
    todos = pygame.sprite.Group()
    torres = pygame.sprite.Group()

    t = Torres(200,100)

    for i in range(10):
        ene = Enemigo()
        ene.id = i
        ene.rect.x = -20
        ene.rect.y = 50
        enemigos.add(ene)
        todos.add(ene)


    torres.add(t)
    todos.add(t)
    
    reloj = pygame.time.Clock()
    tiempo = 60
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        tiempo -= 1
        if tiempo == 0:
            for ene in enemigos:
                if ene.enviado == 0:
                    ene.enviado = 1
                    ene.var_x = 2
                    break

            tiempo = 60

        t.le = enemigos
        screen.fill(NEGRO)
        todos.update()
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)
