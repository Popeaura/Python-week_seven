# Scatter plot: Sepal length vs Petal length
sns.scatterplot(data=data, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='viridis')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
