# Número de pilotes y conexiones entre ellos
participantsNumber, attractions = map(int, input().split(" "))

# Creamos una lista de adyacencia para representar las conexiones entre los pilotes
participants = [[] for i in range(participantsNumber)]
for i in range(attractions):
    a, b = map(int, input().split(" "))
    participants[a].append(b)

for i in range(participantsNumber):
    visitados = [False] * participantsNumber
    if visitados[i]:
        continue
    stack = [i]
    # La stack va recogiendo todos los vecinos de un pilote, pone el visitado
    # en true y sigue con sus vecinos.
    while stack:
        participant = stack.pop()
        visitados[participant] = True
        for vecino in participants[participant]:
            if not visitados[vecino]:
                stack.append(vecino)
    for bool in visitados:
        if bool==False:
            print("HAY QUE REPETIR")
            exit()

print("CASTING COMPLETO")





