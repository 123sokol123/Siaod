import numpy as np
import random

# Функция для численного интегрирования методом Монте-Карло
def monte_carlo_integration(func, a, b, num_samples):
    integral_sum = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        integral_sum += func(x)

    integral = (b - a) * integral_sum / num_samples
    return integral

# Функция для вычисления коэффициентов ряда Фурье
def fourier_coefficients(func, period, num_terms, num_samples):
    coefficients = []
    for n in range(0, num_terms):
        a_n = (2 / period) * monte_carlo_integration(lambda x: func(x) * np.cos(2 * np.pi * n * x / period), 0, period, num_samples)
        b_n = (2 / period) * monte_carlo_integration(lambda x: func(x) * np.sin(2 * np.pi * n * x / period), 0, period, num_samples)
        coefficients.append((a_n, b_n))
    return coefficients

# Функция для вычисления значения ряда Фурье для данного n
def fourier_series_n(coefficients, x, n, period):
    a_n, b_n = coefficients[n]
    return a_n * np.cos(2 * np.pi * n * x / period) + b_n * np.sin(2 * np.pi * n * x / period)

# Функция для вычисления значения ряда Фурье в заданной точке x
def fourier_series(coefficients, x, period):
    series_sum = 0
    for n in range(len(coefficients)):
        series_sum += fourier_series_n(coefficients, x, n, period)
    return series_sum

# Пример использования

# Задаем функцию
def func(x):
    return np.sin(x) + np.cos(2 * x)

# Задаем параметры
period = 2 * np.pi
num_terms = 10
num_samples = 10000

# Вычисляем коэффициенты ряда Фурье
coefficients = fourier_coefficients(func, period, num_terms, num_samples)

# Выводим коэффициенты
for i, (a_n, b_n) in enumerate(coefficients):
    print(f'a_{i} = {a_n}, b_{i} = {b_n}')

# Вычисляем значения ряда Фурье для некоторых точек
x_values = np.linspace(0, period, 10)
for x in x_values:
    y = fourier_series(coefficients, x, period)
    print(f'f({x}) ≈ {y}')