# 27. Write a program to overload in operator. 

class OverloadOperator:
    def __init__(self,data) -> None:
        self.data=data
    
    def __contains__(self,item):
        return item in self.data

lst=OverloadOperator([1,2,3,4,5,6])
print(3 in lst)
print(12 in lst)