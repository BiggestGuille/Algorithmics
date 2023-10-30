# N y M
amigos, relaciones = map(int, input().split(" "))

# Matriz de adyacencia del grafo
adj = [set() for i in range(amigos)]

# Tantas veces como relaciones haya
# a = amigo1 y b = amigo2 - Nodos directamente conectados
for i in range(relaciones):
    amigo1, amigo2 = map(int, input().split(" "))
    if amigo1 < 0 or amigo1 > amigos or amigo2 < 0 or amigo2 > amigos:
        exit("Invalid number of vertex")
    adj[amigo1].add(amigo2)
    adj[amigo2].add(amigo1)

# Vertices visitados
visited = set()
gruposAmigos = set()
gruposAmigos2 = []
listaFinal = set()


# Algorithm
def search_cycle(node):
    visited.add(node)
    for i in adj[node]:
        if i not in visited:
            search_cycle(i)


if amigos > 1:
    for i in range(0, amigos):
        visited = set()
        search_cycle(i)
        # gruposAmigos.add(frozenset(visited))
        if visited not in gruposAmigos2:
            gruposAmigos2.append(visited)

""" 
gruposAmigos = [sorted(map(int, elemento)) for elemento in gruposAmigos] # Ordenar los números en cada grupo
listaFinal = set(" ".join(str(nodo) for nodo in elemento) for elemento in gruposAmigos) # Unir los números en una cadena y convertir a conjunto

# Convertir elementos a tuplas de enteros
listaFinal = set(tuple(map(int, elemento.split())) for elemento in listaFinal)
listaFinalOrdenada = sorted(listaFinal, key=lambda x: x[0])
for elemento in listaFinalOrdenada:
    numeros = list(map(str, elemento))
    cadena = " ".join(numeros)
    print(cadena)
"""
for elemento in gruposAmigos2:
    numeros = list(map(str, elemento))
    cadena = " ".join(numeros)
    print(cadena)
