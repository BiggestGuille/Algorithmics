# Leer datos
habitaciones, cables = map(int, input().split(" "))

g = [[] for i in range(habitaciones)]
finalEdges = []
roomCostList = []

for i in range(cables):
    start, end, weight = map(int, input().split(" "))
    g[start].append((start, end, weight))
    g[end].append((end, start, weight))

def kruskal(g):
    # Eliminar aristas duplicadas
    edges = []
    for adj in g:
        for edge in adj:
            if edge[1] > edge[0]:
                edges.append(edge)
    # Ordenar por peso y crear lista de nodos
    edges = sorted(edges, key= lambda x : x[2], reverse=True)
    nodes = [i for i in range(len(g))]
    visited_nodes = set()
    cost = 0

    # Bucle yendo uno por uno y sumando su coste.
    # Se actualizan los conjuntos disjuntos y se añaden a nodos visitados.
    # Se para cuando se hayan visitados todos o no queden aristas.

    while len(visited_nodes) < len(g) and len(edges) > 0:
        start, end, weight = edges.pop()
        if nodes[start] != nodes[end]:
            cost += weight
            finalEdges.append((start,end,weight))
            nodes = list(map(lambda x: x if x != nodes[end] else nodes[start], nodes))
            visited_nodes.add(nodes[start])
    return cost

costeTotal = kruskal(g)
print("Coste total:",costeTotal)
for i in range(habitaciones):
    roomCost = 0
    for j in range(len(finalEdges)):
        if i==finalEdges[j][0] or i==finalEdges[j][1]:
            roomCost+=finalEdges[j][2]
    # roomCost.append(roomCostList)
    print("H{}: {}".format(i, roomCost))




