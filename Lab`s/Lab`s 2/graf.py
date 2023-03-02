from matplotlib import cm
from matplotlib.ticker import LogLocator
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """Анализируемая функция."""
    return (x[0]-1)**2 + (x[1]-2)**2


area = np.linspace(-4, 4, 100)
x, y = np.meshgrid(area, area)
z = f((x, y))

plt.contourf(x, y, z, 40, cmap=cm.jet, locator=LogLocator(2))
plt.colorbar(format="%.02f")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(alpha=0.75)
plt.show()