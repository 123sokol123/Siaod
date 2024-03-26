import numpy as np

# Определение коэффициентов матрицы системы уравнений
A = np.array([[3, 1, -1],
             [1, 5, -1],
             [2, 0, 3]])

# Определение вектора правой части системы
b = np.array([-2, 8, 1])

def seidel_method(A, b, initial_guess, tolerance, max_iterations):
    n = len(b)
    x = initial_guess.copy()
    for _ in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            # Вычисляем сумму a_ij * x_j, где j != i
            sigma = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i+1:], x[i+1:])
            # Вычисляем новое значение x_i
            x_new[i] = (b[i] - sigma) / A[i, i]
        # Проверяем критерий останова
        if np.allclose(x, x_new, atol=tolerance):
            break
        x = x_new
    return x

# Начальное приближение
initial_guess = np.zeros_like(b)
# Порог сходимости
tolerance = 1e-5
# Максимальное количество итераций
max_iterations = 1000

# Запускаем метод Зейделя
result = seidel_method(A, b, initial_guess, tolerance, max_iterations)

print("Решение системы уравнений:", result)
