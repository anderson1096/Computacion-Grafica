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



#Funcion para transladar un punto
def transladar(c,p):
    px = c[0] + p[0]
    py = c[1] - p[1]
    return px,py

#Funcion para transladar una lista de puntos
def trans_points(puntos,c):
    trans = []
    for p in puntos:
        px = c[0] + p[0]
        py = c[1] - p[1]
        trans.append([px,py])
    return trans

#Funcion para rotar un punto
def rotar_punto(punto,angulo):
    rad = math.radians(angulo)
    xr = punto[0] * math.cos(rad) - punto[1] * math.sin(rad)
    yr = punto[0] * math.sin(rad) + punto[1] * math.cos(rad)
    return int(xr),int(yr)

#Funcion para rotar una lista de puntos
def rotar_lpuntos(puntos, angulo):
    rot = []
    rad = math.radians(angulo)
    for punto in puntos:
        xr = punto[0] * math.cos(rad) - punto[1] * math.sin(rad)
        yr = punto[0] * math.sin(rad) + punto[1] * math.cos(rad)
        rot.append((int(xr),int(yr)))
    return rot

#Funcion para generar una matriz aleatoria dado su tamano
def matriz_aleatoria(tamf, tamc):
    cont = 0
    m = []
    for i in range(tamf):
        f = []
        valor = random.randrange(5)
        f.append(valor)
        m.append(f)
        for j in range(tamc-1):
            valor2 = random.randrange(5)
            m[i].append(valor2)
    return m

#Funcion para sumar dos matrices
def suma_matrices(matriz1, matriz2):
    aux = len(matriz1)
    res = matriz_aleatoria(len(matriz1),len(matriz1))
    for i in range(aux):
        for j in range(aux):
            res[i][j] = matriz1[i][j] + matriz2[i][j]
    return res

#Funcion para construir una lista de tamano n (vector)
def vector(n):
    vec = []
    for i in range(n):
        vec.append(0)
    return vec

#Funcion que suma las filas de una matriz
def suma_filas(matriz1):
    res = vector(len(matriz1[0]))
    aux = len(matriz1)
    for i in matriz1:
        for j in range(len(res)):
            res[j] += i[j]

    return res

