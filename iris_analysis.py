import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris() 
data = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
data['species'] = iris.target
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows
print("First few rows of the dataset:")
print(data.head())

# Check data types
print("\nData types of each column:")
print(data.info())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Basic statistics
print("\nBasic statistics for numerical columns:")
print(data.describe())

# Group by species and compute the mean of numerical columns
print("\nMean values of numerical columns grouped by species:")
grouped = data.groupby('species').mean()
print(grouped)
