#32-WAP using the reduce function to calculate the sum of first 10 Natural numbers

from functools import reduce

y=reduce(lambda a,b: a+b, range(1,11))
print(f"Sum of first 10 Natural Numbers = {y}")

