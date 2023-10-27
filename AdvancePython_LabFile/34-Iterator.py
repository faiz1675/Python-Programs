# 34. WAP that creates an iterator to print the square of number.

sqlist=[i**2 for i in range(1,6)]
itr=iter(sqlist)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))




# class SquareIterator:
#     def __init__(self, start, stop):
#         self.current = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.stop:
#             raise StopIteration
#         else:
#             result = self.current ** 2
#             self.current += 1
#             return result

# # Create an iterator to print the square of each number in the range 1 to 5
# for square in SquareIterator(1, 6):
#     print(square)



