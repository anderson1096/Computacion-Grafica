import pygame
ANCHO = 500
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]

pygame.init()
screen = pygame.display.set_mode((ANCHO,ALTO))
pygame.draw.line(screen, BLANCO, (20,200), (220,200), 1)
pygame.draw.line(screen, BLANCO, (20,200), (20,5), 1)
pygame.draw.line(screen, ROJO, (30, 150), (120,100), 1)
pygame.display.flip()

while 1:
    tecla = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
