import copy
from math import inf

def imprimirLab(lab):
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == -1:
                print("*", end="\t")
            else:
                print(lab[i][j], end="\t")
        print()
    print()


def inicializarMejorSol(lab):
    mejorSol = copy.deepcopy(lab)
    mejorSol[len(lab) - 1][len(lab[0]) - 1] = -1
    return mejorSol

def esSolucion(lab, f, c, numEspacios):

    return (f == len(lab)-1) and (c == len(lab[0])-1) and (lab[f][c]==numEspacios)

def esMejor(sol1, sol2):
    n = len(sol1)-1
    m = len(sol1[0])-1
    if sol2[n][m]==-1:
        return True
    else:
        return sol1[n][m] < sol2[n][m]

def esFactible(lab, f, c):
    if (0 <= f < len(lab)) and (0 <= c < len(lab[0])):
        return lab[f][c] == 0
    else:
        return False

def labVA(lab, mejorSol, f, c, k, numEspacios):
    if esSolucion(lab, f, c, numEspacios):
        if esMejor(lab, mejorSol):
            mejorSol = copy.deepcopy(lab)
    else:
        desp =[[1,0], [0,1], [-1,0], [0,-1]]
        i = 0
        for i in range(len(desp)):
            newF = f + desp[i][0]
            newC = c + desp[i][1]
            if esFactible(lab, newF, newC):
                lab[newF][newC] = k
                mejorSol = labVA(lab, mejorSol, newF, newC, k+1, numEspacios)
                lab[newF][newC] = 0

    return mejorSol




#Laberinto
numFilas = int(input())
numColumnas = numFilas
lab = []
numEspacios = 0
for i in range(numFilas):
    fila = list(map(int, input().strip().split()))
    for elemento in fila:
        if elemento==0:
            numEspacios+=1
    lab.append(fila)

mejorSol = inicializarMejorSol(lab)
f = 0
c = 0
k = 1

lab[f][c] = k
# VA es Vuelta Atrás (BT Back Tracking)
mejorSol = labVA(lab, mejorSol, f,c, k + 1, numEspacios)

if mejorSol[numFilas-1][numColumnas-1] == -1:
    print("NO")
else:
    print("SI")

# imprimirLab(mejorSol)