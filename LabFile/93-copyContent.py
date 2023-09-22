# 93-WAP to copy the contents of one file into another file.
import os
os.getcwd()
os.chdir(r"C:\Users\Singhal\OneDrive\Desktop\Python Training\LabFile")
f1=open("file1.txt",'r')
f2=open("file2.txt",'a')

s=f1.read()
f2.write(s)

f1.close()
f2.close()