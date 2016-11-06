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



class Jugador(pygame.sprite.Sprite):
    camino = None
    def __init__(self, imagen_sp):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen_sp
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.var_x = 4
        self.var_y = 4
        self.cont = 0
        self.contc = 0
        self.dir = 2


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


        for i in range(len(self.camino)-1):
            if self.iguales(self.pini, self.camino[i]):
                self.pfin = self.camino[i+1]

        print self.pini, self.pfin
        if self.pini[0] > self.pfin[0]:
            self.var_x *= -1


    def update(self):
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


        if self.cont < 2:
            self.cont += 1
        else:
            self.cont = 0



def cargar_fondo(archivo, ancho_corte, alto_corte):
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho, img_alto = imagen.get_size()
    matriz_fondo = []
    for fila in range(img_ancho/ancho_corte):
        linea = []
        matriz_fondo.append(linea)
        for columna in range(img_alto/alto_corte):
            cuadro = (fila*ancho_corte, columna*alto_corte, ancho_corte, alto_corte)
            linea.append(imagen.subsurface(cuadro))
    return matriz_fondo



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo = cargar_fondo('Sprites/animals.png', 32, 32)
    jp = Jugador(fondo[6][2])
    todos = pygame.sprite.Group()
    todos.add(jp)

    #trazado de camino
    lector = ConfigParser.ConfigParser()
    lector.read("Mapas/mapa1.map")
    ial_or = int(lector.get("nivel1", "alto"))
    ian_or = int(lector.get("nivel1", "ancho"))
    mapa = lector.get("nivel1", "mapa").split("\n")
    ls_p = []
    yact = 0
    for fila in mapa:
        xact = 0
        for x in range(len(fila)):
            xp = int(lector.get(fila[x], 'x'))
            yp = int(lector.get(fila[x], 'y'))
            xact = (ian_or * x)
            if fila[x] == 'p':
                pto = [xact, yact]
                ls_p.append(pto)

        yact += ial_or

    print ls_p
    jp.camino = ls_p
    jp.nuevo_camino(0)
    reloj = pygame.time.Clock()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        jp.image = fondo[6 + jp.cont][jp.dir]
        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(15)
