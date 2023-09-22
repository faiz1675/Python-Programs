# 43-WAP to display all the Armstrong number from 1 to n

n=int(input('Enter number of terms you want to print the fibonaccii: '))

for i in range(1,n):
    ln=len(str(i))
    temp=i
    s=0
    while(i>0):
        r=i%10
        s=s+r**ln
        i=i//10
    if temp==s:
        print(temp,end=' ')
        
