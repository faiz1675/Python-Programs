# 92-WAP to read the existing file line by line. 
import os
os.getcwd()
os.chdir(r'C:\Users\Singhal\OneDrive\Desktop\Python Training\LabFile')
f=open('file1.txt','r')
s=f.readlines()
for i in s:
    print(i)

f.close()