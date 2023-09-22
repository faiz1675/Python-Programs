# 50-WAP to display the Floyd’s triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
p=1
for i in range(0,5):
    for j in range(0,i+1):
        print(p,end=' ')
        p+=1
    print()