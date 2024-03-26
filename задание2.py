import random
import math

def monte_carlo_integration(func, a, b, num_samples):
    integral_sum = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        integral_sum += func(x)

    integral = (b - a) * integral_sum / num_samples
    return integral

# Периодическая функция (синусоида с изменяемым периодом)
def periodic_function(x, k=1):
    return math.sin(2 * math.pi * k * x)

# Пикообразная функция (функция Гаусса)
def gaussian_function(x):
    return math.exp(-x ** 2)

# Произвольная функция ( 12 вариант)
def new_function(x):
    return x ** 4 * math.log(x + math.sqrt(x ** 2 - 0.36))

# Ввод границ интегрирования с консоли
a = float(input("Введите начало интервала интегрирования: "))
b = float(input("Введите конец интервала интегрирования: "))

# Количество случайных точек для оценки
num_samples = 10000000

# Интегрирование периодической функции
periodic_integral = monte_carlo_integration(periodic_function, a, b, num_samples)
print("Интеграл периодической функции:", periodic_integral)

# Интегрирование пикообразной функции
gaussian_integral = monte_carlo_integration(gaussian_function, a, b, num_samples)
print("Интеграл пикообразной функции:", gaussian_integral)

# Интегрирование произвольной функции
new_integral = monte_carlo_integration(new_function, a, b, num_samples)
print("Интеграл новой функции:", new_integral)