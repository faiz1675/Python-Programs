# 97-WAP to handle multiple exception.
a=5
b=2
try:
    a/b
except ZeroDivisionError as obj:
    print(obj)
except NameError as obj:
    print(obj)
else:
    print(a/b)