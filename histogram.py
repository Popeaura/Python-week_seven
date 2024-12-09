import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.random(1000)

# Plot the histogram
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
