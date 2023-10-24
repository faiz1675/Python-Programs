# 15- Write a program to illustrate the use of following built-in methods: a. hasattr(obj,attr) b. 
# getattr(object, attribute_name [, default]) c. setattr(object, name, value) d. delattr(class_name, 
# name)

class BuiltInMethod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of SampleClass
obj = BuiltInMethod("Faiz", 23)

# Using hasattr to check if an attribute exists
print("Attribute present :",hasattr(obj, 'name'))  # True
print("Attribute present :",hasattr(obj, 'salary'))  # False

# Using getattr to get the value of an attribute
n = getattr(obj, 'name')
print(f"Name: {n}")
default_value = getattr(obj, 'age')
print(f"Age: {default_value}")

# Using setattr to set a new attribute
setattr(obj, 'salary', 50000)
print(f"New Salary: {obj.salary}")

# Using delattr to delete an attribute
delattr(obj, 'age')
print("Age attribute deleted.")