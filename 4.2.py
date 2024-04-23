import numpy as np

# Функция, для которой будем строить сплайн
def f(x):
    return np.sin(x)

# Определение отрезка и шага
a = 1.00
b = 1.20
h = 0.04

# Создание равномерной сетки значений x
x_values = np.arange(a, b + h, h)

# Вычисление значений функции на сетке
y_values = f(x_values)

# Построение кубического сплайна
def cubic_spline(x, x_values, y_values):
    n = len(x_values) - 1
    for i in range(n):
        if x >= x_values[i] and x <= x_values[i+1]:
            h = x_values[i+1] - x_values[i]
            a = y_values[i]
            b = (y_values[i+1] - y_values[i]) / h
            c = (1 / h**2) * ((y_values[i+1] - y_values[i]) / h - (y_values[i] - y_values[i-1]) / (x_values[i] - x_values[i-1]))
            d = (1 / h**3) * ((y_values[i] - y_values[i-1]) / (x_values[i] - x_values[i-1]) - (y_values[i+1] - y_values[i]) / h)
            return a + b * (x - x_values[i]) + c * (x - x_values[i])**2 + d * (x - x_values[i])**3

# Значения сплайна в заданных точках
points_to_interpolate = [1.05, 1.09, 1.13, 1.15, 1.17]
spline_values = [cubic_spline(x, x_values, y_values) for x in points_to_interpolate]

# Вывод результатов
for x, y_interp in zip(points_to_interpolate, spline_values):
    print(f"Значение сплайна в точке x = {x}: {y_interp}")