#46-WAP to create a series from list, numpy array and dict
import numpy as np
import pandas as pd

lst=[3,5,7,9]
arr=np.arange(1,5)
dict1={1:'one',2:'two',3:'three',4:'four'}
print("Series using list")
dflist=pd.Series(lst)
print("Series using numpy array")
dfarr=pd.Series(arr)
print("Series using Dict")
dfdict=pd.Series(dict1)
print(dflist)
print(dfarr)
print(dfdict)