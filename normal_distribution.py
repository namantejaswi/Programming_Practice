import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Generate 1000 random samples from a normal distribution with mean 0 and standard deviation 1
mean = 0
std = 1
samples = np.random.normal(mean, std, 1000)

# Fit a normal distribution to the data
mu, std = norm.fit(samples)

# Plot the histogram with a density curve
plt.hist(samples, density=True)

# Calculate the x values for the normal distribution curve
x_min, x_max = plt.xlim()
x = np.linspace(x_min, x_max, 100)

# Calculate the y values for the normal distribution curve
y = norm.pdf(x, mu, std)

# Plot the normal distribution curve
plt.plot(x, y, color='r', linewidth=2)

# Add a title and labels
plt.title('Normal Distribution')
plt.xlabel('X')
plt.ylabel('Probability')

# Show the plot
plt.show()