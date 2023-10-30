def binarySearchPreAndNext(data, low, high, search):
    preAndNext = []
    if low > high:
        if high >= 0 and high < len(data):
            preAndNext.append(data[high])
        else:
            preAndNext.append('X')
        if low >= 0 and low < len(data):
            preAndNext.append(data[low])
        else:
            preAndNext.append('X')
        return preAndNext
    mid = (low + high) // 2
    if search == data[mid]:
        if mid - 1 >= 0:
            preAndNext.append(data[mid - 1])
        else:
            preAndNext.append('X')
        if mid + 1 < len(data):
            preAndNext.append(data[mid + 1])
        else:
            preAndNext.append('X')
        return preAndNext
    elif search < data[mid]:
        return binarySearchPreAndNext(data, low, mid - 1, search)
    else:
        return binarySearchPreAndNext(data, mid + 1, high, search)


# Datos

numNiveles = int(input())
niveles = list(map(int, input().strip().split()))
if len(niveles) != numNiveles:
    print("Error lista de niveles")
    exit()
numNivelesJugadores = int(input())
nivelesJugadores = list(map(int, input().strip().split()))
if len(nivelesJugadores) != numNivelesJugadores:
    print("Error lista de niveles")
    exit()

# Binary searches
for i in range(numNivelesJugadores):
    preAndNext = binarySearchPreAndNext(niveles, 0, numNiveles - 1, nivelesJugadores[i])
    print(*preAndNext)
