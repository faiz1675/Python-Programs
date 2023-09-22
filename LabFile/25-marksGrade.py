# 25-WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by the student. It also prints grades according to the following criteria:
print("Enter the marks of any five subjects: ")
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

per=(a+b+c+d+e)/5
print("Your percentage is = ",per)
if per>91 and per<=100:
    print('Grade A')
elif per>81 and per<=90:
    print('Grade B')
elif per>61 and per<=80:
    print('Grade C')
elif per>51 and per<=60:
    print('Grade D')
elif per>41 and per<=50:
    print('Grade E')
else: 
    print('Grade F')