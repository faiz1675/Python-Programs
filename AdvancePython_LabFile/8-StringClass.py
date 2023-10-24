# 8- Create a class called String that stores a string and all its status details such as number of 
# uppercase letters, lowercase letters, vowels ,consonants and space in instance variables. 
# a. Write methods named as count_uppercase, count_lowercase, count_vowels, count_consonants 
# and count_space to count corresponding values. 
# b. Write a method called display to print string along with all the values computed by methods in (a)

class String:
    def __init__(self,st):
        self.st=st
    def count_uppercase(self):
        cu=0
        for i in self.st:
            if ord(i)>=65 and ord(i)<=90:
                cu+=1
        return cu
    def count_lowercase(self):
        cl=0
        for i in self.st:
            if ord(i)>=97 and ord(i)<=122:
                cl+=1
        return cl
    def count_vowel(self):
        v=['a','A','e','E','i','I','o','O','u','U']
        cv=0
        for i in self.st:
            if i in v:
                cv+=1
        return cv
    def count_consonant(self):
        v=['a','A','e','E','i','I','o','O','u','U']
        cc=0
        for i in self.st:
            if i not in v:
                cc+=1
        return cc
    def count_whitespace(self):
        cs=0
        for i in self.st:
            if i==' ':
                cs+=1
        return cs
    def display(self):
        print("Total UpperCase = ",self.count_uppercase())
        print("Total LowerCase = ",self.count_lowercase())
        print("Total Vowel = ",self.count_vowel())
        print("Total Consonant = ",self.count_consonant())
        print("Total Whitespace = ",self.count_whitespace())

obj=String("Welcome to NIET")
obj.display()