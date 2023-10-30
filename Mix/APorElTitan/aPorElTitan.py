def selectMinDistance(distances, visited):
    bestItem = 0
    minDist = float('inf')
    # POR TODOS LOS NODOS
    for i in range(len(distances)):
        if i not in visited and minDist>distances[i]:
            bestItem = i
            minDist = distances[i]
    return bestItem


def dijkstra(anclajes, origen):
    distances = [float('inf')] *len(anclajes)
    visited = set()
    parent = [-1] * len(anclajes)

    distances[origen] = 0
    visited.add(origen)

    for start,end,weight in anclajes[origen]:
        distances[end] = weight
        parent[end] = start

    #TODOS LOS NODOS MENOS UNO
    for i in range(len(anclajes) - 1):
        nextNode=selectMinDistance(distances,visited)
        visited.add(nextNode)
        for start, end, weight in anclajes[nextNode]:
            if distances[end] > distances[start] + weight:
                distances[end] = distances[start] + weight
                parent[end]=start
    return parent



def main():
    numAnclajes, numUniones = map(int, input().strip().split())
    anclajes = [[] for i in range(numAnclajes)]
    solution = [0 for i in range(numAnclajes)]

    for i in range (numUniones):
        start, end, weight = map(int,input().strip().split())
        anclajes[start].append([start,end,weight])
        anclajes[end].append([end,start,weight])
    numTitanes = int(input())

    # Es mejor hace un dijkstra para cada origen sólo una vez
    # y guardarlo en otra lista parents_nodos.
    #Si no, si se repite el origen, se vuelve a hacer el dijkstra y pierdes eficiencia.
    #Voy a arreglarlo
    parents_total = [[] for i in range(numAnclajes)]
    for i in range(numAnclajes):
        parent = dijkstra(anclajes, i)
        parents_total[i] = parent
    for i in range(numTitanes):
        origen,final = map(int, input().strip().split())
        parent = parents_total[origen]
        p = parent[final]
        solution[final]+=1
        while p!=origen:
            solution[p]+=1
            p = parent[p]
        solution[origen]+=1

    print(*solution)

if __name__ == '__main__':
    main()