# Número de pilotes y conexiones entre ellos
pilotesNumber, pilotesConnected = map(int, input().split(" "))

# Creamos una lista de adyacencia para representar las conexiones entre los pilotes
pilotes = [[] for i in range(pilotesNumber)]
for i in range(pilotesConnected):
    a, b = map(int, input().split(" "))
    pilotes[a].append(b)
    pilotes[b].append(a)

# Usamos una lista de visitados para evitar contar pilotes dos veces
visitados = [False] * pilotesNumber

# Contamos el número de cucharadas necesarias para comerse todos los pilotes
cucharadas = 0
for i in range(pilotesNumber):
    if visitados[i]:
        continue
    cucharadas += 1
    stack = [i]
    # La stack va recogiendo todos los vecinos de un pilote, pone el visitado
    # en true y sigue con sus vecinos.
    while stack:
        pilote = stack.pop()
        visitados[pilote] = True
        for vecino in pilotes[pilote]:
            if not visitados[vecino]:
                stack.append(vecino)

print(cucharadas)