# 12- Create a class called Complex. Write a menu driven program to read, display, add and 
# subtract two complex numbers by creating corresponding instance methods.

class Complex:
    def __init__(self,r=None,i=None) -> None:
        self.r=r
        self.i=i

    def display(self):
        if self.i<=0:
            return (str(self.r)+str(self.i)+'j')
        else:
            return (str(self.r)+'+'+str(self.i)+'j')
        
    def add(self,other):
        temp=Complex()
        temp.r=self.r+other.r
        temp.i=self.i+other.i
        return temp
    
    def subtract(self,other):
        temp=Complex()
        temp.r=self.r-other.r
        temp.i=self.i-other.i
        return temp

if __name__=='__main__':

    c1=None
    c2=None
    while True:
            print("1-Read\t2-Display\n3-Add\t4-Subtract\n0-Exit")
            choice=int(input("Enter any choice to perform operation:"))
            if choice==1:
                print("Enter the real and imaginary part of first complex number: ")
                r1,i1=map(int, input().split())
                c1=Complex(r1,i1)
                print("Enter the real and imaginary part of second complex number: ")
                r2,i2=map(int, input().split())
                c2=Complex(r2,i2)
            elif choice==2:
                print("First Complex Number = ",c1.display())
                print("Second Complex Number = ",c2.display())
            elif choice==3:
                if c1 and c2:
                    result=c1.add(c2)
                    print("Sum of two complex numbers = ",result.display())
                else:
                    print("Firstly read the two complex numbers.")
            elif choice==4:
                if c1 and c2:
                    result=c1.subtract(c2)
                    print("Difference of two complex numbers = ",result.display())
                else:
                    print("Firstly read the two complex numbers.")
            elif choice==0:
                break
            else:
                print("Enter any valid choice")