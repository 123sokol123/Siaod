import numpy as np


def gauss_seidel(A, b, initial_guess, tol=1e-6, max_iter=1000):
    """
    Решает систему уравнений Ax = b с помощью метода Гаусса-Зейделя.

    Параметры:
        A (numpy.ndarray): Матрица коэффициентов.
        b (numpy.ndarray): Вектор правой части.
        initial_guess (numpy.ndarray): Начальное приближение для решения.
        tol (float): Точность сходимости.
        max_iter (int): Максимальное количество итераций.

    Возвращает:
        numpy.ndarray: Вектор решения.
    """
    n = len(b)
    x = initial_guess.copy()
    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            # Разбиваем A на L (нижнетреугольную) и U (верхнетреугольную) части
            # L - нижнетреугольная часть A включая диагональ
            # U - верхнетреугольная часть A без диагонали
            L = np.tril(A, k=0)
            U = A - L
            # Вычисляем x_i^(k+1) с помощью формулы итерации Гаусса-Зейделя
            x_new[i] = (b[i] - np.dot(U[i, :], x_new) - np.dot(L[i, :i], x_new[:i])) / A[i, i]
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Метод Гаусса-Зейделя не сошелся в пределах максимального количества итераций")


# Пример использования
# Определение коэффициентов системы уравнений
A = np.array([[3, 1, 1],
              [1, 5, -1],
              [2, 0, 3,],
              ])
b = np.array([-2, 8, 1])

# Начальное приближение
initial_guess = np.zeros_like(b)

# Вызов метода Гаусса-Зейделя
solution = gauss_seidel(A, b, initial_guess)
print("Решение:", solution)
