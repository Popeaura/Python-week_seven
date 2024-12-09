# Line plot for average measurements across species
grouped.T.plot(kind='line', figsize=(10, 6))
plt.title('Average Measurements Across Iris Species')
plt.xlabel('Features')
plt.ylabel('Mean Value')
plt.legend(title='Species')
plt.show()
