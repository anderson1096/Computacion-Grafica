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
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.image.fill(AZUL)
        self.rect.x = x
        self.rect.y = y
        self.var_x = 0
        self.var_y = 0
        self.vida = 200

    def golpe(self):
        self.vida -= 5

    def update(self):
        self.rect.x += self.var_x
        self.rect.y += self.var_y


class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.image.fill(ROJO)
        self.rect.x = x
        self.rect.y = y
        self.golpe = False
        self.sonido = pygame.mixer.Sound("boom.wav")
    def update(self):
        if self.golpe:
            self.sonido.play()
            self.golpe = False

class Premio(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.rect = self.image.get_rect()
        self.image.fill(VERDE)
        self.rect.x = x
        self.rect.y = y

        self.golpe = False





if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)

    #Letras
    letra = pygame.font.SysFont("Arial", 30)
    imagenTexto = letra.render("Vida: 30", False, VERDE)
    rectanguloTexto = imagenTexto.get_rect()
    pantalla.blit(imagenTexto, rectanguloTexto)
    todos = pygame.sprite.Group()
    sonido = pygame.mixer.Sound("win.ogg")
    jp = Jugador(100, 100)
    todos.add(jp)
    enemigos = pygame.sprite.Group()
    recompensa = pygame.sprite.Group()
    win = 0
    for i in range(30):
        x = random.randrange(ANCHO-20)
        y = random.randrange(ALTO-20)
        e = Enemigo(x,y)
        todos.add(e)
        enemigos.add(e)

    for i in range(8):
        x = random.randrange(ANCHO-20)
        y = random.randrange(ALTO-20)
        r = Premio(x,y)
        todos.add(r)
        recompensa.add(r)


    reloj = pygame.time.Clock()
    pygame.display.flip()
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x = 1
                    jp.var_y = 0
                if event.key == pygame.K_DOWN:
                    jp.var_y = 1
                    jp.var_x = 0
                if event.key == pygame.K_LEFT:
                    jp.var_x = -1
                    jp.var_y = 0
                if event.key == pygame.K_UP:
                    jp.var_y = -1
                    jp.var_x = 0
                if event.key == pygame.K_s:
                    jp.var_x = 0
                    jp.var_y = 0
                    #sonido.play()
        #Logica del juego
        if jp.rect.x > ANCHO - jp.rect.width:
            #jp.rect.x = 0
            jp.var_x = 0
            jp.rect.x = ANCHO - jp.rect.width

        if jp.rect.x < 0:
            #jp.rect.x = 0
            jp.var_x = 0
            jp.rect.x = 0


        l_col = pygame.sprite.spritecollide(jp, enemigos, False)
        r_col = pygame.sprite.spritecollide(jp, recompensa, True)

        for en in l_col:
            en.golpe = True
            jp.golpe()

        for r in r_col:
            win += 1
            if win >= 5:
                print "WIN"
                sonido.play()

        if jp.vida <= 0:
            fin = True

        todos.update()
        pantalla.fill(BLANCO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(120)
