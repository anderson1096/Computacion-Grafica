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

#Funcion que determina los tres angulos de un triangulo
def angulos_triangulo(pos1,pos2,pos3):
    vec1 = modulo.vector(pos1,pos2)
    vec2 = modulo.vector(pos2,pos3)
    vec3 = modulo.vector(pos3,pos1)
    angulo1 = modulo.angulo(vec1,vec2)
    angulo2 = modulo.angulo(vec2,vec3)
    angulo3 = modulo.angulo(vec3,vec1)
    print angulo1,angulo2,angulo3


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
                elif cont == 2:
                    pos2 = pygame.mouse.get_pos()
                elif cont == 3:
                    pos3 = pygame.mouse.get_pos()
                    pygame.draw.polygon(screen,AZUL,[pos1,pos2,pos3])
                    pygame.display.flip()
                    cont = 0
                    angulos_triangulo(pos1,pos2,pos3)
