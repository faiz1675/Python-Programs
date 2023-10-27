#36-WAP to create a generator that starts counting from 0 and raise an exception 
#when counter is equal to 10

def count_generator():
    counter = 0
    while True:
        if counter == 10:
            raise ValueError("Counter reached 10")
        yield counter
        counter += 1

# Create the count generator
gen = count_generator()

# Iterate over the generator and print the values
try:
    for num in gen:
        print(num, end=' ')
except ValueError as e:
    print("\nException:",str(e))