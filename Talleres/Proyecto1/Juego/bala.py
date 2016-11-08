import random
import pygame
import math

ANCHO = 640
ALTO = 480
CENTRO = (300,300)
BLANCO = (255,255,255)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



def vector(a,b):
    return (b[0]-a[0],b[1]-a[1])

def norma(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2)

def dist2p(a,b):
    v=vector(a,b)
    return norma(v)

class Bala(pygame.sprite.Sprite):

	player = None
	def __init__(self,px,py,archivo):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(archivo).convert_alpha()
		self.rect = self.image.get_rect()
		self.var_x = 0
		self.var_y = 0
		self.rect.x = px
		self.rect.y = py
		self.taunted = False


	def update(self, screen, enemigos):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y

		p=(self.player.rect.x,self.player.rect.y)
		g=(self.rect.x,self.rect.y)

		if dist2p(p,g)<=300:
			self.taunted=True
		else:
			self.var_x = 5

		if self.taunted:
			if self.player.rect.x > self.rect.x:
				self.var_x=6
			if self.player.rect.x == self.rect.x:
				self.var_x=0
			if self.player.rect.x < self.rect.x:
				self.var_x=-6
			if self.player.rect.y > self.rect.y:
				self.var_y=6
			if self.player.rect.y == self.rect.y:
				self.var_y=0
			if self.player.rect.y < self.rect.y:
				self.var_y= -6





if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    pygame.mouse.set_visible(False)
    pygame.display.flip()
    jp = Jugador('/home/anderson/Descargas/TD_archivos/creep/enemigo1/1.png', (100,100))
    todos = pygame.sprite.Group()
    todos.add(jp)
    balas = pygame.sprite.Group()
    reloj = pygame.time.Clock()
    ene = Jugador('/home/anderson/Descargas/TD_archivos/creep/enemigo1/1.png', (300, 300))
    todos.add(ene)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                b = Bala(jp.rect.x, jp.rect.y, '/home/anderson/Descargas/TD_archivos/bala1.png')
                balas.add(b)
                todos.add(b)
                b.player = ene



        #ELiminar balas fuera
        for b in balas:

            if b.rect.x > ANCHO:
                balas.remove(b)
                todos.remove(b)





        todos.update()
        pantalla.fill(BLANCO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
