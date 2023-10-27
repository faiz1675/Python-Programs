#50-Write a pandas program to create a line plot of the opening closing stock prices
#of alphabet inc between two specific dates. Use the alphabet_stock_data.csv
#file to extract the data

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(r"C:\Users\Singhal\OneDrive\Desktop\Python Training\Advance-Python_LabFile\stock.xlsx")

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

x=df['Open']
y=df['Close']

plt.plot(x, label='Opening Price')
plt.plot(y, label='Closing Price')

plt.title('Opening and Closing Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

plt.legend(loc=4)
plt.show()