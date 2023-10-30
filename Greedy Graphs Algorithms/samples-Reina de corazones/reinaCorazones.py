def selectMinDistance(distances, visited, paloBuscado, end):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        esBuenPalo = False
        for i in range(len(tipoJuegos)):
            if tipoJuegos[i][0] == str(end):
                if tipoJuegos[i][1] == paloBuscado:
                    esBuenPalo = True
        if esBuenPalo == True:
            if not visited[i] and distances[i] < minDist and esBuenPalo:
                minDist = distances[i]
                bestItem = i
    return bestItem


def dijkstra(g, origin, ordenJuegos, tipoJuegos):
    n = len(g)
    distances = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    paloBuscado = ordenJuegos.pop()

    for start, end, weight in g[origin]:
        esBuenPalo = False
        for i in range(len(tipoJuegos)):
            if tipoJuegos[i][0] == str(end):
                if tipoJuegos[i][1] == paloBuscado:
                    esBuenPalo = True
        if esBuenPalo==True:
            distances[end] = weight
            parent[end] = start
    for _ in range(2, len(g)):
        nextNode = selectMinDistance(distances, visited, paloBuscado, end)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            esBuenPalo = False
            for i in range(len(tipoJuegos)):
                if tipoJuegos[i][0] == str(end):
                    if tipoJuegos[i][1] == paloBuscado:
                        esBuenPalo = True
            if esBuenPalo == True:
                if distances[end] > distances[start] + weight:
                    distances[end] = distances[start] + weight
                    parent[end] = start

    return distances, parent



#Creación del grafo
juegos, calles, cases = map(int, input().strip().split())
g = []
for _ in range(juegos):
    g.append([])
for _ in range(calles):
    location1, location2, weight = map(int, input().strip().split())
    g[location1].append((location1, location2, weight))
    g[location2].append((location2, location1, weight))

tipoJuegos = []
for _ in range(juegos):
    tipoJuegos.append(input().split())
origen, final, orden = input().strip().split()
origen = int(origen)
final = int(final)
posicionBucle = len(orden)
ordenJuegos = []
for char in orden:
    ordenJuegos.append(char)
ordenJuegos.reverse()
cost = 0
contador = 0
finalList = []
while len(ordenJuegos)!=0:
    distances, parent = dijkstra(g, origen, ordenJuegos, tipoJuegos)
    edgeMenor = float('inf')
    for i in range(len(distances)):
        if distances[i]!=float('inf') and i>contador-1:
            seguir = True
            if edgeMenor>distances[i]:
                edgeMenor = distances[i]
                origen = i

    if seguir==True or len(ordenJuegos)==0:
        finalList.append(origen)
        finalValido = True
    else:
        print("No se puede llegar")
        finalValido = False

    contador+=1

if finalValido and finalList.pop()==final:
    for elemento in finalList:
        print(elemento, end=' ')
else:
    print("No se puede llegar")