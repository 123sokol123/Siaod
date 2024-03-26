import math

def simpsons_rule(f, a, b, n):
    """
    Вычисляет определенный интеграл функции f на интервале [a, b]
    с использованием метода Симпсона с n отрезками.

    :param f: функция, которую нужно проинтегрировать
    :param a: нижний предел интегрирования
    :param b: верхний предел интегрирования
    :param n: количество подотрезков
    :return: приближенное значение определенного интеграла
    """
    h = (b - a) / n
    x = a
    integral = f(a) + f(b)

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral

def adaptive_simpsons_rule(f, a, b, min_n, max_n, tol):
    """
    Использует метод Симпсона для вычисления определенного интеграла функции f на интервале [a, b]
    с контролем погрешности и удвоением числа разбиений.

    :param f: функция, которую нужно проинтегрировать
    :param a: нижний предел интегрирования
    :param b: верхний предел интегрирования
    :param min_n: минимальное количество подотрезков
    :param max_n: максимальное количество подотрезков
    :param tol: требуемая абсолютная погрешность
    :return: приближенное значение определенного интеграла
    """
    n = min_n
    integral_old = simpsons_rule(f, a, b, n)
    n *= 2
    integral_new = simpsons_rule(f, a, b, n)

    while abs(integral_new - integral_old) / 15 > tol and n <= max_n:
        integral_old = integral_new
        n *= 2
        integral_new = simpsons_rule(f, a, b, n)

    if n > max_n:
        raise ValueError("Максимальное количество разбиений достигнуто без достижения требуемой точности.")

    return integral_new, n, abs(integral_new - integral_old) / 15

def main():
    def f(x):
        return x**4 * math.log(x + math.sqrt(x**2 - 0.36))

    a = float(input("Введите нижний предел интегрирования: "))
    b = float(input("Введите верхний предел интегрирования: "))
    min_n = 10
    max_n = 10000
    tol = 10 ** -4

    integral, num_partitions, actual_error = adaptive_simpsons_rule(f, a, b, min_n, max_n, tol)
    print("Приближенное значение интеграла:", integral)
    print("Фактическое количество разбиений:", num_partitions)
    print("Фактическая погрешность по методу Рунге:", actual_error)

if __name__ == "__main__":
    main()
