# 74-WAP to compute the reverse of the given number using recursion.

def reverseNumber(n):
    if n<10:
        return n
    return int(str(n%10)+str(reverseNumber(n//10)))


n=int(input("Enter any number to find the sum of digit: "))
print("Reverser of {} is = {}".format(n,reverseNumber(n)))