import random
import pygame
import ConfigParser


ANCHO = 1024
ALTO = 680
CENTRO = (300,300)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)
cant_ene = 3
tempo = 40


class Enemigo(pygame.sprite.Sprite):
    camino = None
    def __init__(self, imagen_sp, movimientos, tipo, vida):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen_sp
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.var_x = 4
        self.var_y = 4
        self.cont = 0
        self.contc = 0
        self. moves = movimientos
        self.dir = 0
        self.tipo = tipo
        self.vida = vida


    def iguales(self, pa, pb):
        igual = True
        if pa[0] != pb[0]:
            igual = False
        if pa[1] != pb[1]:
            igual = False
        return igual

    def nuevo_camino(self, conc):
        self.finx = False
        self.finy = False
        self.pini = self.camino[conc]
        self.pfin = self.camino[conc]
        if conc == 0:
            self.rect.x = self.pini[0]
            self.rect.y = self.pini[1]
        elif conc == 1 or conc == 3:
            self.dir = 1
        else:
             self.dir = 0


        for i in range(len(self.camino)-1):
            if self.iguales(self.pini, self.camino[i]):
                self.pfin = self.camino[i+1]


        if self.pini[0] > self.pfin[0]:
            self.var_x *= -1

    def moverse(self, conta, direccion):
        self.image = self.moves[direccion][conta]


    def update(self, surface, enemigos):
        if self.vida == 0:
            enemigos.remove(self)
            todos.remove(self)
            
        if self.pini[0]<self.pfin[0]:
            if self.rect.x >= self.pini[0] and self.rect.x < self.pfin[0]:
                self.rect.x += self.var_x
            else:
                self.finx = True
        else:
            if self.rect.x<=self.pini[0] and self.rect.x>self.pfin[0]:
                self.rect.x+=self.var_x
            else:
                self.finx=True



        if self.finx == True:
            if self.rect.y >= self.pini[1] and self.rect.y < self.pfin[1]:
                self.rect.y += self.var_y
            else:
                self.finy = True


        if self.finx == True and self.finy == True:
            self.contc += 1
            if self.contc < len(self.camino):
                self.nuevo_camino(self.contc)


        if self.cont < len(self.moves):
            self.cont += 1
        else:
            self.cont = 0

        self.moverse(self.cont, self.dir)



def load_enemigos(tipo):
    move = []
    fila = []
    if tipo == 1:
        for i in range(1, 7):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo1/{0}.png'.format(i))
            fila.append(imagen)
        move.append(fila)
        fila = []
        for i in range(1, 7):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo1/{0}-1.png'.format(i))
            fila.append(imagen)
        move.append(fila)
    elif tipo == 2:
        for i in range(1, 5):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo2/{0}.png'.format(i))
            fila.append(imagen)
        move.append(fila)
        fila = []
        for i in range(1, 5):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo2/{0}-1.png'.format(i))
            fila.append(imagen)
        move.append(fila)
    elif tipo == 3:
        for i in range(1, 5):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo3/{0}.png'.format(i))
            fila.append(imagen)
        move.append(fila)
        fila = []
        for i in range(1, 5):
            imagen = pygame.image.load('/home/anderson/Descargas/TD_archivos/creep/enemigo3/{0}-1.png'.format(i))
            fila.append(imagen)
        move.append(fila)

    return move



def crear_enemigo(tipo, todos, enemigos):
    moves = load_enemigos(tipo)
    if tipo == 1:
        ene = Enemigo(moves[0][0], moves, tipo, 100)
    elif tipo == 2:
        ene = Enemigo(moves[0][0], moves, tipo, 200)
    elif tipo == 3:
        ene = Enemigo(moves[0][0], moves, tipo, 400)

    todos.add(ene)
    enemigos.add(ene)
    #trazado de camino
    lector = ConfigParser.ConfigParser()
    lector.read("mapa1.map")
    ial_or = int(lector.get("nivel1", "alto"))
    ian_or = int(lector.get("nivel1", "ancho"))
    mapa = lector.get("nivel1", "mapa").split("\n")
    ls_p = []
    yact = 0
    for fila in mapa:
        xact = 0
        for x in range(len(fila)):

            xact = (ian_or * x)
            if fila[x] == 'p':
                pto = [xact, yact]
                ls_p.append(pto)

        yact += ial_or


    ene.camino = ls_p
    ene.nuevo_camino(0)





if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    todos = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    crear_enemigo(1, todos, enemigos)

    reloj = pygame.time.Clock()

    while 1:

        if tempo == 0 and cant_ene > 0:
            tipo = random.randrange(1,2)
            crear_enemigo(tipo, todos, enemigos)
            tempo = 40
            cant_ene -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pantalla.fill(NEGRO)
        todos.update(pantalla, enemigos)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(15)
        tempo -= 1
