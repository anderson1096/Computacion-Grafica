import os, sys
import pygame
import mapa
import enemigo
import oleada
import bala

ANCHO = 800
ALTO = 480
ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,255,0)
BLANCO = (255,255,255)

class Torre(pygame.sprite.Sprite):
    def __init__(self, archivo, pos, idc, tipo):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.y = pos[1]
        self.rect.x = pos[0]
        self.id = idc
        self.radar = auxTorres(pos[0],pos[1],100,48,48)
        self.le = []
        self.tipo = tipo

    def update(self, surface, enemigos):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)

        self.radar.rect.center = self.rect.center






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



def Game(iconos, torres, baldosas, enemigos, flag):

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ic in iconos:
                if ic.rect.collidepoint(event.pos) and ic.id == 1:
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',pygame.mouse.get_pos(), ic.id + 2, 1)
                    torres.add(torre1)
                    todos.add(torre1)
                if ic.rect.collidepoint(event.pos) and ic.id == 2:
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',pygame.mouse.get_pos(), ic.id + 2, 2)
                    torres.add(torre1)
                    todos.add(torre1)
                if ic.rect.collidepoint(event.pos) and ic.id == 3:
                    flag = 1


            for t in torres:
                if t.rect.collidepoint(event.pos):
                    t.click = True

        elif event.type == pygame.MOUSEBUTTONUP:
            for b in baldosas:
                for t in torres:
                    if b.rect.collidepoint((t.rect.x,t.rect.y)):
                        t.click = False
                        t.rect.center = b.rect.center

        elif event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()

    return flag

def list_ene(torre, enemigos):
    le = []
    for ene in enemigos:
        torre.le.append(ene)


def main(screen, todos, vidas, baldosas, enemigos, flag):
    #Captura de teclas
    icono1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',(63, ALTO - 45),1, 0)
    iconos.add(icono1)
    todos.add(icono1)
    icono2 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',(148, ALTO - 45),2, 0)
    iconos.add(icono2)
    todos.add(icono2)
    icono3 = Torre('/home/anderson/Descargas/TD_archivos/play.png',(250, ALTO - 45),3, 0)
    iconos.add(icono3)
    todos.add(icono3)
    flag = Game(iconos, torres, baldosas, enemigos, flag)
    screen.fill(NEGRO)
    mapa.load_fondo(screen)
    mapa.paint_tools(screen, todos, vidas)
    return flag

def asignar_enemigos(enemigos):
    for t in torres:
        t.le = enemigos
        colision = pygame.sprite.spritecollide(t.radar, t.le, False)
        for en_d in colision:
            if t.tipo == 1:
                centro = t.rect.center
                b = bala.Bala(centro[0], centro[1], '/home/anderson/Descargas/TD_archivos/bala1.png')
                balas.add(b)
                todos.add(b)
                b.player = en_d
                #b.disp = 1
            elif t.tipo == 2:
                centro = t.rect.center
                b = bala.Bala(centro[0], centro[1], '/home/anderson/Descargas/TD_archivos/bala2.png')
                balas.add(b)
                todos.add(b)
                b.player = en_d
                #b.disp = 1


def borrar_balas(enemigos, balas, todos):
    for e in enemigos:
        colision = pygame.sprite.spritecollide(e, balas, True)
        if len(colision) > 0:
            e.vida -= 5
            print e.vida
            if e.vida == 0:
                e.kill()


if __name__ == "__main__":
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    todos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    baldosas = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    mapa.paint_mapa(screen, todos, baldosas)
    mapa.inicialize(screen, todos, vidas)
    oleada_act = 1
    aux = oleada.gen(oleada_act)
    flag = 0
    cont = 5
    reloj = pygame.time.Clock()
    while 1:

        flag = main(screen, todos, vidas, baldosas, enemigos, flag)
        if flag == 1:
            aux = oleada.gen_oleada(aux[0], aux[1], aux[2], todos, enemigos)
            if aux[2] == 0:
                flag = 0
                if oleada_act == 3:
                    print 'Gano'
                else:
                    oleada_act += 1
                aux = oleada.gen(oleada_act)

        asignar_enemigos(enemigos)
        borrar_balas(enemigos, balas, todos)


        todos.update(screen, enemigos)
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(20)
