# 37-WAP to compute the sum of following series up to the nth term. 1 + 𝑥1/1! + 𝑥2/2! +𝑥3/3! + …….

n=int(input("Enter the number of terms upto which you want to print: "))
s=1
for i in range(1,n+1):
    f=1
    for j in range(1,i+1):
        f=f*j
    s=s+(n**i//f)

print("Sum of the series is = ",s)


