import matplotlib.pyplot as plt
import numpy as np

# Example data
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 9]

# Create the bar chart
x = np.arange(len(categories))
plt.bar(x, values)
plt.xticks(x, categories)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
