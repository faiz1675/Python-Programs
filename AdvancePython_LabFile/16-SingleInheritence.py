# 16-Write a program to create class Employee. Display the personal information and salary 
# details of 5 employees using single inheritance.

class Employee:
    def __init__(self,name,age,desig,salary) -> None:
        self.name=name
        self.age=age
        self.desig=desig
        self.salary=salary
        
    def personalInformation(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Designation = ",self.desig)
        print("Salary = ",self.salary)
    
class EmpSalary(Employee):
    def __init__(self, name, age, desig,salary) -> None:
        super().__init__(name, age, desig,salary)

emp1=Employee('Faiz',23,'Developer',89000)
emp1.personalInformation()
emp2=Employee('Afiya Khan',22,'Manager',55000)
emp2.personalInformation()
emp3=Employee('Himanshu',24,'Developer',49000)
emp3.personalInformation()
emp4=Employee('Ujjwal',24,'Marketing',55000)
emp4.personalInformation()
emp5=Employee('Abhishek',23,'Tester',44000)
emp5.personalInformation()