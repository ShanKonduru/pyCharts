import matplotlib.pyplot as plt
import numpy as np

# Number of circles to draw
num_circles = 100

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Initialize the center point
center = (0, 0)

# Initialize color flag
color_flag = True

# Set the initial radius and angle increment
radius = 0.1
angle_increment = 0.1

for _ in range(num_circles):
    # Calculate the x and y coordinates of the circle's edge
    x = center[0] + radius * np.cos(np.arange(0, 2 * np.pi, 0.01))
    y = center[1] + radius * np.sin(np.arange(0, 2 * np.pi, 0.01))

    # Plot the circle with alternating colors
    if color_flag:
        ax.plot(x, y, color="black")
    else:
        ax.plot(x, y, color="white")

    # Toggle the color flag
    color_flag = not color_flag

    # Increase the radius and angle increment for the next circle
    radius += 0.1
    angle_increment += 0.1

# Set axis limits to ensure the circles are visible
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Set aspect ratio to be equal to avoid distortion
ax.set_aspect("equal", adjustable="box")

# Add a title
plt.title("Hypnotic Circles Starting from Center (Black and White)")

# Show the plot
plt.grid(True)
plt.show()
