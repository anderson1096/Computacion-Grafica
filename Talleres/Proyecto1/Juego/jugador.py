import os, sys
import pygame
import mapa


ANCHO = 800
ALTO = 480
ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,255,0)
BLANCO = (255,255,255)

class Torre(pygame.sprite.Sprite):
    def __init__(self, archivo, pos, idc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.click = False
        self.rect.y = pos[1]
        self.rect.x = pos[0]
        self.id = idc

    def update(self, surface):
        if self.click:
            self.rect.center = pygame.mouse.get_pos()
        surface.blit(self.image, self.rect)




def Game(iconos, torres, baldosas):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ic in iconos:
                if ic.rect.collidepoint(event.pos) and ic.id == 1:
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',pygame.mouse.get_pos(), ic.id + 2)
                    torres.add(torre1)
                    todos.add(torre1)
                if ic.rect.collidepoint(event.pos) and ic.id == 2:
                    torre1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',pygame.mouse.get_pos(), ic.id + 2)
                    torres.add(torre1)
                    todos.add(torre1)


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




def main(screen, todos, vidas, baldosas):
    #Captura de teclas

    icono1 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-1-1.png',(63, ALTO - 45),1)
    iconos.add(icono1)
    todos.add(icono1)
    icono2 = Torre('/home/anderson/Descargas/TD_archivos/towers/turret-2-1.png',(148, ALTO - 45),2)
    iconos.add(icono2)
    todos.add(icono2)
    Game(iconos, torres, baldosas)
    screen.fill(NEGRO)
    mapa.load_fondo(screen)
    mapa.paint_tools(screen, todos, vidas)






if __name__ == "__main__":
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    todos = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    baldosas = pygame.sprite.Group()
    vidas = pygame.sprite.Group()
    mapa.paint_mapa(screen, todos, baldosas)
    mapa.paint_tools(screen, todos, vidas)
    reloj = pygame.time.Clock()

    while 1:
        main(screen, todos, vidas, baldosas)
        todos.update(screen)
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)
