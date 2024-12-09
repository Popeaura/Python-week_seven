import pandas as pd
from sklearn.datasets import load_iris

#Load Iris dataset
iris = load_iris
data = pd.DataFrame(iris.data, columns=iris.feature_names)

#add the target (species)  to the dataFrame
data['species'] = iris.target
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

#Display the first few rows
print(data.head())

# Check data types
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Basic statistics
print(data.describe())

# Group by species and compute the mean of numerical columns
grouped = data.groupby('species').mean()
print(grouped)
