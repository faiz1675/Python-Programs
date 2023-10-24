# 21. Write a program to create an abstract class Vehicle. Derive three classes Car, Motorcycle and 
# Truck from it. Define appropriate methods and print the details of vehicle

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,model,noTyres,color) -> None:
        self.model=model
        self.noTyres=noTyres
        self.color=color

    @abstractmethod
    def displayDetails(self):
        pass

class Car(Vehicle):
    def __init__(self,model, noTyres, color,gear) -> None:
        super().__init__(model,noTyres, color)
        self.gear=gear

    def displayDetails(self):
        print("This is Car ",self.model)
        print("Number of tyres = ",self.noTyres)
        print(f"Color = {self.color}")
        print("Gear = ", self.gear)


class MotorCycle(Vehicle):
    def __init__(self, model, noTyres, color,isSport) -> None:
        super().__init__(model, noTyres, color)
        self.isSport=isSport
    def displayDetails(self):
        print("This is Bike ",self.model)
        print("Number of tyres = ",self.noTyres)
        print(f"Color = {self.color}")
        print("Is it a sport bike = ", self.isSport)

class Truck(Vehicle):
    def displayDetails(self):
        print("This is Truck ",self.model)
        print("Number of tyres = ",self.noTyres)
        print(f"Color = {self.color}")
# c=Car(4,'White',6)
# c.displayDetails()

# b=MotorCycle('R15',2,'Black','Yes')
# b.displayDetails()

t=Truck('Tata',12,'Brown')
t.displayDetails()
