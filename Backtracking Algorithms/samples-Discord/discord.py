
def inicializarSol(numEstudiantes):
    return [0] * numEstudiantes

def esSolucion(nodo, numEstudiantes):
    return nodo == numEstudiantes

def esFactible(grafo, sol, nodo, color):
    ady = grafo[nodo]
    i = 0
    factible = True
    while factible and i < len(ady):
        if ady[i] < nodo:
            factible = (color != sol[ady[i]])
        i += 1
    return factible

def coloreadoVA(grafo, sol, nodo, m, numEstudiantes):
    if esSolucion(nodo, numEstudiantes):
        esSol = True
    else:
        esSol = False
        color = 1
        while color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                (sol, esSol) = coloreadoVA(grafo, sol, nodo +1, m, numEstudiantes)
                if not esSol:
                    sol[nodo] = 0
                if esSol:
                    return sol, esSol
            color += 1
    return sol, esSol


numEstudiantes, numParejasComparten = map(int, input().strip().split())
grafo = [[] for i in range(numEstudiantes)]
for i in range(numParejasComparten):
    est1, est2 = map (int, input().strip().split())
    grafo[est1].append(est2)
    grafo[est2].append(est1)

numColores = 1
haySolution = False
while not haySolution:
    nodo = 0
    sol = inicializarSol(numEstudiantes)
    (sol, esSol) = coloreadoVA(grafo, sol, nodo, numColores, numEstudiantes)
    if esSol:
        #print(sol)
        haySolution=True
    else:
        #print("No hay solucion")
        numColores += 1

# Se pintará el número de colores necesarios para
# conseguir el coloreado, sumando uno a cada iteración.
print(numColores)