# N y M
vertices, relations = map(int, input().split(" "))

# Matriz de adyacencia del grafo
adj = [set() for i in range(vertices)]
# Costes (N líneas siguientes)
costs = [0]*vertices
for i in range(vertices):
    costs[i] = int(input())

# Tantas veces como relaciones haya
# a = vertex1 y b = vertex2 - Nodos directamente conectados
for i in range(relations):
    vertex1, vertex2 = map(int, input().split(" "))
    if vertex1<0 or vertex1>vertices or vertex2<0 or vertex2>vertices:
        exit("Invalid number of vertex")
    adj[vertex1].add(vertex2)
    adj[vertex2].add(vertex1)

# Vertices visitados
visited = set()


# Algorithm
# Básicamente si visited es completo excepto el nodo ignorado no es crítico.
# Si visited es menor, entonces era crítico porque no se ha llegado a todo.
# Para eso utilizamos dfs normal para mirar todo el grafo pero ignorando un nodo cada vez.
def search_cycle(node, ignore):
    if node == ignore:
        return
    visited.add(node)
    for i in adj[node]:
        if not i in visited:
            search_cycle(i, ignore)


totalCost = 0

# Esta primera comprobación se hace porque, ¿Qué pasa si quitamos el nodo 0?
# El resto comprueba que pasa si empezando desde el 0, qué pasa si quitamos otro nodo.
if vertices > 1:
    search_cycle(1, 0)
    if len(visited) < vertices-1:
        totalCost += costs[0]
    for i in range(1, vertices):
        visited = set()
        search_cycle(0, i)
        # Hasta vertices - 1 porque se está ignorando un nodo en cada bucle.
        if len(visited) < vertices-1:
            totalCost += costs[i]

print(totalCost)
