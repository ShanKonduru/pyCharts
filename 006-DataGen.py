import csv
import random

# Generate 1000 random data points and store them in a list
data = [random.uniform(15.0, 24.0) for _ in range(1000)]

# Write the data to a CSV file
with open(".\data.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["value"])  # Write the header
    for value in data:
        print (value)
        csv_writer.writerow([value])
