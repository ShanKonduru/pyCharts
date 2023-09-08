import matplotlib.pyplot as plt
import numpy as np
import csv

# Read data from CSV file
data = []
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(float(row['value']))

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std_dev = np.std(data)

# Define control limits (e.g., UCL, LCL, USL, LSL)
UCL = mean + 3 * std_dev
LCL = mean - 3 * std_dev
USL = 21.0  # Upper Specification Limit (adjust as needed)
LSL = 19.0  # Lower Specification Limit (adjust as needed)

# Create a time axis (assuming each data point is taken at a different time)
time_axis = np.arange(len(data))

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
plt.plot(time_axis, data, marker='o', linestyle='-')

# Plot control limits
plt.axhline(UCL, color='r', linestyle='--', label='UCL')
plt.axhline(LCL, color='r', linestyle='--', label='LCL')
plt.axhline(USL, color='g', linestyle='--', label='USL')
plt.axhline(LSL, color='g', linestyle='--', label='LSL')

# Add labels and a legend
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

# Add a title
plt.title('Control Chart')

# Show the plot
plt.grid(True)
plt.show()
