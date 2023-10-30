clientes = int(input())

matrix = [0]*clientes

# Load data
for i in range(clientes):
    cliente, tiempo = map(int, input().split(" "))
    matrix[i] = tiempo

matrix.sort()

sumWaitingTimes = 0
addWaitingTimeQueue = 0
for i in matrix:
    sumWaitingTimes += i
    addWaitingTimeQueue += sumWaitingTimes

print(addWaitingTimeQueue)

