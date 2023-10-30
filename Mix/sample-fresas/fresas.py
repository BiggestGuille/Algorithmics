def binarySearch(data, low, high, search, iteraciones):
    iteraciones+=1
    if low>high:
        return -1
    mid = (low + high)//2
    if search == data[mid]:
        return iteraciones
    elif search < data[mid]:
        return binarySearch(data, low, mid - 1, search, iteraciones)
    else:
        return binarySearch(data, mid + 1, high, search, iteraciones)


def iterations(data, iteraciones):
    if data != 1:
        data = data // 2
        iteraciones+=1
        return iterations(data,iteraciones)
    else:
        iteraciones+=1
        return iteraciones

cajas = []
n=0
while(n!=-1):
    n = int(input())
    if n > 1000000000:
        print("OUT OF BOUNDS")
    if n!=-1:
        cajas.append(n)


for i in range(len(cajas)):
    # data = [i for i in range(cajas[i])]
    data = cajas[i]
    iteraciones = 0
    #iteraciones = binarySearch(data, 0, len(data) - 1, len(data) - 1, iteraciones)
    iteraciones = iterations(data, iteraciones)
    print(iteraciones)