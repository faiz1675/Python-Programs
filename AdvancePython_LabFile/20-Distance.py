# 20. Write a program that create a class Distance with members km and metres. Derive classes 
# School and office which store the distance from your house to school and office along with other 
# details.

class Distance:
    def __init__(self,km,met) -> None:
        self.km=km
        self.met=met
    def distance(self):
        return self.km*1000+self.met
class School(Distance):
    def __init__(self, km, met) -> None:
        super().__init__(km, met)

    def display(self):
        print(f"Distance between house and school = {self.distance()} metre")

class Office(Distance):
    def __init__(self, km, met) -> None:
        super().__init__(km, met)

    def display(self):
        print(f"Distance between house and office = {self.distance()} metre")

a=School(10,5)
b=Office(2,100)
a.display()
b.display()