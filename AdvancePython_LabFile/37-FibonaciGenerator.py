#37-WAP to create a generator to print the Fibonacii series

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create the Fibonacci generator
fib_gen = fibonacci_generator()

# Print the first 10 numbers in the Fibonacci series
for _ in range(10):
    print(next(fib_gen), end='  ')