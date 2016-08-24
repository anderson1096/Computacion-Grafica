
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

def perpendicular(vector1, vector2):
    aux = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    if aux == 0:
        print "Si son perpendiculares"
    else:
        print "No son perpendiculares"


str1 = raw_input("Digite los valores de A, B y C (1er ecuacion): ").split(" ")
vector1 = (-int(str1[1]),int(str1[0]))
str2 = raw_input("Digite los valores de A, B y C (2da ecuacion): ").split(" ")
vector2 = (-int(str2[1]),int(str2[0]))

if paralelismo(vector1,vector2) == 1:
    print "Si son paralelas"
else:
    print "No son paralelas"

perpendicular(vector1,vector2)
