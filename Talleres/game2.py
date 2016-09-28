import pygame
import draw_vectors
import modulo

#Definicion dimensiones de la pantalla a mostrar
ANCHO = 600
ALTO = 480
#definicion de los colores en la escala RGB
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,102,255)
CENTRO = (300,300)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    background = pygame.image.load("Imagenes/fondo.jpg")
    sp = pygame.image.load("Imagenes/sprite.png")
    sp2 = pygame.image.load("Imagenes/ball.png")
    sp_x = 100
    sp_y = 100
    sp2_x = 200
    sp2_y = 200
    screen.blit(background, (0,0))
    screen.blit(sp, [sp_x, sp_y])
    screen.blit(sp2, [sp2_x, sp2_y])
    reloj = pygame.time.Clock()
    pygame.display.flip()
    izq = False
    while 1:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                print "tecla"
                if event.key == pygame.K_RIGHT:
                    sp_x += 10
                if event.key == pygame.K_LEFT:
                    sp_x -= 10
                if event.key == pygame.K_UP:
                    sp_y -= 10
                if event.key == pygame.K_DOWN:
                    sp_y += 10
        if izq == False:
            sp2_x += 5
        if sp2_x == 560:
            izq = True
        if sp2_x == 0:
            izq = False
        if izq == True:
            sp2_x -= 5

        screen.blit(background, (0,0))
        screen.blit(sp,[sp_x,sp_y])
        screen.blit(sp2,[sp2_x,sp2_y])
        pygame.display.flip()
        reloj.tick(60)
