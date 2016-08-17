import pygame
ANCHO = 500
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
CENTRO = (250,250)
def Dibujarejes(screen, c, al, an):
    pygame.draw.line(screen, ROJO, (0,c[1]),(an,c[1]),1)
    pygame.draw.line(screen, ROJO, (c[0],0),(c[0],al),1)

def cartesiano(screen,c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    pygame.draw.line(screen, NEGRO,c,(px,py),1)


pygame.init()
screen = pygame.display.set_mode((ANCHO,ALTO))
screen.fill(BLANCO)
Dibujarejes(screen, CENTRO, ALTO, ANCHO)
point = (-100,-100)
cartesiano(screen,CENTRO,point)
pygame.display.flip()

while 1:
    tecla = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
