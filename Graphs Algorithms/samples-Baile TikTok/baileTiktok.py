"""Función que calcula el alcance de un vídeo en función de su calidad.
    Recibe como parámetros la calidad del vídeo, la red de contactos y el usuario que sube el vídeo.
    Devuelve el número de usuarios que podrían ver el vídeo siguiendo lo especificado en el pdf
    (1 = solo el usuario que lo sube, 2 = él y sus contactos, 3 = él, sus contactos y los contactos de sus contactos, etc..."""

def get_reach(danceQuality, network, user, seen=set()):
    if danceQuality == 1:
        reach={user}
        return reach
    elif danceQuality == 2:
        network[user].add(user)
        return network[user]
    else:
        reach = set(network[user])
        if user not in seen:
            seen.add(user)
        for contact in network[user]:
            if contact not in seen:
                seen.add(contact)
                reach |= get_reach(danceQuality - 1, network, contact, seen)
        if user not in reach:
            reach.add(user)
        return reach

# Ejemplo de uso
dances = int(input())
solutions = []
for i in range(dances):

    danceQuality, people, relations = map(int, input().split(" "))
    adj = [set() for i in range(people)]
    for j in range(relations):
        user1, user2 = map(int, input().split(" "))
        adj[user1].add(user2)
        adj[user2].add(user1)
    seen=set()
    reach = get_reach(danceQuality, adj, 0, seen)
    solutions.append(len(reach))

# print(*solutions) Lo printaría todo en una línea bien separado.
# No funciona si la lista contiene sets.
for reach in solutions:
    print(reach)