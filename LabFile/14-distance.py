# 14-Python program to compute the distance between the points (x1, y1) and (x2, y2)
print("Enter the co-ordiante points of A")
x1=int(input())
y1=int(input())
print("Enter the co-ordiante points of B")
x2=int(input())
y2=int(input())

dis=((x1-x2)**2+(y1-y2)**2)**0.5
print('The distance between A({},{}) and B({},{}) is = {}'.format(x1,y1,x2,y2,dis))