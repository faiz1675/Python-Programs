# 29. Write a program to inspect the object using type() ,id(), isinstance(), issubclass() and 
# callable() built-in function.

class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def display(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

class Engineer(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def profession(self):
        print(f"{self.name} is an Engineer")

p=Person("Faiz",23)
print("Type = ",type(p))
print("ID = ",id(p))
print("Is instance",isinstance(p,Person))
print("Is Engineer sub class of Person: ",issubclass(Engineer,Person))
print("Is Person sub class of Engineer: ",issubclass(Person,Engineer))
print(callable(Person))