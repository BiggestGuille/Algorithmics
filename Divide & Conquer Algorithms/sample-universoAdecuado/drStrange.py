def binarySearchPreAndNext(data, low, high, search):
    preAndNext = []
    if low > high:
        if high >= 0 and high < len(data):
            preAndNext.append(data[high])
        else:
            preAndNext.append('VACIO')
        if low >= 0 and low < len(data):
            preAndNext.append(data[low])
        else:
            preAndNext.append('VACIO')
        return preAndNext
    mid = (low + high) // 2
    if search == data[mid]:
        if mid - 1 >= 0:
            preAndNext.append(data[mid - 1])
        else:
            preAndNext.append('VACIO')
        if mid + 1 < len(data):
            preAndNext.append(data[mid + 1])
        else:
            preAndNext.append('VACIO')
        return preAndNext
    elif search < data[mid]:
        return binarySearchPreAndNext(data, low, mid - 1, search)
    else:
        return binarySearchPreAndNext(data, mid + 1, high, search)


# Datos

universos = list(input().strip().split())

numSearch = int(input().strip())
universosSearch = []
for i in range(numSearch):
    universosSearch.append(input().strip())

# Quick sort sería posible
universos.sort()

# Binary searches
for i in range(numSearch):
    preAndNext = binarySearchPreAndNext(universos, 0, len(universos) - 1, universosSearch[i])
    print(*preAndNext)