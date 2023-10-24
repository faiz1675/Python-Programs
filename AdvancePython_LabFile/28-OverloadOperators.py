# 28. WAP to create a Complex class having real and imaginary as it attributes. Overload the +,-
# ,/,* and += operators for objects of Complex class. 

class Complex:
    def __init__(self,real=None,img=None) -> None:
        self.real=real
        self.img=img
    def __add__(self,other):
        temp=Complex()
        temp.real=self.real+other.real
        temp.img=self.img+other.img
        return temp
    def __sub__(self,other):
        temp=Complex()
        temp.real=self.real-other.real
        temp.img=self.img-other.img
        return temp
    def __truediv__(self,other):
        temp=Complex()
        temp.real=self.real/other.real
        temp.img=self.img/other.img
        return temp
    def __mul__(self,other):
        temp=Complex()
        temp.real=self.real*other.real
        temp.img=self.img*other.img
        return temp
    def __str__(self) -> str:
        return f"{self.real},{self.img}"
    
c1=Complex(5,7)
c2=Complex(3,9)
print(c1+c2)