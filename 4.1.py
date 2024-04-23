import numpy as np

class LagrangeInterpolation:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values

    def interpolate(self, x):
        n = len(self.x_values)
        result = 0.0
        for i in range(n):
            term = self.y_values[i]
            for j in range(n):
                if i != j:
                    term *= (x - self.x_values[j]) / (self.x_values[i] - self.x_values[j])
            result += term
        return result

# Пример использования
if __name__ == "__main__":
    # Табличные значения
    x_values = np.array([1, 2, 3, 4, 5])
    y_values = np.array([5.1, 3.4, 3.2, 2.7, 2.55])

    # Создание объекта для интерполяции
    lagrange_interpolator = LagrangeInterpolation(x_values, y_values)

    # Точки для интерполяции
    interpolation_points = np.array([1.5, 2.5, 3.5, 4.5])

    # Интерполяция и вывод результатов
    print("Лагранж:")
    for point in interpolation_points:
        interpolated_value = lagrange_interpolator.interpolate(point)
        print(f"При x={point}, y={interpolated_value}")