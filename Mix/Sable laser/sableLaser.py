import copy

# Queremos el máximo de componentes con el mínimo de pasos
def labVA(lab, inicio, final, pasosAct, numComponentesMax, numComponentes, visited, mejorSol):
    if lab[inicio[0]][inicio[1]] == 'e':
        if numComponentes > numComponentesMax:
            mejorSol[0] = numComponentes
            mejorSol[1] = pasosAct
            numComponentesMax = numComponentes
        elif numComponentes == numComponentesMax:
            mejorSol[1] = min(pasosAct, mejorSol[1])
    else:
        for i in range(len(dirs)):
            updatedComponent = False
            newF = inicio[0] + dirs[i][0]
            newC = inicio[1] + dirs[i][1]
            if esFactible(lab, newF, newC, visited):
                visited.add((newF,newC))
                if lab[newF][newC] == 'x':
                    numComponentes+=1
                    updatedComponent = True
                mejorSol, numComponentesMax = labVA(lab,(newF,newC), final, pasosAct+1, numComponentesMax, numComponentes, visited, mejorSol)
                visited.remove((newF,newC))
                if updatedComponent:
                    numComponentes-=1
    return mejorSol, numComponentesMax

def esFactible(lab, newF, newC, visited):
    if 0<=newF<len(lab) and 0<=newC<len(lab[0]):
        return (lab[newF][newC] == 'f' or lab[newF][newC] == 'x' or lab[newF][newC] == 'e') \
            and (newF,newC) not in visited
    else:
        return False

# Recogemos laberinto
dirs = [[1,0],[0,1],[-1,0],[0,-1]]
n, m = map(int,input().strip().split())
lab=[]
inicio = (0,0)
final = (0,0)
for i in range(n):
    fila = list(input().strip().split())
    lab.append(fila)
    for j,casilla in enumerate(fila):
        if casilla == 's':
            inicio = (i,j)
        if casilla == 'e':
            final = (i,j)

# Una vez leido el laberinto, preparamos enemigos
# (Convertimos la casilla que vigilan en pared, por la que no es factible pasar.
for i in range(n):
    for j in range(m):
        casilla = lab[i][j]
        if casilla == 'u':
            lab[i][j] = 'w'
            if i-1>=0:
                lab[i-1][j] = 'w'
        if casilla == 'd':
            lab[i][j] = 'w'
            if i+1<len(lab):
                lab[i+1][j] = 'w'
        if casilla == 'l':
            lab[i][j] = 'w'
            if j-1>=0:
                lab[i][j-1] = 'w'
        if casilla == 'r':
            lab[i][j] = 'w'
            if j+1<len(lab[0]):
                lab[i][j+1] = 'w'

visited = set()
visited.add(inicio)
mejorSol = [0, 0x3f3f3f]

mejorSol, numComponentesMax = labVA(lab, inicio, final, 0, 0, 0, visited, mejorSol)

print(*mejorSol)
