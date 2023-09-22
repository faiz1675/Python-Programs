# 77-WAP to create a new list consisting of odd numbers from the given list of numbers using
# filter() function.
lst=[3,2,9,6,4,7]
y=list(filter(lambda n:True if n%2!=0 else False,lst))
print("List of Odd Numbers: ",y)