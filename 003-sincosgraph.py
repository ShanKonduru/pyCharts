import matplotlib.pyplot as plt
import numpy as np

# Define callback methods for different functions

def sine_squared_function(x):
    return np.sin(x)

def tan_squared_function(x):
    return np.tan(x) 

# Function to plot the specified function
def plot_function(function, function_label, color):
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    y = function(x)
    
    plt.plot(x, y, label=function_label, color=color)

# Create a plot for the specified functions
plt.figure(figsize=(10, 6))

plot_function(sine_squared_function, 'y = sin(x)', 'green')
plot_function(tan_squared_function, 'y = tan(x)', 'purple')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.grid(True)
plt.title('sin vs tan Functions')

plt.show()
