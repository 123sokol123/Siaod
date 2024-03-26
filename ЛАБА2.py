def gauss_jordan_with_pivot(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        # Выбор ведущего элемента
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        # Приведение к единичной диагональной форме
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        b[i] /= pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]

    return b

# Пример использования
A = [[3, 1, -1],
     [1, 5, -1],
     [2, 0, 3]]
b = [-2, 8, 1]

x = gauss_jordan_with_pivot(A, b)
print("Решение:", x)
