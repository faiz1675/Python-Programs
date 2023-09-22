# 95-WAP to count number of words, lines, and characters in a text file.
import os
os.getcwd()
os.chdir(r"C:\Users\Singhal\OneDrive\Desktop\Python Training\LabFile")

f=open('file1.txt','r')
s=f.readlines()
countWord=0
countChar=0
for i in s:
    nl=i.split(' ')
    for j in nl:
        countChar+=len(j)
    countWord+=len(nl)
print("Total words = ",countWord)
print("Total lines = ",len(s))
print("Total characters in a string",countChar)

f.close()