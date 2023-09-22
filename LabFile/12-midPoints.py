# 12-Python program to calculate midpoints of a line-segment.
print("Enter the co-ordiante points of A")
x1=int(input())
y1=int(input())
print("Enter the co-ordiante points of B")
x2=int(input())
y2=int(input())

x3=(x1+x2)/2
y3=(y1+y2)/2
print('The Mid Point of  A({},{}) and B({},{}) is = ({},{})'.format(x1,y1,x2,y2,x3,y3))