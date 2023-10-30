
import copy


def imprimirSudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=' ')
        print()
    print()


def is_feasible(data, num, i, j):
    return not data['row'][i][num] and not data['column'][j][num] and not data['square'][i // 3][j // 3][num]


def solve_sudoku(data, tile):
    if tile == len(data['numHuecos']):
        if data['solNumber'] == 0:
            data['solution'] = copy.deepcopy(data['sudoku'])
        data['solNumber'] += 1
    else:
        if data['solNumber'] < 2:
            i, j = data['numHuecos'][tile]
            number = data['sudoku'][i][j]
            while number < 9:
                number += 1
                if is_feasible(data, number, i, j):
                    data['sudoku'][i][j] = number
                    data['row'][i][number] = True
                    data['column'][j][number] = True
                    data['square'][i // 3][j // 3][number] = True

                    data = solve_sudoku(data, tile + 1)

                    if data['solNumber'] < 2:
                        number = data['sudoku'][i][j]
                        data['sudoku'][i][j] = 0
                        data['row'][i][number] = False
                        data['column'][j][number] = False
                        data['square'][i // 3][j // 3][number] = False
    return data


def main():
    datos = {
        'solNumber': 0,
        'numHuecos': [],
        'row': [[False] * 10 for _ in range(9)],
        'column': [[False] * 10 for _ in range(9)],
        'square': [[[False] * 10 for _ in range(3)] for _ in range(3)],
        'sudoku': [[] for _ in range(9)],
        'solution': None
    }

    for row in range(9):
        datos['sudoku'][row] = list(map(int, input().strip().split()))

    for i in range(9):
        for j in range(9):
            number = datos['sudoku'][i][j]
            if number != 0:
                datos['row'][i][number] = True
                datos['column'][j][number] = True
                datos['square'][i // 3][j // 3][number] = True
            else:
                datos['numHuecos'].append((i, j))

    datos = solve_sudoku(datos, 0)

    if datos['solNumber'] == 0:
        print('imposible')
    elif datos['solNumber'] == 1:
        imprimirSudoku(datos['solution'])
    else:
        print('casi sudoku')


if __name__ == "__main__":
    main()
