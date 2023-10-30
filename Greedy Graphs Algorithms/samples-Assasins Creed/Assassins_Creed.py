def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(len(distances)):
        if not visited[i] and distances[i] < minDist and i not in zonasDinReal:
            minDist = distances[i]
            bestItem = i
    return bestItem


def dijkstra(g, origen):
    n = len(g)
    distances = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    distances[origen] = 0
    visited[origen] = True

    for start, end, weight in g[origen]:
        if end not in zonasDinReal:
            distances[end] = weight
            parent[end] = start
    #   Lo mismo que len(g) - 1
    for _ in range(1, len(g)):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if end not in zonasDinReal:
                if distances[end] > distances[start] + weight:
                    distances[end] = distances[start] + weight
                    parent[end] = start

    return distances, parent


#Creación del grafo
n, m = map(int, input().strip().split())
g = [[] for i in range(n)]
#Hasta n porque empieza en 0

for _ in range(m):
    u, v, w = map(int, input().strip().split())
    g[u].append([u, v, w])
    g[v].append([v, u, w])

numZonasDinReal = int(input())
zonasDinReal = set(map(int, input().split()))
cost = 0
origen, final = map(int, input().strip().split())

distances, parent = dijkstra(g, origen)

if distances[final]==float('inf'):
    print("IMPOSIBLE")
else:
    cost+=distances[final]
    print(cost)