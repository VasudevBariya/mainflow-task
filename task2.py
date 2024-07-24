import pandas as pd
import numpy as np
from scipy import stats

# Reading the CSV file
data = pd.read_csv('C:\\Users\\Vasudev\\Downloads\\01.Data Cleaning and Preprocessing.csv')

# Checking the type of the data object
print(type(data))

# Removing duplicate rows
data = data.drop_duplicates()

# Checking for null values
# print(data.isnull())
# print(data.isnull().sum())
# print(data.notnull())
# print(data.isnull().sum().sum())

# Handling null values
# data2 = data.fillna(value=0)
# print(data2)

# data2 = data.fillna(method='pad')
# print(data2)

# data2 = data.fillna(method='bfill')
# print(data2)

# Displaying the column names
print(data.columns)

# Dropping the 'Observation' column
data2.drop(['Observation'], axis=1, inplace=True)
print(data2.columns)

# Calculating IQR and removing outliers
d1 = data2.quantile(0.25)
d2 = data2.quantile(0.75)
IQR = d2 - d1
print(IQR)

data2 = data2[~((data2 < (d1 - 1.5 * IQR)) | (data2 > (d2 + 1.5 * IQR))).any(axis=1)]
print(data2)
