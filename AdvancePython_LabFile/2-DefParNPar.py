# 2-Write a program to implement default constructor, parameterized constructor, and destructor

# Default constructor
class DefaultCons:
    def pattern(self):
        for i in range(1,6):
            for j in range(0,i):
                print("*",end=' ')
            print()

d=DefaultCons()
d.pattern()

#Parameterized constructor            
class Parametarized:
    def __init__(self,n):
        self.n=n
    def square(self):
        sq=self.n*self.n
        print("Square of {} is = {}".format(self.n,sq))
obj=Parametarized(15)
obj.square()


#non-parametarized constructor
class NonParametarized:
    def __init__(self):
        self.a=15
    def checkEvenOdd(self):
        if self.a%2==0:
            print("It is an even number")
        else:
            print("It is an Odd number")
np=NonParametarized()
np.checkEvenOdd()