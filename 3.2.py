import numpy as np


def levenberg_marquardt(F, J, x0, tol=10e-4, max_iter=100, lambda_init=0.01, lambda_factor=10):
    """
    Реализация метода Левенберга-Марквардта для решения системы нелинейных алгебраических уравнений F(x) = 0.

    :param F: Функция, задающая систему уравнений F(x) = 0.
    :param J: Якобиан (матрица первых производных) функции F(x).
    :param x0: Начальное приближение к решению системы.
    :param tol: Допустимая погрешность (по умолчанию 1e-6).
    :param max_iter: Максимальное количество итераций (по умолчанию 100).
    :param lambda_init: Начальное значение параметра Левенберга (по умолчанию 0.01).
    :param lambda_factor: Фактор увеличения параметра Левенберга при необходимости (по умолчанию 10).
    :return: Найденное приближенное значение решения системы.
    """
    x = x0
    lambda_ = lambda_init
    for _ in range(max_iter):
        fx = F(x)
        if np.linalg.norm(fx) < tol:
            return x
        Jx = J(x)
        dx = np.linalg.solve(Jx.T @ Jx + lambda_ * np.eye(len(x)), -Jx.T @ fx)
        x_new = x + dx
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        fx_new = F(x_new)
        if np.linalg.norm(fx_new) < np.linalg.norm(fx):
            lambda_ /= lambda_factor
            x = x_new
        else:
            lambda_ *= lambda_factor
    raise ValueError("Достигнуто максимальное количество итераций. Решение не найдено.")


# Реализация функций F и J для данной системы уравнений
def F(x):
    return np.array([
        np.cos(x[1] - 1) + x[0] - 0.5,  # уравнение 1: cos(y - 1) + x - 0.5 = 0
        x[1] - np.cos(x[0]) - 3  # уравнение 2: y - cos(x) - 3 = 0
    ])


def J(x):
    return np.array([
        [-np.sin(x[1] - 1), 1],  # Якобиан для уравнения 1 по x и по y
        [np.sin(x[0]), 1]  # Якобиан для уравнения 2 по x и по y
    ])


# Пример использования новой функции:
x0 = np.array([0.1, 0.1])
solution = levenberg_marquardt(F, J, x0)
print("Приближенное значение решения системы:", solution)
