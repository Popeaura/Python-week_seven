import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)

# Create scatter plot
plt.scatter(x, y, c='blue', alpha=0.5, edgecolor='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot Example')
plt.show()
