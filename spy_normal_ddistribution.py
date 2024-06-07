import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import scipy


def get_data(ticker, start, end):
    data = yf.download(ticker, start, end)
    data = data.dropna()
    return data 

spy=(get_data('spy', '2000-01-01', '2022-10-10'))

print("heade",spy.head())

spy['SMA_50'] = spy['Adj Close'].rolling(window=50).mean()
spy['SMA_200'] = spy['Adj Close'].rolling(window=200).mean()
spy['SMA_100'] = spy['Adj Close'].rolling(window=100).mean()

spy['Percent Change'] = spy['Adj Close'].pct_change()*100

#bell curve of percent change frequency

ax=pd.Series(spy['Percent Change'])
ax.hist(bins=100)
plt.xlabel('Daily Percent Change')
plt.ylabel('Frequency')
plt.title('Bell Curve of Daily Percent Change spy')


# Generate 1000 random samples from a normal distribution with mean 0 and standard deviation 1
mean = 0
std = 1
samples = np.random.normal(mean, std, 1000)

# Plot the histogram with a density curve
plt.hist(samples, density=True)

# Calculate the x values for the normal distribution curve
x_min, x_max = plt.xlim()
x = np.linspace(x_min, x_max, 100)

# Calculate the y values for the normal distribution curve
y = (1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean)**2 / (2 * std**2)))


x1 = mean - std
x3 = mean - 2*std
x5 = mean - 3*std
x2 = mean + std
x4 = mean + 2*std
x6 = mean + 3*std

# Plot the 1 standard deviation line
plt.axvline(x1, color='g', linestyle='dashed', linewidth=2)

# Plot the 2 standard deviation line
plt.axvline(x2, color='g', linestyle='dashed', linewidth=2)

# Plot the 3 standard deviation line
plt.axvline(x3, color='y', linestyle='dashed', linewidth=2)
plt.axvline(x4, color='y', linestyle='dashed', linewidth=2)
plt.axvline(x5, color='r', linestyle='dashed', linewidth=2)
plt.axvline(x6, color='r', linestyle='dashed', linewidth=2)

ax.dropna(inplace=True)
#convert ax to numpy array with

bins = 10
mu, sigma = scipy.stats.norm.fit(ax)
best_fit_line = scipy.stats.norm.pdf(bins, mu, sigma)
plt.plot(bins, best_fit_line)

plt.show()



