# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

for col in range(len(matrix)):
    print('\n')
    for string in range(len(matrix[col])):
        print(matrix[col][string], end=' ')

for string in range(len(matrix[col])):
    print('\n')
    for col in range(len(matrix)):
        print(matrix[col][string], end=' ')


