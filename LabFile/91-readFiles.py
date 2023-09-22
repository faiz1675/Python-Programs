# 91-WAP to read the content of whole file using read() function.
import os
os.getcwd()
os.chdir(r'C:\Users\Singhal\OneDrive\Desktop\Python Training\LabFile')
f=open('file1.txt','r')
s=f.read()
print(s)

f.close()