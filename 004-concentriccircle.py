import matplotlib.pyplot as plt
import numpy as np

# Define the center point
center = (0, 0)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot concentric circles with increasing radii
for radius in range(1, 21):  # You can adjust the number of circles as needed
    circle = plt.Circle(center, radius, fill=False, linestyle='dotted', linewidth=0.7)
    ax.add_patch(circle)

# Set axis limits to ensure the circles are visible
ax.set_xlim(-21, 21)
ax.set_ylim(-21, 21)

# Set aspect ratio to be equal to avoid distortion
ax.set_aspect('equal', adjustable='box')

# Add labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a title
plt.title('Concentric Circles Expanding to Infinity')

# Show the plot
plt.grid(True)
plt.show()
