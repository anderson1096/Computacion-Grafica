import modulo

#Funcion para sacar el angulo entre vectores
def angulo(vector1,vector2):
    a = math.fabs(punto(vector1,vector2))
    b = norma(vector1) * norma(vector2)
    print b
    t = math.acos(a/b)
    return math.degrees(t)

str1 = raw_input("Digite los valores de A, B y C (1er ecuacion): ").split(" ")
vector1 = (-int(str1[1]),int(str1[0]))
str2 = raw_input("Digite los valores de A, B y C (2da ecuacion): ").split(" ")
vector2 = (-int(str2[1]),int(str2[0]))
print "Primera Ecuacion: {0}X + {1}Y + {2} = 0".format(int(str1[0]),int(str1[1]),int(str1[2]))
print "Segunda Ecuacion: {0}X + {1}Y + {2} = 0".format(int(str2[0]),int(str2[1]),int(str2[2]))
print "El angulo entre las rectas es: ", modulo.angulo(vector1,vector2)
