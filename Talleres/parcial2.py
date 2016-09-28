import libreria
import math
import pygame

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

#Funcion QUE DIBUJA UN POLIGONO EN pantalla
def draw(points,color):
    pygame.draw.polygon(screen, color, points)


def escalar(puntos, escala):
    l = []
    for i in puntos:
        aux = (i[0] * escala, i[1] * escala)
        l.append(aux)
    return l

#funcion para rotar un punto por medio de otro punto fijo
def rotar_fijo(point, roter, angulo):
    angulo = math.radians(angulo)
    px = roter[0] + (point[0]-roter[0]) * math.cos(angulo) - (point[1] - roter[1]) * math.sin(angulo)
    py = roter[1] + (point[1]-roter[1]) * math.cos(angulo) - (point[0] - roter[0]) * math.sin(angulo)
    return int(px),int(py)

#Funcion para rotar una lista de puntos a traves de un punto fijo
def rotarV_fijo(points, roter, angulo):
    angulo = math.radians(angulo)
    l = []
    for point in points:
        px = roter[0] + (point[0]-roter[0]) * math.cos(angulo) - (point[1] - roter[1]) * math.sin(angulo)
        py = roter[1] + (point[1]-roter[1]) * math.cos(angulo) - (point[0] - roter[0]) * math.sin(angulo)
        l.append((int(px),int(py)))
    return l


#Funcion PARA DIBUJAR UN PATRON ALREDEDOR DE LA pantalla
def patron_poligono(poligono):
    #Dibujando la parte superior del poligono
    draw(poligono, VERDE)
    while poligono[0][0] < ANCHO - 40:
        l = []
        for point in poligono:
            aux = [point[0] + 50, point[1]]
            l.append(aux)
        poligono = l
        draw(poligono, VERDE)

    #Dibujando la parte derecha
    poligono1 = rotarV_fijo(poligono, (poligono[0][0] + 5,poligono[0][1] + 10), 270)

    while poligono1[0][1] < ALTO - 50:
        l = []
        for point in poligono1:
            aux = [point[0], point[1] + 60]
            l.append(aux)
        poligono1 = l
        draw(poligono1, ROJO)
    draw(poligono1, BLANCO)

    #Dibujando parte inferior
    poligono2 = rotarV_fijo(poligono1, (poligono1[0][0] + 9,poligono1[0][1] + 20), 90)
    draw(poligono2, AZUL)
    while poligono2[0][0] > 0:
        l = []
        for point in poligono2:
            aux = [point[0] - 50, point[1]]
            l.append(aux)
        poligono2 = l
        draw(poligono2, AZUL)

    draw(poligono2, BLANCO)


    #Dibujando parte IZQUIERDA
    poligono3 = rotarV_fijo(poligono2, (poligono2[0][0] + 15,poligono2[0][1] - 45), 270)
    draw(poligono3, NEGRO)
    while poligono3[0][1] > 150:
        l = []
        for point in poligono3:
            aux = [point[0], point[1] - 60]
            l.append(aux)
        poligono3 = l
        draw(poligono3, NEGRO)



    return 1

def up_right(points):
    mayor = points[0]
    for i in points:
        if i > mayor:
            mayor = i
    return mayor



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    
    #Esto es para la prueba de patrones, son 3 poligonos y el llamado a la funcion (escogen el poligono que quieran enviar a la funcion)

    pot = [[10,10], [40,10], [40,20], [20,20], [20,40], [40,40], [40,50], [10,50]]
    pot2 = [[10,10], [50,10], [10,30]]
    pot3 = [[10,10], [40,10], [40,30],[60,30],[60,40],[30,40],[30,20],[10,20]]

    patron_poligono(pot3)

    #libreria.Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    #Interseccion, union y resto (conjuntos) dos circunferencias
    '''pygame.draw.circle(screen,VERDE,CENTRO, 50)
    pygame.draw.circle(screen,AZUL,(CENTRO[0] + 80,CENTRO[1]), 50)
    P1 = libreria.transladar(CENTRO,[40,30])
    P2 = libreria.transladar(CENTRO,[40,-30])
    #pygame.draw.line(screen,AZUL,P1,P2)
    pygame.draw.ellipse(screen, BLANCO,[CENTRO[0]+30,CENTRO[1]-30, 20,60])
    '''
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()
