numCartas, riesgoMax = map(int, input().split(" "))

cartas = []

for i in range(numCartas):
    cartas.append(input().split())
    cartas[i].append(int(cartas[i][2]) / int(cartas[i][1]))

cartas = sorted(cartas, key=lambda x : x[3], reverse=True)
i = 0
while riesgoMax > 0 and i<len(cartas):
    print(cartas[i][0], end=" ")
    riesgoMax -= int(cartas[i][1])
    i += 1
