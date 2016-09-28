def Matriz(lon):
    d = [0]*lon
    for i in range(lon):
        d[i] = [0]*lon
    for i in range(lon):
        for j in range(lon):
            d[i][j] = int(raw_input("Numero: "))

    return d

def Vector(lon):
    d = [0]*lon
    for i in range(lon):
        d[i] = int(raw_input("Numero: "))

    return d

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

M = Matriz(3)
V = Vector(3)
Multiplicar(M,V,3)
