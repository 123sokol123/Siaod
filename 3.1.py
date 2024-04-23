import numpy as np


def f(x):
    # Вектор-функция для данной системы уравнений
    return np.array([x - np.sin(2 * x)])


def df(x):
    # Производная функции
    return np.array(1 - 2 * np.cos(2 * x))


def golden_section_search(func, a, b, tol=1e-6):
    gr = (1 + np.sqrt(5)) / 2  # Золотое сечение
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        if func(c) < func(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return (b + a) / 2


def newton_method(func, df, initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    for _ in range(max_iter):
        # Вычисляем значение функции и её производной в текущей точке
        f_val = func(x)
        df_val = df(x)

        # Решаем уравнение для получения приращения x
        delta_x = -f_val / df_val

        # Обновляем значение x
        x = x + delta_x

        # Проверяем условие остановки
        if abs(delta_x) < tol:
            break
    return x


# Ищем начальное приближение методом золотого сечения
initial_guess = golden_section_search(lambda x: np.linalg.norm(f(x)), -10, 10)

# Решаем уравнение методом Ньютона
solution = newton_method(f, df, initial_guess, tol=1e-4)

print("Решение уравнения методом золотого сечения + Ньютона:", solution)
