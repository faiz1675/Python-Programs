# 4-Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a 
# constructor which takes the parameters x and y (these should all be numbers).

# a. Write an instance method called add which returns the sum of the attributes x and y. 
# b. Write a class method called multiply, which takes a single number parameter a and returns the 
# product of a and MULTIPLIER. 
# c. Write a static method called subtract, which takes two number objects, b and c, and returns b-c
# d. Write a method called value which returns a tuple containing the values of x and y

class Number:
    MULTIPLIER=8
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def multiply(cls,a):
        return a*cls.MULTIPLIER
    @staticmethod
    def subtract(b,c):
        return b-c
    def value(self):
        lst=[]
        lst.append(self.x)
        lst.append(self.y)
        return lst
n=Number(5,12)
print("Instance method: ",n.add())
print("Class Method = ",Number.multiply(4))
print("Static method = ",n.subtract(8,2))
print("Tuple = ",n.value())