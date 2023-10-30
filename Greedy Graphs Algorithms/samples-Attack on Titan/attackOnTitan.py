# Leer datos

puestos, telefericos = map(int, input().split(" "))

g = [[] for i in range(puestos)]

for i in range(telefericos):
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
            nodes = list(map(lambda x : x if x != nodes[end] else nodes[start], nodes))
            visited_nodes.add(nodes[start])
            #visited_nodes.add(nodes[end])
    return(cost)

minimaLongitud = kruskal(g)
minimoCoste = (minimaLongitud//5) + 1

print(minimoCoste)