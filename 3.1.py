import numpy as np

def f(x):
    # Если x - скаляр, преобразовать его в массив
    x = np.atleast_1d(x)
    return x - np.sin(2 * x)

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

def newton_method_all_roots(func, df, initial_guesses, tol=1e-6, max_iter=100):
    roots = []
    for initial_guess in initial_guesses:
        x = initial_guess
        for _ in range(max_iter):
            f_val = func(x)
            df_val = df(x)
            delta_x = -f_val / df_val
            x = x + delta_x
            if abs(delta_x) < tol:
                roots.append(x)
                break
    return roots

# Ищем начальные приближения методом золотого сечения
initial_guesses = []
for i in range(-10, 10):
    initial_guesses.append(golden_section_search(lambda x: np.linalg.norm(f(x)), i, i+1))



# Находим все корни уравнения методом Ньютона
solutions = newton_method_all_roots(f, df, initial_guesses, tol=1e-4)

# Удаляем повторяющиеся корни, используя множество (set)
unique_solutions = list(set(round(root[0], 6) for root in solutions))

print("Корни уравнения:")
for i, root in enumerate(unique_solutions):
    print(f"Корень {i + 1}: {root:.6f}")
