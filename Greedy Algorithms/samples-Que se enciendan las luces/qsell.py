def solveQSELL(parejas, tiempoMax):
    solution = [0] * len(parejas)
    tiempo = 0
    i = 0
    while tiempo < tiempoMax and i<len(solution):
        if tiempo + int(parejas[i][4]) <= tiempoMax:
            tiempo += int(parejas[i][4])
            solution[i] = 1
            i += 1
        else:
            solution[i] = (tiempoMax - tiempo) / int(parejas[i][4])
            tiempo = tiempoMax
    return solution


concursantes = int(input())
# Bucle concursantes
for i in range(concursantes):
    caracteristica = input()
    while caracteristica!= "kindness" and caracteristica!="intelligence" and caracteristica!="beauty":
        caracteristica = input()
    tiempoMax = int(input())
    posiblesParejas = int(input())
    parejas = []
    for i in range(posiblesParejas):
        parejas.append(input().split())
        if caracteristica=="kindness":
            tipoBeneficio=3
            parejas[i].append(int(parejas[i][4])/int(parejas[i][3]))
        elif caracteristica=="intelligence":
            tipoBeneficio = 2
            parejas[i].append(int(parejas[i][4])/int(parejas[i][2]))
        elif caracteristica=="beauty":
            tipoBeneficio = 1
            parejas[i].append(int(parejas[i][4])/int(parejas[i][1]))
    parejas = sorted(parejas, key=lambda case: case[5], reverse=False)

    solution = solveQSELL(parejas, tiempoMax)

    beneficioTotal = 0
    for i in range(len(solution)):
        if solution[i] > 0:
            print(parejas[i][0], end=" ")
            beneficioTotal += int(parejas[i][tipoBeneficio]) * solution[i]
    print("\n" + "{:.2f}".format(float(beneficioTotal)))
    # El problema de print("\n" + str(round(float(beneficioTotal),2))) es que si es .00 solo sale un decimal.