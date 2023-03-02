import math


def f(x):
    return x ** 3 * math.exp(3 * x)


def golden_section_search(a, b, epsilon):
    inter = 0
    phi = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    while abs(b - a) > epsilon:
        inter += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = b - (b - a) / phi
        else:
            a = x1
            x1 = x2
            x2 = a + (b - a) / phi
    x_min = (a + b) / 2
    f_min = f(x_min)
    return x_min, f_min, inter


def newton_method(x0, epsilon):
    inter = 0
    while True:
        inter += 1
        fx_d = 3 * math.exp(3 * x0) * x0 * x0 * (x0 + 1)
        fx_dd = 3 * math.exp(3 * x0) * x0 * (3 * x0 * x0 + 6 * x0 + 2)
        x1 = x0 - fx_d / fx_dd
        if abs(fx_d) <= epsilon:
            break
        x0 = x1
    return x1, f(x1), inter


# Значения
a = -1.1
b = 1
epsilon = 1e-2

x_min_gs, f_min_gs, interas = golden_section_search(a, b, epsilon)
x_min_newton, f_min_newton, interas1 = newton_method(a, epsilon)

print("Метод 'Золотого сечения':")
print("Минимум функции:", f_min_gs)
print("Минимальная точка:", x_min_gs)
print("Кол-во итераций:", interas)

print("Метод Ньютона:")
print("Минимум функции:", f_min_newton)
print("Минимальная точка:", x_min_newton)
print("Кол-во итераций:", interas1)