def selectMinDistance(distances, visited):
    minDist = float('inf')
    bestItem = 0
    for i in range(1, len(distances)):
        if not visited[i] and distances[i] < minDist:
            minDist = distances[i]
            bestItem = i
    return bestItem


def dijkstra(g, origin):
    n = len(g)
    distances = [float('inf')] * n
    parent = [-1] * n
    visited = [False] * n

    distances[origin] = 0
    visited[origin] = True

    for start, end, weight in g[origin]:
        distances[end] = weight
        parent[end] = start
    for _ in range(2, len(g)):
        nextNode = selectMinDistance(distances, visited)
        visited[nextNode] = True
        for start, end, weight in g[nextNode]:
            if distances[end] > distances[start] + weight:
                distances[end] = distances[start] + weight
                parent[end] = start

    return distances, parent


#Creación del grafo
n, m = map(int, input().strip().split())
g = []
# Es así porque empieza en 1 y no en 0.
for _ in range(n+1):
    g.append([])
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    g[u].append((u, v, w))
    g[v].append((v, u, w))

distances, parent = dijkstra(g, 1)
cases, maxDist = map(int, input().strip().split())
for _ in range(cases):
    p = int(input().strip())
    while p != 1:
        if distances[p] <= maxDist:
            print(p, end=" ")
        p = parent[p]
    print()