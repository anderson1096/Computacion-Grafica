import pygame
import draw_vectors
import modulo

#Definicion dimensiones de la pantalla a mostrar
ANCHO = 600
ALTO = 600
#definicion de los colores en la escala RGB
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,102,255)
CENTRO = (300,300)

def transladar(c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    return px,py

if __name__== "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    draw_vectors.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    pygame.display.flip()
    cont = 0
    while 1:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont == 1:
                    pos1 = pygame.mouse.get_pos()
                    AJA = (pos1[0]-CENTRO[0],CENTRO[1]-pos1[1])
                    print AJA
                if cont == 2:
                    pos2 = pygame.mouse.get_pos()
                    print pos2
                    aux = modulo.vector(pos1,pos2)
                    draw_vectors.cartesiano(screen,CENTRO,aux,NEGRO)
                    pygame.draw.line(screen, AZUL,transladar(CENTRO,pos1),transladar(CENTRO,pos2),1)
                    pygame.display.flip()
                    cont = 0
