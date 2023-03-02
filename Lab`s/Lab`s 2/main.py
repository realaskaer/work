import numpy as np
from numpy import linalg
from scipy.optimize import minimize

def f(X):
    return (X[0]-1)**2 + (X[1]-2)**2 + (X[2]-3)**2

def grad_f(X):
    return np.array([2*(X[0]-1), 2*(X[1]-2), 2*(X[2]-3)])

def hessian_f(X):
    return np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# 3(f, grad_f, hessian_f, x0, tol=1e-6, max_iter=100):
def golden_section_search(f, a, b, epsilon):
    inter = 0
    phi = (1 + np.sqrt(5)) / 2
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
    return x_min


def gradient_descent_newton(f, grad_f, hessian_f, x0, tol=1e-6, max_iter=1000):
    x = x0
    counter = 0
    for i in range(max_iter):
        counter += 1
        direction = -grad_f(x)
        alpha = golden_section_search(lambda alpha: f(x + alpha*direction), 0, 100, 1e-4)
        x_next = x + alpha*direction
        if np.linalg.norm(x_next - x) < tol:
            return x_next, counter
        x = x_next
    return x, counter



x0 = np.array([5, 6, 7])
x_min, _x = gradient_descent_newton(f, grad_f, hessian_f, x0)
print("Minimum point:", x_min)
print("Minimum value:", f(x_min))

from timeit import default_timer as timer
from scipy.optimize import minimize

guess = (0, 1)

start = timer()
min_point, iterations = gradient_descent_newton(f, grad_f, hessian_f, x0, tol=1e-6, max_iter=1000)
end = timer()

print("Custom implementation:")
print(f"\tMin point: {min_point}")
print(f"\tValue: {f(min_point)}")
print(f"\tIterations: {iterations}")
print(f"\tTime: {1000 * (end - start)} ms")

print()

start = timer()
minimized = minimize(f, x0, method="CG")
end = timer()

print("SciPy implementation")
print(f"\tMin point: {minimized.x}")
print(f"\tValue: {minimized.fun}")
print(f"\tIterations: {minimized.nit}")
print(f"\tTime: {1000 * (end - start)} ms")

start = timer()
minimized = minimize(f, x0, method="Nelder-Mead")
end = timer()

print("SciPy implementation ")
print(f"\tMin point: {minimized.x}")
print(f"\tValue: {minimized.fun}")
print(f"\tIterations: {minimized.nit}")
print(f"\tTime: {1000 * (end - start)} ms")

