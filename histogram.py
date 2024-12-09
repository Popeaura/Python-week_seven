# Histogram for petal length
sns.histplot(data['petal length (cm)'], bins=20, kde=True, color='purple')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()
