import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line Plot of sin(x)')
plt.show()
