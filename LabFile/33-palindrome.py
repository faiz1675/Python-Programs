# 33-WAP to reverse the given number. Also check whether the given number is in palindrome or not
n=int(input("Enter any number to find the reverse of number: "))
temp=n
s=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10

print("Reverse of Numbe {} is = {}".format(temp,s))
if temp==s:
    print("{} is a Pallindrome number".format(temp))
else:
    print("{} is not a Pallindrome number".format(temp))