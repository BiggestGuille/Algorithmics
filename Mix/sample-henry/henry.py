def obtenerEdges(matriz,n,m):
    edges = []
    grafo = {i*m+j: [] for i in range(n) for j in range(m)}
    valorEdges = []
    cont=0
    for i in range(n):
        for j in range(m):
            #Lista de nodos y valores de nodos
            edges.append(cont)
            valorEdges.append(matriz[i][j])
            cont+=1

            #Aristas del grafo
            # Arista hacia arriba
            if i > 0:
                grafo[i * m + j].append((i * m + j, (i - 1) * m + j, 1))
            # Arista hacia la izquierda
            if j > 0:
                grafo[i * m + j].append((i * m + j, i * m + j - 1, 1))
            #Si no estamos en la última fila, arista hacia abajo
            if i < n - 1:
                grafo[i*m+j].append((i * m + j,(i+1)*m+j, 1)) # Arista hacia abajo
            #Si no estamos en la última columna, arista hacia la derecha
            if j < m - 1:
                grafo[i*m+j].append((i * m + j,i*m+j+1, 1)) # Arista hacia la derecha
    return edges, valorEdges, grafo

def encontrarFinal(edges,valorEdges):
    for i in range(len(edges)):
        if valorEdges[i]==2:
            return i

def selectMinDistance(distances,visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(len(visited)):
        if not visited[i] and distances[i]<minDist:
            minDist=distances[i]
            bestItem=i
    return bestItem

def cerrarMuros(grafo,valorEdges,nextNode,m):
    for adj in grafo:
        cont = 0
        for start,end,weight in grafo[adj]:
            if (valorEdges[end]==-1 or valorEdges[start]==-1) and (start!=nextNode and end!=nextNode) and (start!=1 and end!=1 and start!=m and end!=m):
                del grafo[adj][cont]
            cont+=1


def dijkstra(grafo,origen,edges,valorEdges,turno,m):
    distances = [float('inf')] * len(grafo)
    parent = [-1] * len(grafo)
    grafoAux = grafo
    visited = [False] * len(grafo)

    nextNode=0
    distances[origen]=0
    visited[origen]=True

    for start,end,weight in grafo[origen]:
        distances[end] = weight
        parent[end] = start

    for i in range(1, len(grafo)):
        turno+=1
        if turno%2==0:
            cerrarMuros(grafo,valorEdges,nextNode,m)
        else:
            #Abrir muros
            grafo = grafoAux
        nextNode=selectMinDistance(distances,visited)
        visited[nextNode]=True
        for start, end, weight in grafo[nextNode]:
            if distances[end] > distances[start] + weight:
                distances[end] = distances[start] + weight
                parent[end] = start
    return distances, parent



n , m = map(int, input().strip().split())
matriz = []
for i in range(n):
    fila = list(map(int, input().strip().split()))
    matriz.append(fila)

edges, valorEdges, grafo = obtenerEdges(matriz,n,m)
origen=0
final = encontrarFinal(edges,valorEdges)
turno = 1

distances, parent = dijkstra(grafo,origen,edges,valorEdges,turno,m)
print(distances[final])
"""
#Buscar siguiente iteración
valorAux = float('inf')
for i in range(len(distances)):
    if distances[i]==1:
        distancesAux, parentAux = dijkstra(grafo, i, edges, valorEdges)
        if distancesAux[final] < valorAux:
            valorAux = distancesAux[final]
            origen = i
"""
