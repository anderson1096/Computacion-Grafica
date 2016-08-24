
#Funcion para determinar un vector dados dos puntos
def vector(point1,point2):
    vec = (point2[0] - point1[0],point2[1]-point1[1])
    return vec
#Recibiendo los dos puntos
str1 = raw_input("Digite el primer punto: ").split(" ")
str2 = raw_input("Digite el segundo punto: ").split(" ")
point1 = (int(str1[0]),int(str1[1]))
point2 = (int(str2[0]),int(str2[1]))
v = vector(point1,point2)
#Calculo de las ecuaciones de la recta
print "Ecuacion Vectorial"
print "(X,Y) = ({0},{1}) + K({2},{3})".format(str1[0],str1[1],v[0],v[1])
print "Ecuacion Parametrica"
print "X = {0} + K{1}".format(str1[0],v[0])
print "Y = {0} + K{1}".format(str1[1],v[1])
