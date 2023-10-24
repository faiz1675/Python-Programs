# 13- Write a Program to illustrate the use of __str__(), __repr__(), __new__, __doc__, __dict__, 
# __name__ and __bases__ methods. 

class MagicMethod:
    def __new__(cls,name,salary,desg):
        print("__new__ magic method is created")
        inst=object.__new__(cls)
        return inst
    def __init__(self,name,salary,desg) -> None:
        self.name=name
        self.salary=salary
        self.desg=desg
    def __str__(self) -> str:
        return f"Name is = {self.name} and Salary= {self.salary}"
    def __repr__(self) -> str:
        return f"Name is = {self.name} and Designation = {self.desg}"
    
if __name__=='__main__':
    m=MagicMethod('Faiz',85000,'Developer')
    print(m)
    print(repr(m))