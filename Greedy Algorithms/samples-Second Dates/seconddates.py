#Hace todos los ejemplos bien pero da error en el judge :(

# He llegado a la conclusión de que input().strip().split() es mejor
# porque da el mismo resultado pero elimina los espacios en blanco de forma automática.
numParticipantes, tamanoGrupo = map(int, input().split(" "))

participantes = list()

for i in range(numParticipantes):
    participantes.append(input().split())

participantes = sorted(participantes, key=lambda x : x[1])
sumaEdades1 = 0
sumaEdades2 = 0
sumaEdades3 = 0
sumaEdades4 = 0
grupo = 0

for i in range(tamanoGrupo):
    sumaEdades1 += int(participantes[i][1])
for i in range(len(participantes)-tamanoGrupo):
    sumaEdades2 += int(participantes[i+tamanoGrupo][1])

for i in range(tamanoGrupo):
    sumaEdades3 += int(participantes[len(participantes)-1-i][1])
for i in range(len(participantes)-tamanoGrupo):
    sumaEdades4 += int(participantes[i][1])

diferencia1 = sumaEdades2 - sumaEdades1
diferencia2 = sumaEdades3 - sumaEdades4

if diferencia1>diferencia2:
    grupo = 1
else:
    grupo = 2

if grupo == 1:
    for i in range(len(participantes)):
        # El tamaño del grupo 1 es 2, entonces en la tercera iteración se comienza con un enter
        if i == tamanoGrupo:
            print()
        print(participantes[i][0], end=" ")
else:
    for i in range(len(participantes)):
        if i == tamanoGrupo - 1:
            print()
        print(participantes[i][0], end=" ")
