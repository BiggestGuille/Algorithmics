import copy
from math import inf

def inicializarSol(datos):
    sol = {}
    sol['PesoAc'] = 0
    sol['ValorAc'] = 0
    sol['Objetos'] = [0] * datos['N']
    return sol

def asignar(sol, i, datos):
    sol['Objetos'][i] += 1
    sol['ValorAc'] += datos['Valor'][i]
    sol['PesoAc'] += datos['Peso'][i]
    return sol

def borrar(sol, i, datos):
    sol['Objetos'][i] -= 1
    sol['ValorAc'] -= datos['Valor'][i]
    sol['PesoAc'] -= datos['Peso'][i]
    return sol

def mejor(sol1, sol2):
    if sol1['ValorAc'] > sol2['ValorAc']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor

def esSolucion(sol, datos, k):
    sumaIdentificadores = 0
    for i in range(len(sol['Objetos'])):
        if sol['Objetos'][i] > 0:
            sumaIdentificadores+=(datos['Identificador'][i]*sol['Objetos'][i])

    if k >= datos['N']:
        return True

    min_weight = float('inf')
    for i in range(datos['N']):
        if not datos['picked'][i] and datos['Peso'][i] < min_weight:
            min_weight = datos['Peso'][i]

    return (sol['PesoAc'] + min_weight > datos['W']) and (sumaIdentificadores % 5) != 0

def esFactible(sol, i, datos):
    return sol['PesoAc'] + datos['Peso'][i] <= datos['W']

def mochilaVA(sol, mejorSol,datos, k):
    if esSolucion(sol, datos, k):
        mejorSol = mejor(sol, mejorSol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol, i, datos):
                sol = asignar(sol, i, datos)
                datos['picked'][i] = True
                mejorSol = mochilaVA(sol, mejorSol, datos, i+1)
                sol = borrar(sol, i, datos)
                datos['picked'][i] = False
    return mejorSol


datos = {}
datos['N'], datos['W'] = map(int, input().strip().split())
datos['Identificador'] = []
datos['Valor'] = []
datos['Peso'] = []
datos['picked'] = [False] * datos['N']

for i in range(datos['N']):
    id, valor, peso = map(int, input().strip().split())
    datos['Identificador'].append(id)
    datos['Valor'].append(valor)
    datos['Peso'].append(peso)

sol = inicializarSol(datos)
mejorSol = inicializarSol(datos)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
sumaValor = 0


print(mejorSol['ValorAc'])
#print(mejorSol)