# Bar chart: Average petal length per species
grouped['petal length (cm)'].plot(kind='bar', color=['#4CAF50', '#FFC107', '#2196F3'], figsize=(8, 5))
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()
