def solveCherloJolms(cases, max_cost):
    solution = [0] * len(cases)
    cost = 0
    i = 0
    while cost < max_cost:
        if cost + cases[i][1] <= max_cost:
            cost += cases[i][1]
            solution[cases[i][0]] = 1
            i += 1
        else:
            solution[cases[i][0]] = (max_cost - cost) / cases[i][1]
            cost = max_cost
    return solution


numCasos, maxDinero = map(int, input().split(" "))
casos = []
beneficios = []
for i in range(numCasos):
    w, v = map(int, input().split(" "))
    beneficios.append(v)
    casos.append([i, w, v, v / w])

casos = sorted(casos, key=lambda x: x[3], reverse=True)
solution = solveCherloJolms(casos, maxDinero)
totalGains = 0
for i in range(len(solution)):
    if solution[i] > 0:
        print(str(i), end=" ")
        totalGains += beneficios[i] * solution[i]
print("\n" + str(round(totalGains)))