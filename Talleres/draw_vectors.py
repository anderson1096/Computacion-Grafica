import pygame
#Definicion dimensiones de la pantalla a mostrar
ANCHO = 500
ALTO = 500
#definicion de los colores en la escala RGB
BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
AZUL = [0,102,255]
ROSA = [255,51,255]
#definicion de las coordenadas del centro de mi plano cartesiano
CENTRO = (250,250)

#funcion que dibuja el plano cartesiano
def Dibujarejes(screen, c, al, an):
    pygame.draw.line(screen, ROJO, (0,c[1]),(an,c[1]),1)
    pygame.draw.line(screen, ROJO, (c[0],0),(c[0],al),1)
#funcion que pinta un vector en el plano
def cartesiano(screen,c,p,color):
    px = c[0] + p[0]
    py = c[1] - p[1]
    pygame.draw.line(screen,color,c,(px,py),1)

def suma(vec1,vec2):
    x = vec1[0] + vec2[0]
    y = vec1[1] + vec2[1]
    return x,y

#iniciando pygame
pygame.init()
screen = pygame.display.set_mode((ANCHO,ALTO))
screen.fill(BLANCO)
Dibujarejes(screen, CENTRO, ALTO, ANCHO)
pygame.display.flip()
str1 = raw_input("Inserte los valores de su primer vector (x,y): ").split(" ")
vector1 = (int(str1[0]),int(str1[1]))
str2 = raw_input("Inserte los valores de su segundo vector (x,y): ").split(" ")
vector2 = (int(str2[0]),int(str2[1]))
cartesiano(screen,CENTRO,vector2,ROSA)
pygame.display.flip()
cartesiano(screen,CENTRO,vector1,NEGRO)
pygame.display.flip()
cartesiano(screen,CENTRO, suma(vector1,vector2),AZUL)
pygame.display.flip()
print "AZUL: Vector resultante de la Suma"
print "NEGRO: Vector 1"
print "ROSA: Vector 2"

while 1:
    tecla = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
