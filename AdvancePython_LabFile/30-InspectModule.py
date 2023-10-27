# 30. WAP to inspect the program code using the functions of inspect module

import inspect
import collections
import numpy

def display(a):
    return a*a

class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

print(inspect.getclasstree(inspect.getmro(C)))
print(inspect.ismethod(collections.Counter))
print(inspect.isclass(A))
print(inspect.ismodule(numpy))
print(inspect.isfunction(display))