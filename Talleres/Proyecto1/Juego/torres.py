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
        self.sonido = pygame.mixer.Sound('/home/anderson/Descargas/TD_archivos/sonidos/click.ogg')



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



def Game(iconos, torres, baldosas, enemigos, flag, lim_torr_a, lim_torr_b):

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ic in iconos:
                if ic.rect.collidepoint(event.pos) and ic.id == 1 and lim_torr_a > 0:
                    ic.sonido.play()
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',pygame.mouse.get_pos(), ic.id + 2, 1)
                    torres.add(torre1)
                    todos.add(torre1)
                    lim_torr_a -= 1
                if ic.rect.collidepoint(event.pos) and ic.id == 2 and lim_torr_b > 0:
                    ic.sonido.play()
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',pygame.mouse.get_pos(), ic.id + 2, 2)
                    torres.add(torre1)
                    todos.add(torre1)
                    lim_torr_b -= 1
                if ic.rect.collidepoint(event.pos) and ic.id == 3:
                    flag = 1
                    ic.sonido.play()

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

    return flag, lim_torr_a, lim_torr_b

def list_ene(torre, enemigos):
    le = []
    for ene in enemigos:
        torre.le.append(ene)


def ini_icons(todos, iconos):
    icono1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',(63, ALTO - 45),1, 0)
    iconos.add(icono1)
    todos.add(icono1)
    icono2 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',(148, ALTO - 45),2, 0)
    iconos.add(icono2)
    todos.add(icono2)
    icono3 = Torre('/home/anderson/Descargas/TD_archivos/play.png',(250, ALTO - 45),3, 0)
    iconos.add(icono3)
    todos.add(icono3)

def main(screen, todos, vidas, baldosas, enemigos, flag, lim_torr_a, lim_torr_b):
    aux = Game(iconos, torres, baldosas, enemigos, flag, lim_torr_a, lim_torr_b)
    flag = aux[0]
    lim_torr_a = aux[1]
    lim_torr_b = aux[2]
    screen.fill(NEGRO)
    mapa.load_fondo(screen)
    mapa.paint_tools(screen, todos, vidas)
    return flag, lim_torr_a, lim_torr_b

def asignar_enemigos(enemigos):
    for t in torres:
        t.le = enemigos
        colision = pygame.sprite.spritecollide(t.radar, t.le, False)
        for en_d in colision:
            if t.tipo == 1:
                centro = t.rect.center
                b = bala.Bala(centro[0]-3, centro[1], '/home/anderson/Descargas/TD_archivos/balas/bala1.png', 5)
                b.disp = True
                balas.add(b)
                todos.add(b)
                b.player = en_d
                b.sonido.play()

            elif t.tipo == 2:
                centro = t.rect.center
                b = bala.Bala(centro[0]-3, centro[1], '/home/anderson/Descargas/TD_archivos/balas/bala2.png', 10)
                b.disp = True
                balas.add(b)
                todos.add(b)
                b.player = en_d
                b.sonido.play()



def borrar_balas(enemigos, balas, todos, screen, baldosas):

    #restar vida y eliminar enemigos muertos
    for e in enemigos:
        colision = pygame.sprite.spritecollide(e, balas, True)
        #print colision
        if len(colision) > 0:
            e.vida -= colision[0].power
            if e.vida <= 0:
                e.kill()
    #eliminar las balas a la deriva
    for b in balas:
        if b.player.alive() == False:
            b.kill()







if __name__ == "__main__":
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #definicion de grupos de sprites
    todos = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    baldosas = pygame.sprite.Group()
    vidas = pygame.sprite.Group()

    #sonidos victoria y derrota
    sonido_vic = pygame.mixer.Sound('/home/anderson/Descargas/TD_archivos/sonidos/win.wav')
    sonido_der = pygame.mixer.Sound('/home/anderson/Descargas/TD_archivos/sonidos/lose.wav')
    #inicializacion del mapa y elementos
    mapa.paint_mapa(screen, todos, baldosas)
    mapa.inicialize(screen, todos, vidas)
    ini_icons(todos, iconos)

    #variable para validar victoria o derrota
    fin = False

    #oleada actual
    oleada_act = 1
    aux = oleada.gen(oleada_act)

    #limite de torres de cada tipo
    lim_torr_a = 4
    lim_torr_b = 2
    flag = 0
    temp_disp = 15
    tool = []
    reloj = pygame.time.Clock()

    #musica de fondo
    pygame.mixer.music.load('/home/anderson/Descargas/TD_archivos/sonidos/backsound.mp3')
    pygame.mixer.music.play(-1)

    while 1:
        tool = main(screen, todos, vidas, baldosas, enemigos, flag, lim_torr_a, lim_torr_b)
        flag = tool[0]
        lim_torr_a = tool[1]
        lim_torr_b = tool[2]

        #condiciones de derrota o victoria
        for i in vidas:
            if oleada_act == 4 and i.vida > 0 and len(enemigos) == 0:
                print "Victoria"
                fin = True
                fondo =  pygame.image.load('/home/anderson/Descargas/TD_archivos/win.jpg').convert_alpha()
                screen.blit(fondo, (-50,0))
                #pygame.mixer.music.stop()
                #sonido_vic.play()
            elif i.vida <= 0:
                print "Derrota"
                fin = True
                fondo =  pygame.image.load('/home/anderson/Descargas/TD_archivos/game_over.jpg').convert_alpha()
                screen.blit(fondo, (-50,0))
                #pygame.mixer.music.stop()
                #sonido_der.play()

        #generacion de oleadas
        if flag == 1:
            aux = oleada.gen_oleada(aux[0], aux[1], aux[2], todos, enemigos)
            if aux[2] == 0:
                flag = 0
                oleada_act += 1
                if oleada_act != 4:
                    aux = oleada.gen(oleada_act)

        #temporizador de disparo de las torres
        if temp_disp == 0:
            asignar_enemigos(enemigos)
            temp_disp = 15
        borrar_balas(enemigos, balas, todos, screen, baldosas)

        if fin == False:
            todos.update(screen, enemigos)
            baldosas.draw(screen)
            todos.draw(screen)
        pygame.display.flip()
        reloj.tick(30)
        temp_disp -= 5
