# 10-Write a program that has a class Numbers with a list as an instance variable. 
# a. Write a method called insert_element that takes values from user. 
# b. Write a class method called find_max to find and print largest value in the list. 

class Numbers:
    def __init__(self):
        self.insert_element()
    def insert_element(self):
        self.lst=[]
        n=int(input("Enter number of elements in list: "))
        print("Enter element of the list: ")
        for i in range(n):
            x=int(input())
            self.lst.append(x)
    def find_max(self):
        maxm=max(self.lst)
        print("Maximum element in the list is = ",maxm)
n=Numbers()
n.find_max()