import pygame
import random
import modulo
import draw_vectors

ANCHO = 500
ALTO = 500
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
CENTRO = (250,250)

#Funcion que dibuja los ejes en la pantalla
def Dibujarejes(screen, c, al, an):
    pygame.draw.line(screen, ROJO, (0,c[1]),(an,c[1]),1)
    pygame.draw.line(screen, ROJO, (c[0],0),(c[0],al),1)

#Funcion que genera puntos X y Y al azar dado el centro
def puntos_azar():
    res = [random.randrange(0,200),random.randrange(0,200)]
    return res

#Funcion que retorna un vector de n puntos al azar
def generate_points(n,CENTRO):
    Puntos = []
    for i in range(n):
        Puntos.append(puntos_azar())
    return Puntos

def transladar(c,a):
    return (a[0]+c[0],a[0]+a[1])

if __name__=="__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    Dibujarejes(screen, CENTRO, ALTO, ANCHO)
    point1 = (100,100)
    point2 = (-100,30)
    aux = modulo.vector(point1,point2)
    draw_vectors.cartesiano(screen,CENTRO,aux,BLANCO)
    screen.set_at(transladar(CENTRO,point1), ROJO)
    pygame.draw.circle(screen,ROJO,transladar(CENTRO,point1),10,1)
    screen.set_at(transladar(CENTRO,point2), ROJO)
    pygame.draw.circle(screen,ROJO,transladar(CENTRO,point2),10,1)
    pygame.display.flip()
    #Pintando puntos aleatorios en la pantalla
    """for i in generate_points(5,CENTRO):
        screen.set_at(i,BLANCO)
        pygame.draw.circle(screen, BLANCO, i, 10, 1)
    """


    pygame.display.flip()

    while 1:
        tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
