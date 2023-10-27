#48-WAP to count the number of missing values in each column
import pandas as pd

# create a sample DataFrame with missing values
df = pd.DataFrame({
    'A': [13, 2, None, 4,None],
    'B': [5, None, 7, 8,19],
    'C': [None, 10, None, None,28]
})

# count the number of missing values in each column
missing_values = df.isna().sum()

print(missing_values)