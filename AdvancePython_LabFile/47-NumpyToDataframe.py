#47-WAP to convert a numpy array into a dataframe of given shape
import numpy as np
import pandas as pd

arr=np.array([[2,4,6,8],[10,12,14,16],[18,20,22,24]])
df=pd.DataFrame(arr)
print(df)