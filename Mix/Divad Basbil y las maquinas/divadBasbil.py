
# Algoritmo kruskal
def kruskal(grafo):
    edges = []
    for ady in grafo:
        for edge in ady:
            edges.append(edge)
    edges = sorted(edges, key=lambda x:x[2], reverse=True)

    finalEdges = []
    cost = 0
    visited = set()
    nodes = [i for i in range(len(grafo))]

    while len(edges)>0 and len(visited)<len(grafo):
        start, end, weight = edges.pop()
        if nodes[start]!=nodes[end]:
            finalEdges.append([start,end,weight])
            cost+=weight
            nodes = list(map(lambda x:x if x!=nodes[end] else nodes[start], nodes))
            visited.add(nodes[start])
    return cost, finalEdges



# Recogemos datos
numDroides, numUniones = map(int, input().strip().split())
grafo = [[] for i in range(numDroides)]
for i in range(numUniones):
    start, end, weight = map(int, input().strip().split())
    grafo[start].append([start,end,weight])

numInfo = int(input())
infoDroides = []
for i in range(numInfo):
    info = int(input())
    infoDroides.append(info)

#Calculamos kruskal (unión del grafo completo con el menor peso)
cost, finalEdges = kruskal(grafo)

#Coste total
print(cost)

#Preparamos datos sobre vecinos y gastos de cada droide pedido
sumaDroides = [0 for i in range(numInfo)]
droidesVecinos = [[] for i in range(numInfo)]
for i in range(numInfo):
    for start, end, weight in finalEdges:
        if start == infoDroides[i]:
            sumaDroides[i]+=weight
            droidesVecinos[i].append(end)
        elif end == infoDroides[i]:
            sumaDroides[i] += weight
            droidesVecinos[i].append(start)
        droidesVecinos[i].sort()

# Imprimimos resultados
for i in range(numInfo):
    print("{}:".format(sumaDroides[i]), end = ' ')
    for vecino in droidesVecinos[i]:
        print(vecino, end=' ')
    print()