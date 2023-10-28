import math

positions_bloc =  [1, 0, 9]
positions_player = [0, 0, 7]

def calcul_point(X1,X2,Y1,Y2,Z1,Z2) :
    x = X1 - X2
    x = x** 2
    y = Y1 + Y2
    y = y** 2
    z = Z1 + Z2
    z = z** 2
    t = x + y + z
    res = math.sqrt(t)
    res = round(res)
    return res

print(calcul_point(positions_bloc[0], positions_player[0], positions_bloc[1], positions_player[1], positions_bloc[2], positions_player[2]))