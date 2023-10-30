# Leer datos

mundos, caminos = map(int, input().split(" "))

g = [[] for i in range(mundos)]

for i in range(caminos):
    start, end, weight = map(int, input().split(" "))
    g[start].append((start, end, weight))

def kruskal(g):
    # Eliminar aristas duplicadas
    edges = []
    for adj in g:
        for edge in adj:
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
    return cost

print(kruskal(g))