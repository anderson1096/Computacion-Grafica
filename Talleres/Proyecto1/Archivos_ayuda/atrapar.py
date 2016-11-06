import os, sys
import pygame
import random

ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,255,0)
BLANCO = (255,255,255)
ANCHO = 1000
ALTO = 600

class Raton(pygame.sprite.Sprite):
    def __init__(self, imagen_sp):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen_sp
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.var_x = 0
        self.var_y = 0
        self.cont = 0
        self.dir = 0
        self.suerte = 0

    def nueva_direccion(self, dir):
        if dir == 0:
            self.var_x = 0
            self.var_y = 5
            self.dir = 0
        elif dir == 1:
            self.var_x = -5
            self.var_y = 0
            self.dir = 1
        elif dir == 2:
            self.var_x = 0
            self.var_y = -5
            self.dir = 3
        elif dir == 3:
            self.var_x = 5
            self.var_y = 0
            self.dir = 2



    def update(self, surface):
        if self.suerte == 0:
            self.suerte = 12
        else:
            self.suerte -= 1

        self.rect.x += self.var_x
        self.rect.y += self.var_y
        #Limite Der
        if self.dir == 2 and self.rect.x >= (ANCHO - self.rect.width):
            self.var_x = 0
            self.var_y = 5
            self.dir = 0
        #Limite Inf
        if self.dir == 0 and self.rect.y >= (ALTO - self.rect.width):
            self.var_x = -5
            self.var_y = 0
            self.dir = 1

        #Limite Izq
        if self.dir == 1 and self.rect.x <= 0:
            self.var_x = 0
            self.var_y = -5
            self.dir = 3

        #Limite Sup
        if self.dir == 3 and self.rect.y <= 0:
            self.var_x = 5
            self.var_y = 0
            self.dir = 2

        if self.cont < 2:
            self.cont += 1
        else:
            self.cont = 0


def cargar_fondo(archivo, ancho_corte, alto_corte):
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho, img_alto = imagen.get_size()
    print img_ancho, ' ', img_alto
    matriz_fondo = []
    for fila in range(img_ancho/ancho_corte):
        linea = []
        matriz_fondo.append(linea)
        for columna in range(img_alto/alto_corte):
            cuadro = (fila*ancho_corte, columna*alto_corte, ancho_corte, alto_corte)
            linea.append(imagen.subsurface(cuadro))
    return matriz_fondo





class Cuadro(pygame.sprite.Sprite):
    def __init__(self, archivo, pos, idc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.id = idc
        self.rect.y = pos[1]
        self.rect.x = pos[0]

    def update(self, surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)




def Game(iconos, cuadros, cont):

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Observando si un icono fue presionado.
            for ic in iconos:
                if ic.rect.collidepoint(event.pos) and ic.id == 1:
                    print "Icono: " + str(ic.id)
                    cuadro1 = Cuadro('Sprites/caja2.png',(100,100),cont)
                    cuadro1.id = cont
                    cont += 1
                    print str(cuadro1.id)
                    col = True
                    while col:
                        col = False
                        colision = pygame.sprite.spritecollide(cuadro1, cuadros, False)
                        for bl in colision:
                            if cuadro1.id != bl.id:
                                cuadro1.rect.left = bl.rect.right
                                col = True

                    cuadros.add(cuadro1)
                    todos.add(cuadro1)

            #Mirando eventos en el cuadro
            for cu in cuadros:
                if cu.rect.collidepoint(event.pos):
                    cu.click = True


        elif event.type == pygame.MOUSEBUTTONUP:
            for cu in cuadros:
                if cu.rect.collidepoint(event.pos):
                    cu.click = False
                col = True
                while col:
                    col = False
                    colision1 = pygame.sprite.spritecollide(cu, cuadros, False)
                    for bl in colision1:
                        if cu.id != bl.id:
                            cu.rect.left = bl.rect.right
                            col = True


        elif event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
    return cont

def paint_zone():
    points = [(0,400),(0,600),(1000,600),(1000,400)]
    pygame.draw.polygon(screen, BLANCO, points)



def main(screen, iconos, cuadros, cont):
    #Captura de teclas

    Game(iconos, cuadros, cont)
    screen.fill(NEGRO)
    #paint_zone()




if __name__ == "__main__":
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((1000,600))

    todos = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    ratones = pygame.sprite.Group()
    cuadros = pygame.sprite.Group()
    icono1 = Cuadro('Sprites/icono.png',(20,560),1)
    iconos.add(icono1)
    todos.add(icono1)

    imagen = cargar_fondo('Sprites/animals.png',32,32)
    temp = 120
    reloj = pygame.time.Clock()
    cont = 2
    nrat = 10
    while 1:
        cont += 1
        main(screen, iconos, cuadros, cont)

        if temp == 0 and nrat > 0:
            raton = Raton(imagen[9][2])
            raton.var_x = 5
            raton.dir = 2
            todos.add(raton)
            ratones.add(raton)
            temp = 60
            nrat -= 1
        for r in ratones:
            r.image = imagen[9 + r.cont][r.dir]

        for bl in cuadros:
            colision = pygame.sprite.spritecollide(bl, ratones, False)
            for elemento in colision:
                if elemento.var_x > 0:
                    elemento.rect.right = bl.rect.left
                elif elemento.var_x < 0:
                    elemento.rect.left = bl.rect.right

                if elemento.var_y > 0:
                    elemento.rect.bottom = bl.rect.top
                elif elemento.var_y < 0:
                    elemento.rect.top = bl.rect.bottom

                nueva_dir = random.randrange(4)
                if nueva_dir != elemento.dir:
                    elemento.nueva_direccion(nueva_dir)

        todos.update(screen)
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(40)
        temp -= 1