#Funcion que calcula la transpuesta de una matriz
def transpuesta(matriz):
    res = matriz_aleatoria(len(matriz[0]),len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            res[j][i] = matriz[i][j]
    return res

#Funcion que calcula la opuesta de una matriz
def opuesta(matriz):
    aux = len(matriz)
    for i in range(aux):
        for j in range(aux):
            matriz[i][j] = matriz[i][j] * (-1)
    return matriz

#Funcion para imprimir una matriz
def imprimir(matriz):
    for fila in matriz:
        print fila

#Funcion para sacar el angulo entre vectores
def angulo(vector1,vector2):
    a = math.fabs(punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    print b
    t = math.acos(a/b)
    return math.degrees(t)

#funcion que dibuja el plano cartesiano
def Dibujarejes(screen, c, al, an):
    pygame.draw.line(screen, ROJO, (0,c[1]),(an,c[1]),1)
    pygame.draw.line(screen, ROJO, (c[0],0),(c[0],al),1)

#funcion que pinta un vector en el plano
def cartesiano(screen,c,p,color):
    px = c[0] + p[0]
    py = c[1] - p[1]
    pygame.draw.line(screen,color,c,(px,py),1)

#Funcion que suma dos vectores
def suma(vec1,vec2):
    x = vec1[0] + vec2[0]
    y = vec1[1] + vec2[1]
    return x,y

#Funcion para determinar un vector dados dos puntos
def vector(point1,point2):
    vec = (point2[0] - point1[0],point2[1]-point1[1])
    return vec

#Funcion para dibujar una lista de puntos en pantalla
def dibujar_puntos(points, screen):
    for p in points:
        pygame.draw.circle(screen, NEGRO, p, )

#Funcion que determina la norma de un vector
def norma(vec):
    n = math.sqrt(vec[0]**2 + vec[1]**2)
    return n

#Funcion que determina la distancia entre dos puntos
def distancia(point1,point2):
    a = point2[0]-point1[0]
    b = point2[1]-point1[1]
    dis = math.sqrt(a**2 + b**2)
    return dis

#Funcion para retornar el producto punto entre dos vectores
def punto(vec1,vec2):
    res = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    return res

#Funcion para sacar el angulo entre vectores
def angulo(vector1,vector2):
    a = math.fabs(punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    print b
    t = math.acos(a/b)
    return math.degrees(t)

#Funcion para construir una matriz de tamano lon ingresando cada valor
def Matriz(lon):
    d = [0]*lon
    for i in range(lon):
        d[i] = [0]*lon
    for i in range(lon):
        for j in range(lon):
            d[i][j] = int(raw_input("Numero: "))

    return d

#Funcion para construir un vector de tamano lon ingresando cada valor
def Vector(lon):
    d = [0]*lon
    for i in range(lon):
        d[i] = int(raw_input("Numero: "))

    return d

#Funcion para multiplicar un vector por una matriz
def Multiplicar(matriz, vector, lon):
    res = [0]*lon
    aux = 0;
    for i in range(lon):
        for j in range(lon):
            res[i] += matriz[i][j] * vector[j]
    print "Matriz Origen: "
    for i in matriz:
        print i
    print "Vector Origen: "
    for i in vector:
        print "[%d]" % i
    print "Resultado: "
    for i in res:
        print "[%d]" % i

#Funcion que determina si dos vectores son paralelos
def paralelismo(vector1, vector2):
    aux1 = vector1[1]/vector2[1]
    tol = aux1 * 0.05
    abajo = aux1 - tol
    arriba = aux1 + tol
    aux2 = vector1[0]/vector2[0]
    if aux2 >= abajo and aux2 <= arriba:
        return 1
    else:
        return 0

#Funcion que determina si dos vectores son perpendiculares
def perpendicular(vector1, vector2):
    aux = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    if aux == 0:
        print "Si son perpendiculares"
    else:
        print "No son perpendiculares"


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

#Funcion que determina los tres angulos de un triangulo
def angulos_triangulo(pos1,pos2,pos3):
    vec1 = modulo.vector(pos1,pos2)
    vec2 = modulo.vector(pos2,pos3)
    vec3 = modulo.vector(pos3,pos1)
    angulo1 = modulo.angulo(vec1,vec2)
    angulo2 = modulo.angulo(vec2,vec3)
    angulo3 = modulo.angulo(vec3,vec1)
    print angulo1,angulo2,angulo3


#Funcion que dado un radio y un angulo retorne la posicion en x,y de se punto
def polares_cartesianas(r, angulo):

    #angulo = math.radians(angulo)
    aux_x = math.cos(angulo)
    aux_y = math.sin(angulo)
    x = int(r * aux_x)
    #x = r * aux_x
    y = int(r * aux_y)
    #y = r * aux_y
    return x,y


#Funcion que dado un radio y un angulo retorne la posicion en x,y de se punto
def cartesianas_polares(x,y):
    #calculando el radio
    r = math.sqrt(x**2 + y**2)

    #calculando el angulo
    if x > 0 and y >= 0:
        angulo = math.degrees(math.atan(y/x))
    elif x == 0 and y > 0:
        angulo = math.pi/2
    elif x < 0:
        angulo = math.atan(y/x) + math.pi
    elif x == 0 and y < 0:
        angulo = (3 * math.pi)/2
    elif x > 0 and y < 0:
        angulo = math.atan(y/x) + 2*math.pi

    return int(r), int(angulo)


def draw(screen, NEGRO, CENTRO):
    pygame.draw.ellipse(screen, NEGRO,[CENTRO[0]-130,CENTRO[1] - 25, 130,60],1)
    pygame.draw.ellipse(screen, NEGRO, [CENTRO[0],CENTRO[1] - 25, 130,60],1)
#Funcion para dibujar un poligono de n lados iguales
def poligono_le(lados,anguloIni,radio):
    aux = 360 / lados
    l = [polares_cartesianas(radio, anguloIni)]
    angulo = anguloIni
    for i in range(1, lados):
        angulo += aux
        l.append(polares_cartesianas(radio, angulo))

    return l


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((ANCHO,ALTO))
    screen.fill(BLANCO)
    Dibujarejes(screen,CENTRO,ALTO,ANCHO)
    pygame.draw.circle(screen, VERDE, transladar(CENTRO,(0,0)),100,1)
    lista = poligono_le(5, 0, 100)
    listaT = trans_points(lista, CENTRO)
    print cartesianas_polares(0,100)
    pygame.draw.polygon(screen, VERDE, listaT)

    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
