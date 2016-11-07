import random
import pygame
import os, sys
import ConfigParser

ANCHO = 800
ALTO = 480
CENTRO = (300,300)
BLANCO = (255,255,255)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)


class Tile(pygame.sprite.Sprite):
    def __init__(self, archivo, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = archivo
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]

    def update(self, surface):
        pass

class Life(pygame.sprite.Sprite):
    def __init__(self, archivo, pos, mode):
        pygame.sprite.Sprite.__init__(self)
        self.image = archivo
        self.rect = self.image.get_rect()
        self.rect.y = pos[1]
        self.rect.x = pos[0]
        self.modos = mode
        self.vida = 100

    def update(self, surface):
        if self.vida > 80:
            self.image = self.modos[0]
        elif self.vida > 40 and self.vida <= 80:
            self.image = self.modos[1]
        else:
            self.image = self.modos[2]


def load_lifes():
    lifes = []
    for i in range(1, 4):
        imagen = pygame.image.load(('/home/anderson/Descargas/TD_archivos/tileset/13-{0}.png').format(i)).convert_alpha()
        lifes.append(imagen)
    return lifes

def load_tiles():
    tiles = []
    for i in range(1, 9):
        imagen = pygame.image.load(('/home/anderson/Descargas/TD_archivos/tiles/{0}.gif').format(i)).convert_alpha()
        tiles.append(imagen)
    return tiles

def toMap(mapa, lector, ian_or, ial_or, tiles, baldosas, todos):
    yact = 0
    for fila in mapa:
        xact = 0
        for x in range(len(fila)):
            xp = int(lector.get(fila[x], 'x'))
            xact = (ian_or * x)
            if fila[x] != '.':
                baldosa = Tile(tiles[xp], (xact, yact))
                baldosas.add(baldosa)
                todos.add(baldosa)
        yact += ial_or

def paint_mapa(screen, todos, baldosas):
    fondo =  pygame.image.load('/home/anderson/Descargas/TD_archivos/fondo.jpg').convert_alpha()
    screen.blit(fondo, (0,0))
    tiles = load_tiles()
    lector = ConfigParser.ConfigParser()
    lector.read("mapa1.map")
    ial_or = int(lector.get("nivel1", "alto"))
    ian_or = int(lector.get("nivel1", "ancho"))
    mapa = lector.get("nivel1", "mapa").split("\n")
    toMap(mapa, lector, ian_or, ial_or, tiles, baldosas, todos)

def load_fondo(screen):
    fondo =  pygame.image.load('/home/anderson/Descargas/TD_archivos/fondo.jpg').convert_alpha()
    screen.blit(fondo, (0,0))

def paint_tools(screen, todos, vidas):
    mode = load_lifes()
    life =  Life(mode[0], (690, 400), mode)
    todos.add(life)
    vidas.add(life)
    #tower1 = pygame.image.load('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png').convert_alpha()
    #tower2 = pygame.image.load('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png').convert_alpha()
    aux0 =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/01.png').convert_alpha()
    aux1 =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/03.png').convert_alpha()
    aux2 =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/14.png').convert_alpha()
    ama =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/07.png').convert_alpha()
    az =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/06.png').convert_alpha()
    tor =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/02.png').convert_alpha()
    cuadro =  pygame.image.load('/home/anderson/Descargas/TD_archivos/tileset/cuadro.png').convert_alpha()
    screen.blit(aux0, (690, 0))
    screen.blit(aux2, (585, 0))
    screen.blit(aux1, (690, 400 - 320))
    screen.blit(tor, (690, 400 - 240))
    screen.blit(az, (690, 400 - 160))
    screen.blit(ama, (690, 400 - 80))
    screen.blit(cuadro, (48, ALTO - 75))
    #screen.blit(tower1, (63, ALTO - 45))
    screen.blit(cuadro, (133, ALTO - 75))
    #screen.blit(tower2, (148, ALTO - 45))


if __name__ == '__main__':
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    todos = pygame.sprite.Group()
    baldosas = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    # Funcion que dibuja todas las baldosas del mapa y las toma como un objeto
    paint_mapa(todos, baldosas)
    # Funcion que dibuja la vida y las otras imagenes laterales
    paint_tools(todos, vidas)
    pygame.display.flip()
