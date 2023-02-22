import numpy as np
import matplotlib.pyplot as plt


# Определяем функцию
def f(x):
    return x ** 3 * np.exp(3 * x)


# Задаём интервал и количество точек
x_vals = np.linspace(-1, 1, 1000)

# Вычисляем значения функции на интервале
y_vals = f(x_vals)

# Находим минимум и максимум
xmin, xmax = x_vals[np.argmin(y_vals)], x_vals[np.argmax(y_vals)]
ymin, ymax = np.min(y_vals), np.max(y_vals)

# Выводим результаты
print(f"Минимум функции: x = {xmin:.4f}, y = {ymin:.4f}")
print(f"Максимум функции: x = {xmax:.4f}, y = {ymax:.4f}")

# Строим график
plt.plot(x_vals, y_vals)
plt.scatter([xmin, xmax], [ymin, ymax], c=['g', 'r'], s=50)
plt.title("График функции f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
