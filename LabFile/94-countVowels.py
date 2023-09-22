# 94-WAP to count number of vowels and consonants in a text file.
import os
os.getcwd()
os.chdir(r"C:\Users\Singhal\OneDrive\Desktop\Python Training\LabFile")
f=open("file1.txt",'r')

s=f.read()

vow=['A','a','E','e','I','i','O','o','U','u']
vowCount=0
constCount=0
for i in s:
    if (i>'A' and i<='Z') or (i>='a' and i<='z'):
        if i in vow:
            vowCount+=1
        else:
            constCount+=1
print("Number of vowels = {} \nNumber of consonants = {}".format(vowCount,constCount))

f.close()