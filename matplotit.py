import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sqrt(8 + 8 * x - 4 * y - 4 * x**2 - y**2)


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

z = f(x, y)

plt.contour(x, y, z, levels=100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("f(x, y) = sqrt(8+8x -4y -4x^2-y^2)")
plt.show()
