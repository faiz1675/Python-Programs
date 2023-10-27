#49-WAP to replace the missing values in a column of a dataframe by the mean value of that column 

import pandas as pd

# Create a sample DataFrame with missing values
df = pd.DataFrame({
    'A': [13, 2, None, 4,None],
    'B': [5, None, 7, 8,19],
    'C': [None, 10, None, None,28]
})

# Replace missing values with the mean of each column
print("Updated DataFrame after inserting the mean value:")
df_filled = df.fillna(df.mean())

print(df_filled)