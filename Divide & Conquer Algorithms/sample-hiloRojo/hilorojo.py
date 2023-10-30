def binarySearch(data, start, end, search):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if search == data[mid]:
            return mid
        else:
            if search > data[mid]:
                return binarySearch(data, mid + 1, end, search)
            else:
                return binarySearch(data, start, mid - 1, search)


n = int(input())
'''
line = input().split()
data1 = [0] * n
for i in range(n):
    data1[i] = int(line[i])
m = int(input())
line = input().split()
data2 = [0] * m
for i in range(m):
    data2[i] = int(line[i])
'''
data1 = list(map(int, input().strip().split()))
m = int(input().strip())
data2 = list(map(int, input().strip().split()))
k = int(input())
for _ in range(k):
    q1, q2 = map(int, input().split())
    p1 = binarySearch(data1, 0, n - 1, q1)
    p2 = binarySearch(data2, 0, m - 1, q2)
    if p1 >= 0 and p2 >= 0:
        print(str(p1) + " " + str(p2))
    else:
        print("SIN DESTINO")
