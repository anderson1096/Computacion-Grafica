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
VERDE = (0,255,0)
AZUL = (0,102,255)
CENTRO = (300,300)

#Funcion para trasladar
def transladar(c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    return px,py

def trans_points(puntos,c):
    trans = []
    for p in puntos:
        px = c[0] + p[0]
        py = c[1] - p[1]
        trans.append([px,py])
    return trans



def escalar(s, puntos):
    escalados = []
    for p in puntos:
        escalados.append([p[0] * s[0], p[1] * s[1]])
    return escalados

def dibujar_puntos(points, screen):
    for p in points:
        pygame.draw.circle(screen, NEGRO, p, )


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    draw_vectors.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    pygame.display.flip()
    cont = 0
    points = ([50,50],[75,75],[175,75],[125,50])
    while 1:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                """cont+=1
                if cont == 1:
                    pos1 = pygame.mouse.get_pos()
                elif cont == 2:
                    pos2 = pygame.mouse.get_pos()
                elif cont == 3:
                    pos3 = pygame.mouse.get_pos()
                """
                pygame.draw.polygon(screen,AZUL,trans_points(points,CENTRO))
                pygame.draw.polygon(screen,ROJO,trans_points(escalar([2,2],points),CENTRO))
                pygame.draw.polygon(screen,VERDE,trans_points(escalar([3,3],points),CENTRO))
                pygame.draw.polygon(screen,NEGRO,trans_points(escalar([0.5,0.5],points),CENTRO))
                
                pygame.display.flip()
                cont = 0





"""if __name__== "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    while 1:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    print escalar([2,2],puntos)
"""
