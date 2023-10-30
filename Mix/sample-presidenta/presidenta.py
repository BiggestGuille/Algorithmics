
def kruskal(edges):
    nodes = [i for i in range(len(edges))]
    visited_nodes = set()
    edges = sorted(edges, key=lambda x:x[2], reverse=False)
    cost = 0
    finalEdges=[]

    while len(visited_nodes)<len(edges) and len(edges)>0:
        start, end, weight = edges.pop()
        if nodes[start]!=nodes[end]:
            cost+=weight
            finalEdges.append((start,end,weight))

numPueblos, numCarreteras = map(int, input().strip().split())
edges=[]
"""
No era necesario
cont=0
puebloAnterior="No"
for i in range(numCarreteras):
    puebloOrigen, puebloDestino, coste = input().strip().split()
    coste = int(coste)
    if puebloAnterior=="No":
        g[cont].append((puebloOrigen, puebloDestino, coste))
    else:
        if puebloAnterior==puebloOrigen:
            g[cont].append((puebloOrigen, puebloDestino, coste))
        else:
            cont+=1
            g[cont].append((puebloOrigen, puebloDestino, coste))
    puebloAnterior = puebloOrigen
"""

for i in range(numCarreteras):
    carretera = input().strip().split()
    carretera[2]=int(carretera[2])
    edges.append(carretera)

kruskal(edges)

print("Hola")