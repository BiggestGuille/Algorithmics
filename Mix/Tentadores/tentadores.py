
def encontrarMediana(low, high, tentadores):
    lowInt = tentadores.index(low)
    highInt = tentadores.index(high)
    mid = (lowInt + highInt) // 2
    return mid

def binarySearch(tentadores, low, high, search):
    if low>high:
        return tentadores.index(low)
    mid = encontrarMediana(low, high, tentadores)
    mid2 = tentadores[mid]
    # No se permiten nombres repetidos
    # if mid == search
    if tentadores[mid] > search:
        if mid-1>=0:
            return binarySearch(tentadores, low, tentadores[mid-1],search)
        else:
            return 0
    else:
        if mid+1<len(tentadores):
            return binarySearch(tentadores, tentadores[mid+1], high,search)
        else:
            return len(tentadores)


numTentadores, numNuevosTentadores = map(int, input().strip().split())

tentadores = list(input().strip().split())
nuevosTentadores = []
"""
if "Cristian"<"Fran":
    print("Hola")
"""
for i in range(numNuevosTentadores):
    tentadores.sort()
    nuevosTentadores.append(input().strip())
    index = binarySearch(tentadores, tentadores[0], tentadores[len(tentadores)-1], nuevosTentadores[i])
    if index==len(tentadores):
        tentadores.append(nuevosTentadores[i])
    else:
        tentadores.insert(index,nuevosTentadores[i])
    print(nuevosTentadores[i]+": "+str(index))

print(*tentadores)
