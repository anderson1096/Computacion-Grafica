import random
import pygame
import math




def vector(a,b):
    return (b[0]-a[0],b[1]-a[1])

def norma(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def dist2p(a,b):
    v=vector(a,b)
    return norma(v)




class Bala(pygame.sprite.Sprite):
    player = None
    def __init__(self, px, py, archivo, power):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.var_x = 0
        self.var_y = 0
        self.rect.x = px
        self.rect.y = py
        self.taunted = False
        self.flag = False
        self.power = power
        self.disp = False

    def update(self, screen, enemigos):
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        p = (self.player.rect.center[0], self.player.rect.center[1])
        g = (self.rect.center[0], self.rect.center[1])

        if dist2p(p, g) <= 300:
            self.taunted = True
        else:
            self.var_x = 5


        if self.taunted:
            if self.player.rect.center[0] > self.rect.x:
                self.var_x = 5
            if self.player.rect.center[0] == self.rect.x:
                self.var_x = 0
                self.flag = True
            if self.player.rect.center[0] < self.rect.x:
                self.var_x = -5
            if self.player.rect.center[1] > self.rect.y:
                self.var_y = 5
            if self.player.rect.center[1] == self.rect.y:
                self.var_y = 0
                self.flag = True
            if self.player.rect.center[1] < self.rect.y:
                self.var_y = -5
