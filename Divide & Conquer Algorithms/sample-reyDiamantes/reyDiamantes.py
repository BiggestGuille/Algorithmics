def binarySearch(data, low, high, search):
    if low > high:
        if low >= 0 and low < len(data):
            return low
        return -1
    mid = (low + high) // 2
    if search == data[mid]:
        return mid
    elif search < data[mid]:
        return binarySearch(data, low, mid - 1, search)
    else:
        return binarySearch(data, mid + 1, high, search)

def eliminar_jugadores(matriz, targets):
    # Ordenar la matriz de identificadores de jugador en orden ascendente
    matriz_ordenada = sorted(matriz)

    # Recopilar una lista de identificadores de jugadores en orden ascendente
    lista_jugadores = []
    for fila in matriz_ordenada:
        for jugador in fila:
            lista_jugadores.append(jugador)

    # Eliminar jugadores en orden ascendente, uno por uno
    for i in range(len(targets)):
        # Encontrar el índice del jugador más cercano al número dado por el rey
        index = binarySearch(lista_jugadores, 0, len(lista_jugadores)-1, targets[i])

        # Determinar la fila y columna del jugador a eliminar
        num = lista_jugadores[index]
        """
        cont1 = -1
        cont2 = -1
        for fila in matriz:
            cont1+=1
            cont2=-1
            for jugador in fila:
                cont2+=1
                if jugador==num:
                    # Poner en la matriz una X
                    matriz[cont1][cont2] = 'X'
        """
        for i, fila in enumerate(matriz):
            for j, jugador in enumerate(fila):
                if jugador == num:
                    matriz[i][j] = 'X'

        # Eliminar al jugador de la lista de jugadores
        del lista_jugadores[index]


# Leer el tamaño de la matriz
n = int(input())

# Leer la matriz de identificadores de jugador
matriz = []
for i in range(n):
    fila = list(map(int, input().strip().split()))
    matriz.append(fila)

# Leer los identificadores de los jugadores a los que se va a atacar
targets = list(map(int, input().strip().split()))

# Lo mismo, para tener ints.

# Eliminar a los jugadores correspondientes y mostrar la rejilla resultante
eliminar_jugadores(matriz, targets)

# Imprimir la rejilla resultante tras eliminar a los jugadores correspondientes
for fila in matriz:
    print(' '.join(str(jugador) for jugador in fila))