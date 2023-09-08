import matplotlib.pyplot as plt
import numpy as np

# Define callback methods for the functions
def quadratic_function(x):
    return x**2 + 5*x - 1

def cubic_function(x):
    return x**3 + 2*x**2 - 5*x - 3

# Function to plot the specified function
def plot_function(function, function_label, color):
    x = np.linspace(-5, 5, 400)
    y = function(x)
    
    plt.plot(x, y, label=function_label, color=color)

# Create a plot for the specified functions
plt.figure(figsize=(8, 6))

plot_function(quadratic_function, 'y = x**2 + 5*x - 1', 'blue')
plot_function(cubic_function, 'y = x**3 + 2*x**2 - 5*x - 3', 'red')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.grid(True)
plt.title('Quadratic and Cubic Functions')

plt.show()
