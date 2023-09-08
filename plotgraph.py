import matplotlib.pyplot as plt
import numpy as np

def quadratic_function(x):
    return x**2 - 1

def cubic_function(x):
    return x**3 - 3

x = np.linspace(-5, 5, 400)

y_quadratic = quadratic_function(x)
y_cubic = cubic_function(x)

plt.figure(figsize=(8, 6))

plt.plot(x, y_quadratic, label='y = x^2 - 1', color='blue')
plt.plot(x, y_cubic, label='y = x^3 - 3', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.grid(True)
plt.title('Quadratic and Cubic Functions')

plt.show()
