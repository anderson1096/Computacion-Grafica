import random
import pygame

ANCHO = 640
ALTO = 480
CENTRO = (300,300)
BLANCO = (255,255,255)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Muro(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vel = 2
        self.t = 60
        self.fuego = 0

    def tempo(self):
        self.t -= 1
        if self.t == 0:
            self.t = 60
            self.fuego = 1
        else:
            self.fuego = 0


    def update(self):
        self.rect.x -= self.vel
        if self.rect.x < 0:
            self.rect.x = ANCHO - self.rect.width

class Disparo(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vel = 10
        self.dir = 0

    def update(self):
        if self.dir == 0:
            self.rect.x += self.vel
        else:
            self.rect.x -= self.vel



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    pygame.mouse.set_visible(False)
    pygame.display.flip()
    sonido_shot = pygame.mixer.Sound('laser.wav')
    jp = Jugador('Sprites/nave1.png')
    todos = pygame.sprite.Group()
    todos.add(jp)
    enemigos = pygame.sprite.Group()
    for i in range(6):
        x = ANCHO
        y = random.randrange(ALTO - 35)
        e = Enemigo('Sprites/enemigo1.png')
        e.rect.x = x
        e.rect.y = y
        e.vel = random.randrange(5)
        enemigos.add(e)
        todos.add(e)

    balas = pygame.sprite.Group()
    ebalas = pygame.sprite.Group()

    reloj = pygame.time.Clock()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                b = Disparo('Sprites/bala.png')
                b.rect.x = jp.rect.x
                b.rect.y = jp.rect.y
                sonido_shot.play()
                balas.add(b)
                todos.add(b)


        #ELiminar balas fuera
        for b in balas:
            ls_imp = pygame.sprite.spritecollide(b, enemigos, True)
            for b_imp in ls_imp:
                balas.remove(b)
                todos.remove(b)

            if b.rect.x > ANCHO:
                balas.remove(b)
                todos.remove(b)


        #Disparo de enemigos
        for e in enemigos:
            e.tempo()
            if e.fuego == 1:
                b = Disparo('Sprites/bala.png')
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                b.dir = 1
                ebalas.add(b)
                todos.add(b)



        todos.update()
        pantalla.fill(BLANCO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
