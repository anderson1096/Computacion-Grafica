import os, sys
import pygame

ROJO = (255,0,0)
NEGRO = (0,0,0)
AZUL = (0,255,0)
BLANCO = (255,255,255)

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




def Game(iconos, cuadros):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ic in iconos:
                if ic.rect.collidepoint(event.pos) and ic.id == 1:
                    cuadro1 = Cuadro('Sprites/caja.png',(100,100),ic.id + 3)
                    cuadros.add(cuadro1)
                    todos.add(cuadro1)
                if ic.rect.collidepoint(event.pos) and ic.id == 2:
                    cuadro1 = Cuadro('Sprites/caja.png',(300,100),ic.id + 4)
                    cuadros.add(cuadro1)
                    todos.add(cuadro1)


            for cu in cuadros:
                if cu.rect.collidepoint(event.pos):
                    cu.click = True

        elif event.type == pygame.MOUSEBUTTONUP:
            for cu in cuadros:
                if cu.rect.collidepoint(event.pos):
                    cu.click = False

        elif event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()

def paint_zone():
    points = [(0,400),(0,600),(1000,600),(1000,400)]
    pygame.draw.polygon(screen, BLANCO, points)



def main(screen, iconos, cuadros):
    #Captura de teclas
    Game(iconos, cuadros)
    screen.fill(NEGRO)
    paint_zone()




if __name__ == "__main__":
    #Para que la ventana salga centrada en la pantalla
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    todos = pygame.sprite.Group()
    iconos = pygame.sprite.Group()
    cuadros = pygame.sprite.Group()
    icono1 = Cuadro('Sprites/icono.png',(20,420),1)
    iconos.add(icono1)
    todos.add(icono1)
    icono2 = Cuadro('Sprites/icono.png',(70,420),2)
    iconos.add(icono2)
    todos.add(icono2)
    reloj = pygame.time.Clock()

    while 1:
        main(screen, iconos, cuadros)
        todos.update(screen)
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)
