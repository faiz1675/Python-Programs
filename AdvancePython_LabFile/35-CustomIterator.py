# 35. WAP that creates a custom iterator to create even numbers

class EvenIterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result

# Create an iterator to generate even numbers up to 10
n=int(input("Enter the number upto you want to print even number: "))
even_iter = EvenIterator(n)

# Iterate over the even numbers and print them
print("Even numbers are: ")
for num in even_iter:
    print(num,end=' ')