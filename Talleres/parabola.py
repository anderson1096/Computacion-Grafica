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

#Funcion para trasladar
def transladar(c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    return px,py


#Funcion que dibuja un punto en el plano
def parabola(x):
    y = x**2 - 100
    return x,y


#Funcion que retorna los puntos para una parabola


if __name__== "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    draw_vectors.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    pygame.display.flip()
    reloj = pygame.time.Clock()
    cont = -20
    while 1 and cont <= 20:
        #tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            pygame.draw.circle(screen, NEGRO, transladar(CENTRO,parabola(cont)), 2, 1)
            pygame.draw.line(screen, NEGRO,transladar(CENTRO,parabola(cont-1)),transladar(CENTRO,parabola(cont)),1)
            pygame.display.flip()
            reloj.tick(1300)
            cont+=1
