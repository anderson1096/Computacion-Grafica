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
    def __init__(self, imagen_sp):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagen_sp
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.var_x = 0
        self.var_y = 0
        self.cont = 0
        self.dir = 0

    def update(self):
        self.rect.x += self.var_x
        self.rect.y += self.var_y
        if self.cont <= 2:
            self.cont += 1
        else:
            self.cont = 0


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




if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fondo = cargar_fondo('Sprites/animals.png', 32, 32)
    jp = Jugador(fondo[0][0])
    todos = pygame.sprite.Group()
    todos.add(jp)
    reloj = pygame.time.Clock()


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x = -5
                    jp.var_y = 0
                    jp.dir = 1

                if event.key == pygame.K_RIGHT:
                    jp.var_x = 5
                    jp.var_y = 0
                    jp.dir = 2

                if event.key == pygame.K_UP:
                    jp.var_x = 0
                    jp.var_y = -5
                    jp.dir = 3

                if event.key == pygame.K_DOWN:
                    jp.var_x = 0
                    jp.var_y = 5
                    jp.dir = 0

                if event.key == pygame.K_SPACE:
                    jp.var_x = 0
                    jp.var_y = 0

        #ELimina
        #ELiminar balas fuera

        jp.image = fondo[0 + jp.cont][jp.dir]
        pantalla.fill(BLANCO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
