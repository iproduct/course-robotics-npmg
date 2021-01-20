"""
Задача 3. Айсберг има форма, която може да се изобрази в таблица с N реда и N стълба, 7 < N < 200,
например айсбергът от фиг. 1 след един час в резултат на топенето се превръща в айсберга от фиг. 2:
 _ _ _ _ _ _ _ _      _ _ _ _ _ _ _ _        
|_|_|_|_|_|_|_|_|    |_|_|_|_|_|_|_|_|
|_|_|█|█|_|_|_|_|    |_|_|_|_|_|_|_|_|
|_|_|█|█|_|█|█|_|    |_|_|█|█|_|_|_|_|
|_|█|█|█|█|█|█|_|    |_|_|█|█|█|█|_|_|
|_|█|█|█|█|█|_|_|    |_|█|█|█|█|█|_|_|
|_|█|█|_|█|█|_|_|    |_|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|_|    |_|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|_|    |_|_|_|_|_|_|_|_|    фиг. 1                фиг. 2
Клетките от първия и последния ред и стълб са винаги празни. 
Външните клетки, които са изложени на съприкосновение с топлия въздух и вода се топят,  а вътрешните не.
Айсбергът се топи по следното правило: всяка клетка която има поне 2 от съседните 4 клетки (с обща страна) празни
се стопява изцяло за 1 час, а останалите клетки не се топят изобщо.
Напишете програма, която прочита от текстов файл размера и съдържанието на таблицата - например:
8
00000000
00**0000
00**0**0
0******0
0*****00
0**0**00
00000000
00000000

3
000
000
000

3
000
0*0
000

3
**0
**0
000
В резултат програмата следва да извежда на екрана броя часове, за които айсбергът ще се разтопи изцяло.
В горния пример изходът на програмата следва да бъде: 4.
"""

from copy import deepcopy

# This works even with tables which have filled cells around the edges
def should_melt(matrix, row, col):
    if matrix[row][col] == '0':
        return True

    size = len(matrix)
    shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adjacent_empty = 0
    for drow,dcol in shifts:
        next_row = row + drow
        next_col = col + dcol
        if 0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] == '0':
            adjacent_empty += 1

    if adjacent_empty >= 2:
        return True
    return False

def melt_once(current, following):
    melted = 0
    for row in range(len(current)):
        for col in range(len(current[row])):
            if current[row][col] == '*' and should_melt(current, row, col):
                melted += 1
                following[row][col] = '0'
            elif current[row][col] == '0':
                following[row][col] = '0'
            else:
                following[row][col] = '*'

    return melted

def melt(matrix):
    copy = deepcopy(matrix)
    melts = 0
    while True:
        melted = melt_once(matrix, copy)
        print_grid(matrix)
        matrix, copy = copy, matrix
        if melted == 0:
            break
        melts += 1

    return melts

def print_grid(grid):
    for line in grid:
        print(line)
    print()

if __name__ == '__main__':
    file = open('grid.txt', 'r')
    lines = file.readlines()
    size = int(lines[0])
    matrix = []
    for i in range(size):
        matrix.append(list(lines[i+1].strip()))

    turns = melt(matrix)
    print(turns)

