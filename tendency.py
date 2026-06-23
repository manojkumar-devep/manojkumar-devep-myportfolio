import numpy as np
from scipy import stats

# Data set
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculations
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data).mode
variance = np.var(data, ddof=0)
std_deviation = np.sqrt(variance)

# Output
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")