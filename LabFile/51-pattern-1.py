# 51-WAP to display the following pattern.
# A
# A B
# A B C
# A B C D
# A B C D E

for i in range(0,5):
    ch=65
    for j in range(0,i+1):
        print(chr(ch+j),end=' ')
    print()