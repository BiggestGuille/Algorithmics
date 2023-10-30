numAsignaturas, numPruebas = map(int, input().split(" "))

asignaturas = [0] * numAsignaturas

for i in range(numAsignaturas):
    asignatura, tiempo = map(int, input().split(" "))
    asignaturas[i] = tiempo

asignaturas.sort()

pruebas = []
tiempoPorAsignatura = 0
colaTiempoTotal = 0

for i in asignaturas:
    tiempoPorAsignatura += i
    colaTiempoTotal += tiempoPorAsignatura

for i in range(numPruebas):
    pruebas.append(int(input()))
    if colaTiempoTotal<=pruebas[i]:
        print("APROBADO")
    else:
        print("SUSPENSO")

