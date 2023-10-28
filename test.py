import math

def calcul_point(X2,X1,Y2,Y1,Z2,Z1) :
    x = X1 - X2
    print(x)
    x = x** 2
    print(x)
    y = Y1 + Y2
    print(y)
    y = y** 2
    print(y)
    z = Z1 - Z2
    print(z)
    z = z** 2
    print(z)
    t = x + y + z
    print(t)
    res = math.sqrt(t)
    print(res)
    res = round(res)
    print(res)
    return res

calcul_point(1,0,0,0,9,4)